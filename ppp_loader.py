import os
import pandas as pd
import sys
import db_config as dbc
# from database import psql_procedures as prc


CWD =  os.getcwd() 
PPP_DIR = '\\ppp\\'
# DATABASE_DIR = '\\database'
ENCODING = 'windows-1250' 

  

PPP_PATH = CWD + PPP_DIR
# DATABASE_PATH = CWD + DATABASE_DIR
# sys.path.insert(0, DATABASE_PATH)


# os.listdir(PPP_PATH)


def load_to_ppp_data(file_name):
    full_path = PPP_PATH + file_name

    # df = pd.read_csv(full_path, sep=',', engine='python', quoting=1, encoding='ascii')
    # df = pd.read_csv(full_path, sep=',', engine='python', quoting=1, encoding='utf-8', on_bad_lines='error')
    # df = pd.read_csv(full_path, sep=',', engine='python', quoting=1, encoding='ascii', on_bad_lines='error')
    df = pd.read_csv(full_path, sep=',', engine='c', quoting=1, encoding=ENCODING, on_bad_lines='error')
        
    df = df.rename(columns=str.lower)
    # df.columns = df.columns.str.replace(' - ','_', regex=True)    
    # df.columns = df.columns.str.replace(' ','_', regex=True)
    # df.columns = df.columns.str.replace('/','_', regex=True)
    # df.columns = df.columns.str.replace(')','', regex=True)
    # df.columns = df.columns.str.replace('(','', regex=True)
    # df.columns = df.columns.str.replace('-','_', regex=True)
    
    db_engine =  dbc.DbConfig.get_central_engine()
    print('db_engine: ', db_engine)
    with db_engine.connect() as connection:
    
        try:
            df.to_sql('ppp_data', con=db_engine, if_exists='append')
        except Exception as e:
            raise   
  
def chunk_file_to_db(file_name):
    full_path = PPP_PATH + file_name
    db_engine =  dbc.DbConfig.get_central_engine()  
    chunk_size=500000
    batch_no=1
    # for chunk in pd.read_csv('yellow_tripdata_2016-02.csv',chunksize=chunk_size,iterator=True):
    for chunk in pd.read_csv(full_path, sep=',', engine='c', quoting=1, encoding=ENCODING, on_bad_lines='error',chunksize=chunk_size,iterator=True):
        
        
        with db_engine.connect() as connection:
        
            try:
                chunk.to_sql('ppp_data', con=db_engine, if_exists='append')
                # df.to_sql('ppp_data', con=db_engine, if_exists='append')
                input('stop')
            except Exception as e:
                raise      
        batch_no+=1
        print('index: {}'.format(batch_no))   
   
   
def main():
    # prc.truncate_ppp_data()      
    for x in os.listdir(PPP_PATH):
        if x.endswith(".csv"):
            # Prints only text file present in My Folder
            print(x)
            load_to_ppp_data(x)
            # print(x)
            # if x >= 'public_up_to_150k_6_220403.csv':
            #     print(x)
            #     load_to_ppp_data(x)
            # if x not in ['public_150k_plus_220403.csv','public_up_to_150k_10_220403.csv']:
            #     load_to_ppp_data(x)
            #     print(x)
            # input('stop')

# print(CWD)  

if __name__ == '__main__':
    main()      
    
# public_up_to_150k_11_220403.csv
# public_up_to_150k_12_220403.csv
# public_up_to_150k_1_220403.csv
# public_up_to_150k_2_220403.csv
# public_up_to_150k_3_220403.csv
# public_up_to_150k_4_220403.csv
# public_up_to_150k_5_220403.csv
