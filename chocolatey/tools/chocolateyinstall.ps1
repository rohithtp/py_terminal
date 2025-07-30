$ErrorActionPreference = 'Stop'

$packageName = 'py-terminal'
$toolsDir = "$(Split-Path -parent $MyInvocation.MyCommand.Definition)"

# Install Python if not present
$pythonPath = Get-Command python -ErrorAction SilentlyContinue
if (-not $pythonPath) {
    Write-Host "Python not found. Installing Python..."
    choco install python -y
}

# Install the package using pip
Write-Host "Installing py-terminal using pip..."
& python -m pip install py-terminal

# Create a batch file for easy execution
$batchContent = @"
@echo off
python -m terminal_web.main %*
"@

$batchPath = Join-Path $toolsDir "py-terminal.bat"
$batchContent | Out-File -FilePath $batchPath -Encoding ASCII

# Add to PATH
$installPath = Split-Path -Parent $batchPath
$currentPath = [Environment]::GetEnvironmentVariable("PATH", "Machine")
if ($currentPath -notlike "*$installPath*") {
    [Environment]::SetEnvironmentVariable("PATH", "$currentPath;$installPath", "Machine")
}

Write-Host "Py Terminal has been installed successfully!"
Write-Host "You can now run 'py-terminal' from anywhere in your terminal." 