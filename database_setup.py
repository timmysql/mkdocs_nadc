from db_config import DbConfig
import database_psql_generic as sql 
import db_models as mdl
from sqlalchemy import create_engine
from sqlalchemy_utils import database_exists, create_database
import os

engine = db_engine = DbConfig.get_central_engine()

def create_db():
    if not database_exists(engine.url):
        create_database(engine.url)
    print(database_exists(engine.url))


# def drop_db():
#     sql.execute_sql("DROP DATABASE")    
#     # drop_database()


def create_model_tables():
    mdl.main()
  
def read_sql_file(file_name):
    with open(f'{file_name}') as file:
        df = file.read()
        print(df)
    return df     
  
def create_sql_objects(dir):
    cwd = os.getcwd()
    base_path = cwd + f"\\"
    path = base_path + f"{dir}\\"
    # print(path)
    dir_list = os.listdir(path)
    # return dir_list  
    for file in dir_list:
        sql_file = path + file
        print('doing ' + sql_file)
        df = read_sql_file(sql_file)
        sql.execute_sql(df)
        # print(path + file)
        
    # print(dir_list)
       
def main():
    create_db() 
    create_model_tables() 
    create_sql_objects('sql_tables') 
    create_sql_objects('sql_views')
    create_sql_objects('sql_procedures')     

if __name__ == "__main__":
    main()   

    # for file in dir_list:
    #     print(file)
    # cwd = os.getcwd()
    # print(cwd)