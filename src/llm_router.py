"""
Multi-provider LLM router with automatic fallback.

Design rules:
  1. Route by task. Long generation -> Gemini. Short calls -> Groq.
  2. The VERIFIER must be a different model family than the DRAFTER.
     Same-model self-checking is not verification.
  3. On 429 / 5xx / timeout -> rotate to the next provider, never fail loudly.
  4. All providers exhausted -> raise. The pipeline must STOP, not publish degraded output.
"""

import json, os, time, urllib.request, urllib.error, random

UA = "channel-ops/1.0"


def _post(url, payload, headers, timeout=180, retries=2):
    data = json.dumps(payload).encode()
    last = None
    for attempt in range(retries + 1):
        req = urllib.request.Request(url, data=data, method="POST")
        req.add_header("Content-Type", "application/json")
        req.add_header("User-Agent", UA)
        for k, v in headers.items():
            req.add_header(k, v)
        try:
            with urllib.request.urlopen(req, timeout=timeout) as r:
                return json.loads(r.read().decode("utf-8", "ignore"))
        except urllib.error.HTTPError as e:
            body = e.read().decode("utf-8", "ignore")
            last = f"HTTP {e.code}: {body[:160]}"
            if e.code in (429, 500, 502, 503, 504):
                time.sleep(2 ** attempt + random.random())
                continue
            raise RuntimeError(last)
        except Exception as e:
            last = f"{type(e).__name__}: {e}"
            time.sleep(2 ** attempt)
    raise RuntimeError(last)


class Provider:
    def __init__(self, name, kind, models, base, key, family):
        if isinstance(models, str):
            models = [m.strip() for m in models.split(",") if m.strip()]
        self.name, self.kind, self.models = name, kind, models
        self.model = models[0]
        self.base, self.key, self.family = base, key, family

    def complete(self, prompt, system=None, max_tokens=6000, temperature=0.7):
        last = None
        for model in self.models:
            try:
                return self._complete(model, prompt, system, max_tokens, temperature)
            except Exception as e:
                last = f"{model}: {e}"
                continue
        raise RuntimeError(last)

    def _complete(self, model, prompt, system=None, max_tokens=6000, temperature=0.7):
        if self.kind == "gemini":
            url = f"{self.base}/models/{model}:generateContent?key={self.key}"
            payload = {
                "contents": [{"role": "user", "parts": [{"text": prompt}]}],
                "generationConfig": {
                    "temperature": temperature,
                    "maxOutputTokens": max_tokens,
                },
            }
            if system:
                payload["systemInstruction"] = {"parts": [{"text": system}]}
            r = _post(url, payload, {})
            return r["candidates"][0]["content"]["parts"][0]["text"]

        url = f"{self.base}/chat/completions"
        msgs = []
        if system:
            msgs.append({"role": "system", "content": system})
        msgs.append({"role": "user", "content": prompt})
        r = _post(url,
                  {"model": model, "messages": msgs,
                   "temperature": temperature, "max_tokens": max_tokens},
                  {"Authorization": f"Bearer {self.key}"})

        ch = (r.get("choices") or [{}])[0]
        msg = ch.get("message") or {}

        # Reasoning models (gpt-oss, R1-style) often return null `content`
        # and put the actual output in `reasoning` / `reasoning_content`.
        txt = (msg.get("content")
               or msg.get("reasoning")
               or msg.get("reasoning_content")
               or ch.get("text")
               or "")
        txt = txt.strip()
        if not txt:
            raise RuntimeError(
                f"empty completion (finish_reason={ch.get('finish_reason')})")
        return txt


def build_providers():
    """Instantiate whatever keys are present in the environment."""
    out = []
    g = os.environ.get("GEMINI_API_KEY")
    if g:
        out.append(Provider("gemini", "gemini",
                            os.environ.get("GEMINI_MODELS",
                                           "gemini-3.8-flash,gemini-3.5-flash-lite,gemini-3.5-flash"),
                            "https://generativelanguage.googleapis.com/v1beta",
                            g, "google"))
    k = os.environ.get("GROQ_API_KEY")
    if k:
        out.append(Provider("groq", "openai",
                            os.environ.get("GROQ_MODELS", "openai/gpt-oss-120b,qwen/qwen3.8-27b,openai/gpt-oss-20b"),
                            "https://api.groq.com/openai/v1", k, "openai-oss"))
    k = os.environ.get("OPENROUTER_API_KEY")
    if k:
        out.append(Provider("openrouter", "openai",
                            os.environ.get("OPENROUTER_MODELS",
                                           "nvidia/nemotron-3-super-120b-a12b:free,openrouter/free"),
                            "https://openrouter.ai/api/v1", k, "nvidia"))
    return out


class Router:
    def __init__(self, providers, log=None):
        self.providers = providers
        self.log = log if log is not None else []
        self.usage = {}

    def call(self, task, prompt, system=None, prefer=None,
             avoid_family=None, max_tokens=6000, temperature=0.7):
        """
        task         : label for logs
        prefer       : provider name to try first
        avoid_family : never use this model family (used to force verifier diversity)
        """
        order = list(self.providers)
        if prefer:
            order.sort(key=lambda p: 0 if p.name == prefer else 1)
        if avoid_family:
            divers = [p for p in order if p.family != avoid_family]
            if divers:
                order = divers

        errors = []
        for p in order:
            try:
                t0 = time.time()
                txt = p.complete(prompt, system, max_tokens, temperature)
                model_used = p.model
                dt = time.time() - t0
                self.usage[p.name] = self.usage.get(p.name, 0) + 1
                self.log.append(f"[{task}] {p.name}/{model_used} ok in {dt:.1f}s")
                return txt, p
            except Exception as e:
                errors.append(f"{p.name}: {e}")
                self.log.append(f"[{task}] {p.name} FAILED -> {str(e)[:90]}")
                continue

        raise RuntimeError(f"all providers failed for {task} :: " + " | ".join(errors))
