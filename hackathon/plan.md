# Plan: AI Safety Net for `py_terminal`

A unified pre/post-execution AI layer that shares one interception point, one Rich panel system, and one LLM client. Goal: ship to hackathon by **June 7** (11 days from today).

---

## 1. The Core Architectural Insight

Both features are the same shape:

```
[command] → [AI inspects something] → [Rich panel] → [user decides] → [maybe execute]
```

Pre-Flight inspects the *command string* before running. Self-Healing inspects the *failure artifacts* (stderr + exit code) after running. Same wrapper, same UI primitives, two trigger points. Build the scaffolding once.

The bonus narrative beat: **healing suggestions get fed back through pre-flight**. The AI's fix could itself be `rm -rf` something — so the safety net protects you from its own suggestions. That recursion is the demo moment.

---

## 2. Module Layout

Add these to your existing tree (names suggested — adapt to your conventions):

```
py_terminal/
├── ai/
│   ├── __init__.py
│   ├── client.py          # LLM client wrapper (Claude/OpenAI/local), retry, timeout
│   ├── preflight.py       # Risk scoring (heuristics + LLM)
│   ├── healer.py          # Failure → suggested fix
│   ├── prompts.py         # All prompt templates in one file
│   └── cache.py           # SQLite cache: hash(cmd+ctx) → response
├── ui/
│   ├── panels.py          # PreflightPanel, HealingPanel, shared scaffolding
│   └── confirm.py         # Tiered confirmation (Enter / y / typed phrase)
├── safety_net.py          # The wrapper that ties it all together
└── config.py              # Risk thresholds, model choice, offline flag
```

The single `safety_net.run(cmd)` function replaces (or wraps) your current execution entry point. Everything else hangs off it.

---

## 3. Component Specs

**`preflight.py` — two-tier risk scoring**

Tier 1 is pure heuristics, runs in microseconds, no API call. Pattern-match against a curated list: `rm -rf`, `dd of=`, `mkfs`, `chmod -R 777`, `git push --force`, `git reset --hard`, `DROP TABLE`, `> /dev/sd*`, `kubectl delete`, `terraform destroy`, `:(){:|:&};:`, etc. Each pattern maps to a risk level: `SAFE | MUTATING | DESTRUCTIVE | IRREVERSIBLE`.

Tier 2 only fires if Tier 1 returns `MUTATING` or above, OR if a config flag enables "always explain." The LLM call returns `{plain_english_summary, affected_resources, reversibility_note}`. Cached aggressively — the same command in the same cwd shouldn't re-hit the API.

**`healer.py` — single LLM call with rich context**

Inputs sent to the model: the command, stderr (truncated to ~2KB tail), exit code, cwd, OS, and optionally the last 3 commands from history. Output schema (request JSON mode):

```json
{
  "diagnosis": "one-sentence root cause",
  "suggested_command": "the fix, or null if not auto-fixable",
  "explanation": "2-3 sentences why this fixes it",
  "confidence": 0.0
}
```

If `confidence < 0.6`, render the panel as "best guess" with a softer CTA.

**`panels.py` — three Rich layouts, one design language**

Use `rich.layout.Layout` + `rich.panel.Panel` consistently. Color tokens: green for safe, yellow for mutating, red for destructive, magenta for AI-generated. Every AI panel gets a tiny `✨ AI` badge in the corner so users always know what's machine-written.

**`confirm.py` — tiered confirmation matching risk**

- `SAFE`: no prompt
- `MUTATING`: Enter to proceed, Esc to abort
- `DESTRUCTIVE`: `y/N` with default No
- `IRREVERSIBLE`: must type a confirmation phrase (e.g. the command name)

Same UI is reused for accepting healing suggestions.

---

## 4. The Unified Flow

```python
def run(cmd: str) -> Result:
    risk = preflight.score(cmd)
    if risk.level >= MUTATING:
        if not panels.show_preflight(risk).confirmed:
            return Result.aborted()

    result = execute_with_status_capture(cmd)   # your existing code

    if result.failed:
        fix = healer.diagnose(cmd, result)
        choice = panels.show_healing(fix)
        if choice == "apply" and fix.suggested_command:
            return run(fix.suggested_command)   # recursion → preflight re-runs
    return result
```

