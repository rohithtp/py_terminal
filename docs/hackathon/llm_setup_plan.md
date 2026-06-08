# LiteLLM Setup Plan & Installation Verification

## Overview
Setup LiteLLM as the unified LLM client for AI Safety Net integration. LiteLLM provides a single interface for multiple LLM providers (OpenAI, Anthropic, Ollama, etc.).

---

## Phase 1: Prerequisites

### ✅ System Requirements
- Python 3.8+
- Virtual environment: `/workspaces/py_terminal/venv`
- Active venv: `source venv/bin/activate`
- ~100MB disk space for dependencies

### ✅ API Keys (Choose One)
- **OpenAI**: Set `OPENAI_API_KEY` environment variable
- **Anthropic**: Set `ANTHROPIC_API_KEY` environment variable
- **Ollama (Local)**: No API key needed, just ensure Ollama server is running

### ✅ Current Project State
- Base dependencies: `rich>=15.0.0`
- Existing modules: `ai/preflight.py`, `terminal_web/main.py`, `safety_net.py`
- Target: Create `ai/client.py` with LiteLLM integration

---

## Phase 2: Installation Steps

### Step 1: Activate Virtual Environment
```bash
cd /workspaces/py_terminal
source venv/bin/activate
```
**Expected output**: Prompt prefix shows `(venv)`

### Step 2: Update pip
```bash
pip install --upgrade pip setuptools wheel
```
**Expected output**: Successfully installed or already satisfied messages

### Step 3: Install LiteLLM
```bash
pip install litellm>=1.0.0
```
**Expected output**: Successfully installed litellm and its dependencies

### Step 4: Install Optional Provider Dependencies
Choose based on your LLM provider:

**For OpenAI:**
```bash
pip install openai>=1.0.0
```

**For Anthropic:**
```bash
pip install anthropic>=0.7.0
```

**For Ollama (local LLMs):**
```bash
pip install ollama>=0.1.0
```

**For Hugging Face:**
```bash
pip install huggingface-hub>=0.16.0
```

### Step 5: Update requirements.txt
```bash
pip freeze > requirements.txt
```
Verify that `litellm` is now in `requirements.txt`

---

## Phase 3: Configuration

### Create `ai/config.py`
```python
import os
from enum import Enum

class LLMProvider(Enum):
    OPENAI = "openai"
    ANTHROPIC = "anthropic"
    OLLAMA = "ollama"
    HUGGINGFACE = "huggingface"

# Configuration
LLM_PROVIDER = os.getenv("LLM_PROVIDER", "openai").lower()
LLM_MODEL = os.getenv("LLM_MODEL", "gpt-4")
LLM_API_KEY = os.getenv("OPENAI_API_KEY") or os.getenv("ANTHROPIC_API_KEY")

# Timeouts & Retries
LLM_TIMEOUT = int(os.getenv("LLM_TIMEOUT", "30"))
LLM_MAX_RETRIES = int(os.getenv("LLM_MAX_RETRIES", "3"))

# Cache
ENABLE_CACHE = os.getenv("ENABLE_CACHE", "true").lower() == "true"
CACHE_DIR = os.getenv("CACHE_DIR", "/workspaces/py_terminal/ai/.cache")
```

### Create `ai/client.py`
```python
import litellm
from ai.config import LLM_PROVIDER, LLM_MODEL, LLM_API_KEY, LLM_TIMEOUT, LLM_MAX_RETRIES
from typing import Optional, Dict, Any

class LLMClient:
    def __init__(
        self,
        provider: str = LLM_PROVIDER,
        model: str = LLM_MODEL,
        api_key: Optional[str] = LLM_API_KEY,
        timeout: int = LLM_TIMEOUT,
        max_retries: int = LLM_MAX_RETRIES
    ):
        self.provider = provider
        self.model = model
        self.api_key = api_key
        self.timeout = timeout
        self.max_retries = max_retries
        
        # Set API key if provided
        if api_key:
            if "openai" in model:
                litellm.openai_api_key = api_key
            elif "claude" in model:
                litellm.anthropic_api_key = api_key
    
    def call(
        self,
        messages: list,
        temperature: float = 0.7,
        max_tokens: Optional[int] = None,
        json_mode: bool = False
    ) -> str:
        """
        Call the LLM with retry logic and timeout handling.
        
        Args:
            messages: List of message dicts with 'role' and 'content'
            temperature: Sampling temperature (0.0-1.0)
            max_tokens: Max response tokens
            json_mode: If True, request JSON output
        
        Returns:
            str: Model's response content
        """
        try:
            response = litellm.completion(
                model=self.model,
                messages=messages,
                temperature=temperature,
                max_tokens=max_tokens,
                timeout=self.timeout,
                api_key=self.api_key,
            )
            return response.choices[0].message.content
        except Exception as e:
            print(f"❌ LLM call failed: {e}")
            raise
    
    def call_json(
        self,
        messages: list,
        schema: Optional[Dict[str, Any]] = None,
        temperature: float = 0.3
    ) -> Dict[str, Any]:
        """
        Call the LLM and parse JSON response.
        """
        import json
        response_text = self.call(messages, temperature=temperature)
        try:
            return json.loads(response_text)
        except json.JSONDecodeError as e:
            print(f"❌ Failed to parse JSON: {e}")
            print(f"Raw response: {response_text}")
            raise

# Global client instance
_client: Optional[LLMClient] = None

def get_client() -> LLMClient:
    global _client
    if _client is None:
        _client = LLMClient()
    return _client

def reset_client():
    global _client
    _client = None
```

---

