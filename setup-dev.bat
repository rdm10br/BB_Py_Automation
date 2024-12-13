@echo on

:: Create virtual environment
python -m venv venv

:: Activate virtual environment
call venv\Scripts\activate

:: Install dependencies
@REM pip install --upgrade pip
python -m pip install --upgrade pip
pip install -r requirements.txt
python -m playwright install
python -m spacy download pt_core_news_sm

echo Setup complete. Activate the virtual environment with 'venv\Scripts\activate'.

echo Defining the .env variables
:: Define the variables
set BASE_URL=
set BQ_ID_REPOSITORY=
set GIT_REPO=rdm10br/BB_Py_Automation
set BRANCH=dev

echo Creating .env file
:: Create the .env file and write the variables to it
echo BASE_URL=%BASE_URL% >> .env
echo BQ_ID_REPOSITORY=%BQ_ID_REPOSITORY% >> .env
echo GIT_REPO=%GIT_REPO% >> .env
echo BRANCH=%BRANCH% >> .env

echo .env file created successfully!