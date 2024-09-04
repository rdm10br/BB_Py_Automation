@echo on

:: Create virtual environment
python -m venv venv

:: Activate virtual environment
call venv\Scripts\activate

:: Install dependencies
pip install --upgrade pip
pip install -r requirements.txt
python -m playwright install
python -m spacy download pt_core_news_sm

echo Setup complete. Activate the virtual environment with 'venv\Scripts\activate'.

echo Setup schedule to updater.

SET TaskName=BBPyAuto_DailyUpdater
SET ScriptPath=update_checker.py
SET WorkingDir=%cd%
SET TriggerTime=14:00

@REM schtasks /create /tn "%TaskName%" /tr "%WorkingDir%\%ScriptPath%" /sc daily /st %TriggerTime% /f /ru %username%
