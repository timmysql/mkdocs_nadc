# from database.db_config import get_central_engine


from db_config import DbConfig
import sqlalchemy
# from db_config import DbConfig
# import psycopg2 
import pandas as pd



def return_df(sql):  
    db_engine = DbConfig.get_central_engine()
    # db_engine = dbc.get_central_engine()
    # user = auth.api.get_user(lookup_name)
    """ Connect to the PostgreSQL database server """
    conn = None
    conn = db_engine.connect()
    # cursor = conn.cursor()
    try:
        df = pd.read_sql(sql, conn)
    except Exception as e:
        raise
    df = df.rename(columns=str.lower)
    df.columns = df.columns.str.replace(' ','_')    
    # cursor.close()
    conn.close()
        
    return df

def execute_sql(sql):  
    sql = sqlalchemy.text(sql)
    db_engine = DbConfig.get_central_engine()
    # db_engine = dbc.get_central_engine()  
    # user = auth.api.get_user(lookup_name)
    """ Connect to the PostgreSQL database server """
    conn = None
    conn = db_engine.connect()
    conn.autocommit = True
    try:
        conn.execute(sql)
    except Exception as e:
        raise        
    conn.close()   

      
if __name__ == '__main__':  
    execute_sql('select * from contribution limit 100;')
    print("test")
    # dataset = pg_return_df('select * from public.facilities_am_stage')  
    # print(dataset)  