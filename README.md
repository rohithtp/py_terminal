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

1. **Create and activate a virtual environment** (already set up):
   ```sh
   python3 -m venv venv
   source venv/bin/activate
   ```

2. **Install dependencies**:
   ```sh
   pip install --break-system-packages rich
   ```

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