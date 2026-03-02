@echo off
REM Batch installer for Python3 + project dependencies.
REM Usage: double-click or run from cmd.

:: check for conda (Anaconda/Miniconda)
conda --version >nul 2>&1
IF %ERRORLEVEL% NEQ 0 (
    echo Anaconda/Miniconda is not installed. Attempting download and installation...
    set CONDA_INSTALLER=Anaconda3-latest-Windows-x86_64.exe
    powershell -Command "Invoke-WebRequest -Uri 'https://repo.anaconda.com/archive/Anaconda3-2025.12-2-Windows-x86_64.exe' -OutFile '%CONDA_INSTALLER%'"
    if exist %CONDA_INSTALLER% (
        echo Launching Anaconda installer...
        start /wait %CONDA_INSTALLER% /S /D=C:\ProgramData\Anaconda3
        del %CONDA_INSTALLER%
        echo Installing Jupyter Notebook via conda...
        call conda install -y notebook
    ) else (
        echo Failed to download Anaconda. Continuing without it.
    )
)

:: check for python3
python --version >nul 2>&1
IF %ERRORLEVEL% NEQ 0 (
    echo Python is not installed. Attempting download and installation...
    set INSTALLER=python-installer.exe
    powershell -Command "Invoke-WebRequest -Uri 'https://www.python.org/ftp/python/3.14.3/python-3.14.3-amd64.exe' -OutFile '%INSTALLER%'"
    if exist %INSTALLER% (
        echo Launching Python installer...
        start /wait %INSTALLER% /quiet InstallAllUsers=1 PrependPath=1
        del %INSTALLER%
    ) else (
        echo Failed to download Python. Please install manually.
        goto END
    )
)

:: now invoke python script to install packages
python install_dependencies.py

:END
pause