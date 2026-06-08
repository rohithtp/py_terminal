# Demo Script: AI Safety Net for py_terminal

This walkthrough shows the completed AI safety net, including Tier-2 preflight, healing suggestions, and offline fallback.

## 1. Launch the application

```bash
source venv/bin/activate
python terminal_web/main.py
```

## 2. Run a safe command

- Choose `3. Run Single Command`
- Enter: `echo hello`
- Choose mode: `capture`

Expected: command runs immediately with output shown.

## 3. Trigger a risky preflight warning

- Choose `3. Run Single Command`
- Enter: `rm -rf /tmp/testdir`
- Choose mode: `capture`

Expected:
- Preflight panel warns with risk level `IRREVERSIBLE`
- If LLM is available, the panel also shows AI summary, affected resources, and reversibility note
- The command is blocked unless the typed confirmation matches

## 4. Trigger a failed command and healing suggestion

- Choose `3. Run Single Command`
- Enter: `mkdir /root/should-fail`
- Choose mode: `capture`

Expected:
- Command fails with a permission error
- A healing panel appears with diagnosis and a suggested fix
- If you type `yes`, the fix is re-run through the preflight flow

## 5. Demonstrate offline or heuristic fallback

- Set `OFFLINE_MODE=true` and restart the app, or leave `OPENAI_API_KEY` unset
- Run a risky command again

Expected:
- The tool still performs the heuristic Tier-1 scan
- The UI falls back gracefully without causing a crash
- Only the non-LLM warning panel appears

## 6. Demonstrate SQLite Caching

- Run a risky command that triggers an LLM preflight, like `rm -rf /tmp/testdir2`
- Cancel the execution.
- Run the exact same command again.

Expected:
- The preflight panel appears instantly (zero latency).
- A cache hit avoids making a duplicate LLM API call.

## 7. Show status capture

- From the menu, choose `6. Show Status`

Expected:
- The repository workspace status report is printed
- It includes git metadata, dependency checks, and system info

## Notes for judges

- The AI safety net is designed to prevent risky shell execution and to offer safe remediation when commands fail.
- The healing loop is protected by rerunning suggested fixes through the same preflight checks.
- The tool works even when LLM access is unavailable, which is important for a robust demo.
