@echo on
echo --- SETUP STARTED --- > setup_debug.log

:: Create virtual environment
python -m venv venv >> setup_debug.log 2>&1

:: Activate virtual environment
call venv\Scripts\activate

:: Install dependencies
pip install --upgrade pip
pip install -r requirements.txt
python -m playwright install
python -m spacy download pt_core_news_sm

echo Setup complete. Activate the virtual environment with 'venv\Scripts\activate'.
echo Setup complete. >> setup_debug.log
echo Setup schedule to updater.

SET WorkingDir=%cd%
SET TriggerTime=14:00
SET TaskName=BlackBot_DailyUpdater
SET TaskBat=%WorkingDir%\run_update_checker.vbs

REM Create scheduled task
schtasks /create /tn "%TaskName%" /tr "wscript.exe \"%TaskBat%\"" /sc daily /st %TriggerTime% /f /ru %USERNAME%

echo --- SETUP FINISHED --- >> setup_debug.log