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

SET WorkingDir=%cd%
SET TriggerTime=14:00
SET TaskName=BlackBot_DailyUpdater
SET TaskBat=%WorkingDir%\run_update_checker.bat

REM Create scheduled task
schtasks /create /tn "%TaskName%" /tr "\"%TaskBat%\"" /sc daily /st %TriggerTime% /f /ru %USERNAME%
