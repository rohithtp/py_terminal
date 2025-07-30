from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="py-terminal",
    version="1.0.0",
    author="Your Name",
    author_email="your.email@example.com",
    description="A powerful terminal-based UI web project using Python and Rich for beautiful terminal output",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/py_terminal",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Intended Audience :: System Administrators",
        "License :: Public Domain",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Topic :: System :: Systems Administration",
        "Topic :: Terminals",
        "Topic :: Utilities",
    ],
    python_requires=">=3.7",
    install_requires=[
        "rich>=10.0.0",
    ],
    entry_points={
        "console_scripts": [
            "py-terminal=terminal_web.main:main",
        ],
    },
    keywords="terminal, ui, rich, command-execution, system-administration",
    project_urls={
        "Bug Reports": "https://github.com/yourusername/py_terminal/issues",
        "Source": "https://github.com/yourusername/py_terminal",
        "Documentation": "https://github.com/yourusername/py_terminal#readme",
    },
) 