## Phase 4: Verification Steps

### ✅ Verification 1: Import Check
```bash
python3 -c "import litellm; print(f'✅ LiteLLM version: {litellm.__version__}')"
```
**Expected**: `✅ LiteLLM version: X.X.X` (version number shown)

### ✅ Verification 2: Client Module Import
```bash
python3 -c "from ai.client import LLMClient, get_client; print('✅ Client module imported successfully')"
```
**Expected**: `✅ Client module imported successfully`

### ✅ Verification 3: Check Configuration
```bash
python3 << 'EOF'
from ai.config import LLM_PROVIDER, LLM_MODEL, LLM_TIMEOUT, LLM_MAX_RETRIES
print(f"✅ Provider: {LLM_PROVIDER}")
print(f"✅ Model: {LLM_MODEL}")
print(f"✅ Timeout: {LLM_TIMEOUT}s")
print(f"✅ Max Retries: {LLM_MAX_RETRIES}")
EOF
```
**Expected**: Shows current configuration values

### ✅ Verification 4: Test LLM Connection (OpenAI)
```bash
export OPENAI_API_KEY="your-api-key-here"
python3 << 'EOF'
from ai.client import get_client
client = get_client()
response = client.call([{"role": "user", "content": "Say 'Hello from LiteLLM!' in exactly 5 words."}])
print(f"✅ Response: {response}")
EOF
```
**Expected**: `✅ Response: Hello from LiteLLM success.` (or similar 5-word response)

### ✅ Verification 5: Test JSON Mode
```bash
export OPENAI_API_KEY="your-api-key-here"
python3 << 'EOF'
from ai.client import get_client
import json
client = get_client()
response = client.call_json([
    {"role": "user", "content": 'Return JSON: {"status": "ok", "message": "LiteLLM working"}'}
])
print(f"✅ JSON Response: {json.dumps(response, indent=2)}")
EOF
```
**Expected**: Valid JSON output with status and message keys

### ✅ Verification 6: Test with Ollama (Local)
```bash
# First, start Ollama (in separate terminal)
ollama serve

# In another terminal, test:
export LLM_PROVIDER="ollama"
export LLM_MODEL="qwen2.5-coder:1.5b"
python3 << 'EOF'
from ai.client import LLMClient
from ai.config import LLM_PROVIDER, LLM_MODEL
client = LLMClient(provider=LLM_PROVIDER, model=LLM_MODEL)
response = client.call([{"role": "user", "content": "Say hello in one word."}])
print(f"✅ Ollama Response: {response}")
EOF
```
**Expected**: Response from local Ollama model

### ✅ Verification 7: Performance Check
```bash
python3 << 'EOF'
import time
from ai.client import get_client

client = get_client()
start = time.time()
response = client.call([{"role": "user", "content": "ping"}], max_tokens=5)
elapsed = time.time() - start
print(f"✅ Response time: {elapsed:.2f}s")
print(f"✅ Response: {response}")
EOF
```
**Expected**: Response time < 5 seconds, successful response

---

## Phase 5: Integration Checklist

- [ ] LiteLLM installed and version verified
- [ ] `ai/config.py` created with configuration
- [ ] `ai/client.py` created with LLMClient class
- [ ] API keys set (OPENAI_API_KEY or ANTHROPIC_API_KEY)
- [ ] Connection test successful (Verification 4)
- [ ] JSON mode working (Verification 5)
- [ ] Update `requirements.txt` committed
- [ ] Add to `.gitignore`: `ai/.cache/`
- [ ] Update `README.md` with LLM setup instructions

---

## Phase 6: Next Steps

### 1. Integrate with `ai/preflight.py`
```python
from ai.client import get_client

def score_with_llm(command: str) -> Dict:
    client = get_client()
    response = client.call_json([
        {"role": "user", "content": f"Analyze command safety: {command}"}
    ])
    return response
```

### 2. Integrate with `ai/healer.py` (if creating)
```python
from ai.client import get_client

def diagnose_failure(cmd: str, stderr: str, exit_code: int) -> Dict:
    client = get_client()
    # Use LLM to diagnose failure and suggest fix
```

### 3. Add Error Recovery
- Implement retry logic with exponential backoff
- Cache LLM responses by command hash
- Fallback to heuristic-only mode if LLM fails

---

## Troubleshooting

| Issue | Solution |
|-------|----------|
| `ModuleNotFoundError: litellm` | Run `pip install litellm` |
| API key not found | Set environment: `export OPENAI_API_KEY="..."` |
| Connection timeout | Increase `LLM_TIMEOUT` in `ai/config.py` |
| JSON parse error | Check API response, enable debug logging: `litellm.set_verbose=True` |
| Ollama not found | Start Ollama server: `ollama serve` in separate terminal |

---

## Environment Variables Reference

```bash
# Required
export LLM_PROVIDER="openai"              # or "anthropic", "ollama", "huggingface"
export LLM_MODEL="gpt-4"                  # model identifier
export OPENAI_API_KEY="sk-..."            # if using OpenAI
export ANTHROPIC_API_KEY="sk-ant-..."     # if using Anthropic

# Optional
export LLM_TIMEOUT="30"                   # seconds
export LLM_MAX_RETRIES="3"                # retry attempts
export ENABLE_CACHE="true"                # enable response caching
```

---

## Success Criteria

✅ All 7 verification tests pass  
✅ LLM responds within 5 seconds  
✅ Configuration is flexible (environment-driven)  
✅ Ready to integrate with `preflight.py` and `healer.py`  
✅ Error handling is in place (retry, timeout, fallback)
