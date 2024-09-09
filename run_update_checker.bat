@echo off

cd /d %~dp0

FOR /F "tokens=1-4 delims=/.- " %%A IN ("%DATE%") DO (
    SET CurrentDate=%%A-%%B-%%C
)
FOR /F "tokens=1-2 delims=:." %%A IN ("%TIME%") DO (
    SET CurrentTime=%%A-%%B
)
REM Remove trailing spaces from CurrentTime if necessary
SET CurrentTime=%CurrentTime: =%

REM Combine date and time for a filename
SET DateTime=%CurrentDate%_%CurrentTime%

SET WorkingDir=%cd%
SET ScriptPath=%WorkingDir%\update_checker.py
SET PythonInterpreter=%WorkingDir%\venv\Scripts\python.exe

REM Ensure Logs directory exists
IF NOT EXIST "%WorkingDir%\Logs" (
    mkdir "%WorkingDir%\Logs"
)

@REM echo %WorkingDir% > C:\Users\%USERNAME%\Desktop\log-teste.log

%PythonInterpreter% %ScriptPath% > %WorkingDir%\Logs\output-updater-%DateTime%.log 2>&1