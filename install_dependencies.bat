@echo off
setlocal

echo =====================================
echo INSTALLATION ENVIRONNEMENT PYTHON
echo =====================================

set ANACONDA_URL=https://repo.anaconda.com/archive/Anaconda3-2025.12-2-Windows-x86_64.exe
set PYTHON_URL=https://www.python.org/ftp/python/3.14.3/python-3.14.3-amd64.exe

set ANACONDA_INSTALLER=anaconda_installer.exe
set PYTHON_INSTALLER=python_installer.exe

echo.
echo Verification Python...

where python >nul 2>nul
if %errorlevel% neq 0 (
    echo Python non detecte. Telechargement...

    powershell -Command "Invoke-WebRequest -Uri '%PYTHON_URL%' -OutFile '%PYTHON_INSTALLER%'"

    echo Installation Python...

    start /wait %PYTHON_INSTALLER% /quiet InstallAllUsers=1 PrependPath=1 Include_test=0
) else (
    echo Python detecte.
)

echo.
echo Verification Anaconda...

where conda >nul 2>nul
if %errorlevel% neq 0 (
    echo Anaconda non detecte. Telechargement...

    powershell -Command "Invoke-WebRequest -Uri '%ANACONDA_URL%' -OutFile '%ANACONDA_INSTALLER%'"

    echo Installation Anaconda...

    start /wait %ANACONDA_INSTALLER% /S /InstallationType=JustMe /AddToPath=1 /RegisterPython=0
) else (
    echo Anaconda detecte.
)

echo.
echo Initialisation de conda...

call "%USERPROFILE%\Anaconda3\Scripts\activate.bat"

echo.
echo Verification Jupyter Notebook...

where jupyter >nul 2>nul
if %errorlevel% neq 0 (
    echo Installation de Jupyter Notebook via conda...

    conda install -y notebook
) else (
    echo Jupyter detecte.
)

echo.
echo Verification finale...

where python >nul 2>nul
if %errorlevel% neq 0 (
    echo ERREUR : Python non installe correctement.
    pause
    exit
)

where jupyter >nul 2>nul
if %errorlevel% neq 0 (
    echo ERREUR : Jupyter non installe correctement.
    pause
    exit
)

where conda >nul 2>nul
if %errorlevel% neq 0 (
    echo ERREUR : Anaconda non installe correctement.
    pause
    exit
)

echo.
echo =====================================
echo INSTALLATION DEPENDANCES PYTHON
echo =====================================

python install_dependencies.py

echo.
echo Installation terminee.
pause