That recursion is six lines of code and an entire feature in itself.

---

## 5. Eleven-Day Schedule

**Days 1–2 (May 27–28): Skeleton + heuristics.** Stand up the `ai/` and `ui/` modules as no-op stubs. Implement `safety_net.run()` as a passthrough. Build the Tier-1 heuristic pattern list with ~30 rules and unit tests. By end of Day 2, dangerous commands should print a static warning panel — no LLM yet.

**Days 3–4 (May 29–30): LLM client + pre-flight Tier 2.** Wire up the LLM client with timeout, retry, and an offline mock mode for testing. Build prompt templates in `prompts.py`. Connect Tier 2 pre-flight; commands now get AI-written explanations. Add the SQLite cache.

**Days 5–6 (May 31 – June 1): Self-Healing path.** Hook into your existing `status_capture` failure path. Implement `healer.diagnose()` and the healing panel. Test against a curated list of common failures: missing binary, wrong port, permission denied, git conflict, Python import error, etc.

**Day 7 (June 2): Close the loop.** Wire healing suggestions back through `safety_net.run()` so they re-trigger pre-flight. Record a short clip of this happening — it's your headline demo moment.

**Days 8–9 (June 3–4): Polish.** Config file (model choice, risk thresholds, opt-out flags). Offline mode that uses only heuristics. Streaming LLM responses into the Rich panel so it feels live. Keyboard shortcuts. Error states (API down, rate limited, malformed JSON).

**Day 10 (June 5): Submission assets.** README with before/after GIFs. A `DEMO.md` script you can walk a judge through in 90 seconds. The Copilot-narrative writeup: which commits Copilot wrote, what prompts you used, what it got wrong. Submission post draft.

**Day 11 (June 6): Buffer + submit.** Bug-fix day. Submit early on June 6 to leave room for the June 7 deadline.

---

## 6. Key Technical Decisions to Make on Day 1

**Which LLM?** Claude (Haiku 4.5 for speed/cost on pre-flight, Sonnet for healing diagnoses) or OpenAI. Pick one, abstract behind `ai/client.py` so a judge can plug in their own key.

**API key handling.** Read from env var (`ANTHROPIC_API_KEY` or `OPENAI_API_KEY`). Never log it. If missing at startup, fall back to heuristics-only mode with a friendly message — don't crash.

**Latency budget.** Pre-flight Tier 2 must complete in under ~800ms or the UX dies. Use the smallest fast model, short prompts, JSON mode, and aggressive caching. Stream the response so the panel populates progressively.

**Offline mode.** Required for hackathon judging — judges may not want to wire their key. Heuristics-only path must be fully functional and demo-able.

---

## 7. The Demo Narrative (write this on Day 10, but plan for it now)

A 90-second judge walkthrough that hits all four rubric categories:

1. Run a safe command → no interruption. *(Shows the tool isn't annoying.)*
2. Run `rm -rf ./build` → yellow Mutating panel, plain-English explanation, Enter to proceed.
3. Run a typo'd command that fails → red failure, magenta Healing panel slides in with diagnosis and fix.
4. Press `a` to apply the fix → **pre-flight catches it again** because the fix touches a protected path → judge sees the recursion live.
5. Cut to README showing the 11-month-old baseline vs. today's diff.

That's your Completion Arc, UX, Originality, and Tech Use in one shot.

---

## 8. Risks and Cuts

If you're behind by **Day 6**, cut Tier 2 pre-flight explanations and ship heuristics-only pre-flight + full self-healing. The recursion still works; you lose only the AI-written pre-flight prose.

If you're behind by **Day 8**, cut the SQLite cache (use an in-memory dict) and cut streaming.

Do **not** cut: the recursion (it's the demo), the offline mode (judges need it), or the README before/after (it's the Completion Arc score).

---

Want me to draft the actual `prompts.py` templates next — pre-flight risk explainer and healer diagnostic — so you've got the LLM calls ready to drop in on Day 3?