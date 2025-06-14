# Terminal Web

A terminal-based UI web project using Python and [Rich](https://github.com/Textualize/rich) for beautiful terminal output.

## Features
- Terminal UI with styled panels
- Easy to extend for more features

## Setup

1. Create and activate a virtual environment (already set up):
   ```sh
   python3 -m venv venv
   source venv/bin/activate
   ```
2. Install dependencies:
   ```sh
   pip install --break-system-packages rich
   ```

## Usage

Run the main program:
```sh
python terminal_web/main.py
```

You should see a styled welcome message in your terminal.

## Project Structure
```
terminal_web/
    __init__.py
    main.py
README.md
venv/
``` 