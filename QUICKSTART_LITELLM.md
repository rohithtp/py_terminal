# LiteLLM Quick Start Guide

Complete setup in 5 minutes.

## 1️⃣ Install LiteLLM (1 minute)

```bash
# Ensure venv is activated
source /workspaces/py_terminal/venv/bin/activate

# Install LiteLLM
pip install litellm
```

## 2️⃣ Set Your API Key (1 minute)

**Choose ONE provider:**

### Option A: OpenAI (GPT-4)
```bash
export OPENAI_API_KEY="sk-..."  # Replace with your actual key
export LLM_MODEL="gpt-4"
```

### Option B: Anthropic (Claude)
```bash
export ANTHROPIC_API_KEY="sk-ant-..."  # Replace with your actual key
export LLM_MODEL="claude-3-5-sonnet-20241022"
```

### Option C: Ollama (Local, Free, No API Key)
```bash
# In one terminal:
ollama serve

# In another terminal:
export LLM_PROVIDER="ollama"
export LLM_MODEL="qwen2.5-coder:1.5b"
```

## 3️⃣ Verify Installation (2 minutes)

```bash
cd /workspaces/py_terminal

# Run verification script
python3 verify_llm_setup.py
```

**Expected output:**
```
✅ Import Check
✅ Client Module Import  
✅ Configuration Check
✅ Client Initialization
✅ LLM Health Check
✅ Simple API Call
✅ JSON Mode

Total: 7/7 passed
🎉 All verifications passed! LiteLLM is ready to use.
```

## 4️⃣ Use the Client (1 minute)

### Simple Text Response
```python
from ai.client import get_client

client = get_client()
response = client.call([
    {"role": "user", "content": "What is 2+2?"}
])
print(response)
```

### JSON Response
```python
from ai.client import get_client
import json

client = get_client()
response = client.call_json([
    {"role": "user", "content": 'Return JSON: {"answer": 4, "correct": true}'}
])
print(json.dumps(response, indent=2))
```

### Stream Response (for long outputs)
```python
from ai.client import get_client

client = get_client()
for token in client.stream([
    {"role": "user", "content": "Write a haiku about Python"}
]):
    print(token, end="", flush=True)
```

## 5️⃣ Integration with Your Project

### In `ai/preflight.py`
```python
from ai.client import get_client

def analyze_command_with_llm(cmd: str) -> dict:
    client = get_client()
    response = client.call_json([
        {"role": "system", "content": "You are a shell command safety analyzer."},
        {"role": "user", "content": f"Analyze this command: {cmd}"}
    ])
    return response
```

### In `safety_net.py`
```python
from ai.client import get_client

client = get_client()
# Use client.call() or client.call_json() as needed
```

---

## Configuration Reference

| Variable | Default | Options |
|----------|---------|---------|
| `LLM_PROVIDER` | `openai` | `openai`, `anthropic`, `ollama`, `huggingface` |
| `LLM_MODEL` | `gpt-4` | `gpt-4`, `claude-3-5-sonnet-20241022`, `qwen2.5-coder:1.5b`, `ollama/llama2`, etc. |
| `LLM_TIMEOUT` | `30` | seconds (number) |
| `LLM_MAX_RETRIES` | `3` | number of retries |
| `ENABLE_CACHE` | `true` | `true` or `false` |

## Troubleshooting

| Issue | Fix |
|-------|-----|
| `ModuleNotFoundError: litellm` | `pip install litellm` |
| `API key not found` | Set `OPENAI_API_KEY` or `ANTHROPIC_API_KEY` |
| `Connection timeout` | Increase `LLM_TIMEOUT` or check internet |
| `Ollama not found` | Run `ollama serve` in separate terminal |
| `JSON parse error` | Ensure API response is valid JSON |

## Next Steps

1. ✅ Complete verification with `python3 verify_llm_setup.py`
2. 📝 Review [llm_setup_plan.md](hackathon/llm_setup_plan.md) for detailed information
3. 🔧 Integrate client into `ai/preflight.py` and `safety_net.py`
4. 🧪 Test with sample commands
5. 📊 Monitor performance and adjust `LLM_TEMPERATURE` as needed

---

For detailed documentation, see:
- [LiteLLM Setup Plan](hackathon/llm_setup_plan.md) - Complete setup guide with verification steps
- [LiteLLM Docs](https://docs.litellm.ai/) - Official documentation
