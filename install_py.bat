@echo off
REM Change version and URL as needed
set PYTHON_VERSION=3.12.0
set INSTALLER=python-%PYTHON_VERSION%-amd64.exe
set DOWNLOAD_URL=https://www.python.org/ftp/python/%PYTHON_VERSION%/%INSTALLER%

echo Downloading Python %PYTHON_VERSION% installer...
powershell -Command "Invoke-WebRequest -Uri '%DOWNLOAD_URL%' -OutFile '%INSTALLER%'"

echo Installing Python silently...
%INSTALLER% /quiet InstallAllUsers=1 PrependPath=1 Include_test=0

echo Python installation complete!
pause
