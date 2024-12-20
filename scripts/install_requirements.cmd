@echo off
REM Define path variables relative to the script

REM %%    : indication of loop variable
REM %~dp0 : getting file name (0) with path (p) and disk drive (d) without quotes (~), % used for character escaping for ~
REM ..    : parent directory
REM %%~fi : f convert .. from characters to actual command to go up from directory, all this gives path without last folder in path
for %%i in ("%~dp0..") do set "PROJECT_ROOT=%%~fi"
set "VENV_NAME=.venv"
set "VENV_PATH=%PROJECT_ROOT%\%VENV_NAME%"
set "VENV_ACTIVATE_PATH=%VENV_PATH%\Scripts\activate.bat"
set "REQUIREMENTS_PATH=%PROJECT_ROOT%\requirements"
set "REQUIREMENTS_FILE=%REQUIREMENTS_PATH%\requirements.txt"
set "BACKEND_PATH=%PROJECT_ROOT%\backend"

REM -q: Give less output.
REM Option is additive, and can be used up to 3 times (corresponding to WARNING, ERROR, and CRITICAL logging levels).
REM Optional parameter.
if "%1" == "-q" (
    set "QUIET_PIP=-q"
    echo Set pip silent mode to WARNINGS.
) else if "%1" == "-qq" (
    set "QUIET_PIP=-qq"
    echo Set pip silent mode to ERRORS.
) else if "%1" == "-qqq" (
    set "QUIET_PIP=-qqq"
    echo Set pip silent mode to CRITICAL.
) else (
    set "QUIET_PIP="
    echo Set pip silent mode to default.
)

REM Create venv if not exists
echo Create virtual environment %VENV_NAME%...
if not exist %VENV_PATH% (
    python -m venv %VENV_PATH%
    echo Virtual environment %VENV_NAME% successfully created.
) else (
    echo Virtual environment %VENV_NAME% already exists.
)

REM Activate venv
echo Activating virtual environment %VENV_NAME%...
call %VENV_ACTIVATE_PATH%
if errorlevel 1 (
    echo Virtual environment is not activated due to some errors.
    pause
    exit /b 1
) else (
    echo Virtual environment successfully activated.
)

REM Install and update pip
python.exe -m pip install --upgrade pip %QUIET_PIP%
if errorlevel 1 (
    echo Failed to install and update pip.
    pause
    exit /b 1
) else (
    echo Pip installed and updated successfully.
)

REM Install other necessary packages
pip install pip-tools pipreqs %QUIET_PIP%
if errorlevel 1 (
    echo Failed to install pip-tools or pipreqs.
    pause
    exit /b 1
) else (
    echo Pip-tools and pipreqs installed successfully.
)

REM Check requirements directory for existence
if not exist "%REQUIREMENTS_PATH%" (
    echo Requirements directory is not exists. Creating directory...
    mkdir "%REQUIREMENTS_PATH%"
    if errorlevel 1 (
        echo Failed to create requirements directory.
        pause
        exit /b 1
    ) else (
        echo Directory created successfully on path:
        echo %REQUIREMENTS_PATH%
    )
)

REM Generate requirements.txt
echo Generating requirements.txt...
echo Running pipreqs on %BACKEND_DIR% and saving to %REQUIREMENTS_FILE%
pipreqs --force --encoding=utf-8 --savepath %REQUIREMENTS_FILE% %BACKEND_PATH%

REM Check, if requirements.txt generated successfully
if exist %REQUIREMENTS_FILE% (
    echo File requirements.txt created successfully.
) else (
    echo Failed to create file requirements.txt.
    pause
    exit /b 1
)

REM Install dependencies
echo Installing dependencies...
pip install -r "%REQUIREMENTS_FILE%" %QUIET_PIP%
if errorlevel 1 (
    echo Failed to install dependencies.
    pause
    exit /b 1
)
echo Dependencies installed successfully.

pause