# Terminal Web

A powerful terminal-based UI web project using Python and [Rich](https://github.com/Textualize/rich) for beautiful terminal output with advanced command execution capabilities.

## ✨ Features

### 🎯 **Core Features**
- **Beautiful Terminal UI** with styled panels and rich formatting
- **Interactive Menu System** with logical grouping
- **Command Execution** with multiple execution modes
- **Real-time Command Monitoring** for long-running processes
- **Comprehensive Error Handling** with user-friendly messages

### 🚀 **Advanced Command Execution**
- **Single Command Execution** with interactive/capture modes
- **Multiple Commands Execution** with batch processing
- **Interactive Mode** for real-time commands (top, htop, ping, etc.)
- **Capture Mode** for output collection and display
- **Timeout Protection** (30-second default) to prevent hanging
- **Keyboard Interrupt Support** (Ctrl+C) for user control

### 🛡️ **Safety & User Experience**
- **Logical Menu Organization** by functionality
- **Clear Mode Selection** for each command
- **Comprehensive Output Display** (stdout, stderr, exit codes)
- **Graceful Error Handling** with detailed feedback
- **User-friendly Prompts** with validation

## 🛠️ Setup

1. **Create and activate a virtual environment**:
   ```sh
   python3 -m venv venv
   source venv/bin/activate
   ```

2. **Install dependencies**:
   ```sh
   pip install -r requirements.txt
   ```

3. **Configure environment variables**:
   ```sh
   cp .env.example .env
   export LLM_API_KEY="your-openai-api-key"
   export LLM_PROVIDER="openai"
   export LLM_MODEL="gpt-4"
   ```

## 🚀 Quickstart

### Run locally
```sh
source venv/bin/activate
python terminal_web/main.py
```

### Run with Docker
```sh
docker build -t py-terminal:latest .
docker run --rm -it \
  -e LLM_API_KEY="$LLM_API_KEY" \
  -e LLM_PROVIDER="openai" \
  -e LLM_MODEL="gpt-4" \
  py-terminal:latest
```

> Use `-it` so the interactive terminal menu works correctly.

## 🎮 Usage

### **Starting the Application**
```sh
python terminal_web/main.py
```

### **Menu Options**

#### **Basic Operations**
- **Option 1: Say Hello** - Simple greeting message
- **Option 2: Show Project Info** - Displays content from `info.md` file

#### **Command Execution**
- **Option 3: Run Single Command** - Execute one command with mode selection
- **Option 4: Execute Multiple Commands** - Batch execute multiple commands

#### **System**
- **Option 5: Exit** - Safely exit the application

### **Command Execution Modes**

#### **Interactive Mode**
- **Best for**: Real-time monitoring, long-running commands
- **Examples**: `top`, `htop`, `ping`, `tail -f`, `watch`
- **Features**: 
  - Real-time output display
  - Full terminal interaction
  - Ctrl+C to interrupt
  - No timeout (runs until completion or interruption)

#### **Capture Mode**
- **Best for**: Quick commands, output collection
- **Examples**: `ls`, `ps`, `df`, `date`, `whoami`
- **Features**:
  - Collects all output before display
  - 30-second timeout protection
  - Shows stdout, stderr, and exit codes
  - Safe for potentially hanging commands

### **Usage Examples**

#### **Single Command Execution**
```
1. Choose Option 3: Run Single Command
2. Enter command: top
3. Choose mode: interactive
4. Use Ctrl+C to stop when done
```

#### **Multiple Commands Execution**
```
1. Choose Option 4: Execute Multiple Commands
2. Enter commands one by one:
   - ls -la
   - ps aux
   - df -h
   - done
3. Choose mode for each command
4. View results for each command
```

#### **Long-running Commands**
```
Command: ping google.com
Mode: interactive
Result: Real-time ping output with Ctrl+C to stop

Command: top
Mode: interactive  
Result: Full top interface with process monitoring
```

## 📁 Project Structure
```
py_terminal/
├── terminal_web/
│   ├── __init__.py
│   └── main.py          # Main application with all features
├── README.md            # This file
├── info.md             # Project information (optional)
├── venv/               # Virtual environment
└── LICENSE
```

## 🔧 Technical Details

### **Dependencies**
- **Rich**: Beautiful terminal formatting and UI components
- **subprocess**: Command execution and process management
- **signal**: Process control and interruption handling

### **Key Features Implementation**
- **Dual Execution Modes**: Interactive vs Capture for different use cases
- **Process Management**: Proper handling of long-running processes
- **Error Recovery**: Graceful handling of timeouts and interruptions
- **User Experience**: Clear prompts, validation, and feedback

## 🎯 Use Cases

### **System Administration**
- Process monitoring with `top`/`htop`
- System information gathering
- Batch command execution

### **Development**
- Quick command testing
- Output collection and analysis
- Interactive debugging

### **Monitoring**
- Real-time system monitoring
- Log file tailing
- Network connectivity testing

## 🚀 Future Enhancements

Potential features for future development:
- Command history and favorites
- Custom command aliases
- Output export capabilities
- Remote command execution
- Plugin system for custom commands

## 📝 License

This project is licensed under the terms specified in the LICENSE file. 

## 🔎 Status Capture Utility

This repository includes a lightweight status-capture utility to audit the
workspace, collect git metadata, system/runtime info, and dependency health.

Usage:

```sh
# Run the status capture CLI (pretty output)
python -m terminal_web.status_capture

# JSON output
python -m terminal_web.status_capture --json

# Or use from the interactive menu: run the app and choose "Show Status"
python terminal_web/main.py
```

Programmatically, call `gather_status(path='.')` to get a dict and
`print_status(status)` to print a readable report.

### AI Safety Net

This project includes a lightweight AI safety layer for command execution:

- **Tier-1 heuristics** detect risky commands like `rm -rf`, `git push --force`, and `terraform destroy`
- **Tier-2 AI preflight** uses an LLM to summarize risk, affected resources, and reversibility notes
- **Healing suggestions** diagnose failed commands and propose safer fixes
- **Offline fallback** keeps the app usable even when no API key is present

### Demo and Submission Assets

- `hackathon/DEMO.md` includes a 90-second walkthrough script for judges
- `terminal_web/status_capture.py` reports repo and environment health
- The app is designed to work with and without LLM access, which is important for hackathon judging

### Project Judgment

Use the same utility to score the project on four criteria:

```sh
python -m terminal_web.status_capture --judge
```

For JSON-only judgment output:

## Hackathon: Final Submission

This repository contains the completed "AI Safety Net" hackathon feature.

- **Tier-1 Heuristic Scanner:** Detects dangerous commands locally without API calls.
- **Tier-2 AI Preflight:** Uses LLMs to generate risk summaries, affected resources, and reversibility notes for `MUTATING+` risk levels.
- **Self-Healing Workflow:** Diagnoses failed commands (e.g., permissions, missing files) and generates safe fix suggestions via the LLM, which are re-run through the preflight safety loop.
- **SQLite Caching:** Caches preflight AI evaluations to avoid duplicate API calls and ensure zero latency for repeated commands.
- **Status Capture:** A built-in telemetry utility to verify repo and dependency health.
- **Robust UI:** Rich panel rendering for warnings, healing suggestions, and offline graceful degradation when APIs are unavailable.

```sh
python -m terminal_web.status_capture --judge --judge-json
```
