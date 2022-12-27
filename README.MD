## Database Setup

1. Install PostgreSQL
2. Clone Repo
3. Create Virtual Environment w/ venv venv
4. Activate virtual environment
5. install requirements.txt   
6. Run \database\database_setup.py

#### Install VirtualEnv
1. python -m pip install --upgrade pip
2. python -m pip install virtualenv

#### Create VirtualEnv
1. Ensure you are in your project directory
2. virtualenv venv

#### Activate VirtualEnv
1. venv\Scripts\Activate
2. python -m venv\Scripts\Activate ???

#### Create requirements.txt
1. pip freeze > requirements.txt

#### Install requirements.txt
1.  pip install requirements.txt


## Configure database stuff...
1. Make sure you have Postgres Installed somewhere.
   - This thing uses stored procedures, so make sure your version of Postgres supports those.
  
2. Configure db_config.ini
    ```
    [localhost_section]
    host = localhost            <--- DNS or IP Address also would work.
    database = nadc_sqlmodel    <--- NAME of the database it will create
    user = osint                <--- user that has rights to create the db
    password = osint            <--- pw for the user

    ```

3. Configure database/DbConfig.py
    ```
    class DbConfig:
        def __init__(self):
            self.current_dir = os.getcwd()
            self.config_ini = 'db_config.ini'     <--- THE NAME OF YOUR CONFIG INI FILE
            self.section = 'localhost_section'    <--- THE SECTION IN YOUR db_config.ini you want to point to (e.g. [localhost_section]).
    ```        

4. Let's load this thing.
   Option 1
    - run setup.py
    - run daily_process.py
   Option 2
    - run rebuild_everything.py
