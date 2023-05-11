# NADC 

## Built With
- [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/)
- [PostgreSQL](https://www.postgresql.org/)
- [SQLModel](https://sqlmodel.tiangolo.com/)

## Database Setup

1. Install PostgreSQL
2. Clone Repo
3. Create Virtual Environment w/ venv venv
4. Activate virtual environment
5. install requirements.txt   
6. Run \database\database_setup.py
7. Run database_daily_process.py (Downloads files and loads them to database)
8. markdown_refresh_main.py
9. mkdocs serve (to run site locally)

## Install Postgres...
1. Make sure you have Postgres Installed somewhere.
   - This thing uses stored procedures, so make sure your version of Postgres supports those.

#### Install VirtualEnv
1. `python -m pip install --upgrade pip`
2. `python -m pip install virtualenv`

#### Create VirtualEnv
1. Ensure you are in your project directory
2. `python -m virtualenv venv`

#### Activate VirtualEnv
1. `venv\Scripts\Activate`


#### Install requirements.txt
1.  `pip install -r requirements.txt`

#### Configure db_config.ini
2. Configure db_config.ini
    ```
    [localhost_section]
    host = localhost:5432       <--- DNS:Port or IP:Port
    database = nadc_sqlmodel    <--- NAME of the database it will create
    user = osint                <--- user that has rights to create the db
    password = osint            <--- pw for the user

    ```

#### Run database_setup.py to create database and database objects
Requires PostgreSQL to be installed and db_config.ini configured
1. `python.exe database_setup.py`



#### Daily Reload Order of Operations 

1. Download NADC files and load the Database
    - `python.exe database_daily_process.py`
2. Build Markdown for MkDocs Site
   - `python.exe markdown_refresh_main.py`
3. Build and Serve MkDocs site 
   - `cd nadc`
   - `mkdocs serve`



  
