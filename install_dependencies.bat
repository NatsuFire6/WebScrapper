@echo off
REM Batch installer for Python3 + project dependencies.
REM Usage: double-click or run from cmd (NOT PowerShell).
REM Requires network access and administrator privileges; works on Windows 7/8/10/11.

:: ensure we are running under cmd.exe by inspecting COMSPEC
for %%I in ("%COMSPEC%") do set _cs=%%~nxI
if /I "%_cs%" NEQ "cmd.exe" (
    echo This script must be run from a Command Prompt (cmd.exe).
    echo Please open a cmd window and execute %~nx0 there.
    pause
    exit /b
)


:: check for conda (Anaconda/Miniconda)
conda --version >nul 2>&1
IF %ERRORLEVEL% NEQ 0 (
    echo Anaconda/Miniconda is not installed. Attempting download and installation...
    set CONDA_INSTALLER=Anaconda3-latest-Windows-x86_64.exe
    powershell -Command "Invoke-WebRequest -Uri 'https://repo.anaconda.com/archive/Anaconda3-2025.12-2-Windows-x86_64.exe' -OutFile '%CONDA_INSTALLER%' -UseBasicParsing"
    if exist %CONDA_INSTALLER% (
        echo Launching Anaconda installer...
        start /wait %CONDA_INSTALLER% /S /D=C:\ProgramData\Anaconda3
        if %ERRORLEVEL% NEQ 0 echo Anaconda installer returned error %ERRORLEVEL%
        del %CONDA_INSTALLER%
        echo Installing Jupyter Notebook via conda...
        call conda install -y notebook
    ) else (
        echo Failed to download Anaconda (file not found). Check your network.
    )
)

:: check for python3
python --version >nul 2>&1
IF %ERRORLEVEL% NEQ 0 (
    echo Python is not installed. Attempting download and installation...
    set INSTALLER=python-installer.exe
    powershell -Command "Invoke-WebRequest -Uri 'https://www.python.org/ftp/python/3.14.3/python-3.14.3-amd64.exe' -OutFile '%INSTALLER%' -UseBasicParsing"
    if exist %INSTALLER% (
        echo Launching Python installer...
        start /wait %INSTALLER% /quiet InstallAllUsers=1 PrependPath=1
        if %ERRORLEVEL% NEQ 0 echo Python installer returned error %ERRORLEVEL%
        del %INSTALLER%
    ) else (
        echo Failed to download Python (file not found). Please install manually.
        goto END
    )
)

:: now invoke python script to install packages
python install_dependencies.py

:END
pause