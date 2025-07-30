#!/usr/bin/env python3
"""
Build script for creating standalone executables using PyInstaller
"""

import os
import sys
import subprocess
import platform

def build_executable():
    """Build standalone executable using PyInstaller"""
    
    # Install PyInstaller if not available
    try:
        import PyInstaller
    except ImportError:
        print("Installing PyInstaller...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "pyinstaller"])
    
    # Determine platform-specific options
    system = platform.system().lower()
    
    # Base PyInstaller command
    cmd = [
        "pyinstaller",
        "--onefile",  # Create single executable
        "--console",  # Console application (not GUI)
        "--name=py-terminal",  # Executable name
        "--add-data=info.md:.",  # Include info.md file
        "--hidden-import=rich.console",
        "--hidden-import=rich.panel", 
        "--hidden-import=rich.prompt",
        "--hidden-import=rich.markdown",
        "terminal_web/main.py"
    ]
    
    # Platform-specific optimizations
    if system == "windows":
        cmd.extend(["--windowed"])  # Hide console window on Windows
    elif system == "darwin":  # macOS
        cmd.extend(["--target-architecture=universal2"])  # Universal binary
    
    print(f"Building executable for {system}...")
    print(f"Command: {' '.join(cmd)}")
    
    try:
        subprocess.check_call(cmd)
        print("\n✅ Build completed successfully!")
        print(f"Executable location: dist/py-terminal{'.exe' if system == 'windows' else ''}")
    except subprocess.CalledProcessError as e:
        print(f"\n❌ Build failed with error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    build_executable() 