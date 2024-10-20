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

@REM echo Defining the .env variables
@REM :: Define the variables
@REM set BASE_URL=
@REM set BQ_ID_REPOSITORY=
@REM set GIT_REPO=rdm10br/BB_Py_Automation
@REM set BRANCH=dev

@REM echo Creating .env file
@REM :: Create the .env file and write the variables to it
@REM echo BASE_URL=%BASE_URL% >> .env
@REM echo BQ_ID_REPOSITORY=%BQ_ID_REPOSITORY% >> .env
@REM echo GIT_REPO=%GIT_REPO% >> .env
@REM echo BRANCH=%BRANCH% >> .env

@REM echo .env file created successfully!

echo Setup schedule to updater.

SET WorkingDir=%cd%
SET TriggerTime=14:00
SET TaskName=BlackBot_DailyUpdater
SET TaskBat=%WorkingDir%\run_update_checker.vbs

REM Create scheduled task
schtasks /create /tn "%TaskName%" /tr "wscript.exe \"%TaskBat%\"" /sc daily /st %TriggerTime% /f /ru %USERNAME%