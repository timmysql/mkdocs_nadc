# from database import setup 
import database_load_files
import time
import os
from db_config import DbConfig

from sqlalchemy import create_engine
from sqlalchemy_utils import database_exists, create_database

CWD = os.getcwd()

engine = db_engine = DbConfig.get_central_engine()

def create_dir(path):
    isExist = os.path.exists(path)
    if not isExist:
        os.makedirs(path)

def create_dirs():
    create_dir(f"{CWD}\\csv_files")



def create_db():
    if not database_exists(engine.url):
        create_database(engine.url)

    print(database_exists(engine.url))

def main():
    create_db()
    database_load_files.main()
    time.sleep(2)
    database_load_files.main_post_load()    
    
    time.sleep(10)
    print('========================================')
    print('========================================')
    print('========================================')
    print('=======  DAILY PROCESS COMPLETE  =======')
    print('========================================')
    print('========================================')
    print('========================================')    


def main_test():

    database_load_files.main()
    time.sleep(2)    
    database_load_files.main_post_load()   
    time.sleep(10)
    print('========================================')
    print('========================================')
    print('================ TEST =================')
    print('=======  DAILY PROCESS COMPLETE  =======')
    print('================ TEST =================')
    print('========================================')
    print('========================================')   


if __name__ == "__main__":
    # print(CWD)
    create_dirs()
    main()