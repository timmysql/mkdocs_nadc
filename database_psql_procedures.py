# import sql_generic as sql
# import psql_generic as psql
import database_psql_generic as psql
# import psql_generic as psql
    
################################################################
# ETL
################################################################

def load_tweet_contributions():
    tsql = f"""call sp_load_tweet_contributions();"""
    psql.execute_sql(tsql)


# DROP STAGE TABLES  
def drop_stage_contributions():
    tsql = f"""drop table stage_contributions"""
    psql.execute_sql(tsql)  

def drop_stage_expenditures():
    tsql = f"""drop table stage_expenditures"""
    psql.execute_sql(tsql)  

    
def truncate_generic_table(table_name):
    # table_name = 'stage_contributions'
    tsql = f"""DO $$
            BEGIN
            if (SELECT to_regclass('public.{table_name}')) != NULL THEN 
                truncate table {table_name};
            end if;
            END $$"""
    print(tsql)
    psql.execute_sql(tsql)      
    
# TRUNCATE STAGE TABLES  
def truncate_stage_contributions():
    table_name = 'stage_contributions'
    tsql = f"""DO $$
BEGIN
if (SELECT to_regclass('public.{table_name}')) != NULL THEN 
    truncate table {table_name};
end if;
END $$"""
    psql.execute_sql(tsql)  

def truncate_stage_expenditures():
    table_name = 'stage_expenditures'
    tsql = f"""DO $$
BEGIN
if (SELECT to_regclass('public.{table_name}')) != NULL THEN 
    truncate table {table_name};
end if;
END $$"""
    psql.execute_sql(tsql)   
    
def truncate_ppp_data():
    table_name = 'ppp_data'
    tsql = f"""DO $$
            BEGIN
            if (SELECT to_regclass('public.{table_name}')) != NULL THEN 
                truncate table {table_name};
            end if;
            END $$"""
    print(tsql)
    psql.execute_sql(tsql)        
    


# LOAD TABLES FROM STAGE
def load_contributions():
    tsql = f"""call sp_load_contribution();"""
    psql.execute_sql(tsql)
    
def load_expenditures():
    tsql = f"""call sp_load_expenditure();"""
    psql.execute_sql(tsql)   
    
def load_filers():
    tsql = f"""call sp_load_filer();"""
    psql.execute_sql(tsql)
    
def load_payees():
    tsql = f"""call sp_load_payee();"""
    psql.execute_sql(tsql)
    
def load_payors():
    tsql = f"""call sp_load_payor();"""
    psql.execute_sql(tsql)        
    
    
def update_contribution():
    tsql = f"""call sp_update_contribution();"""
    psql.execute_sql(tsql)
    
def update_expenditure():
    tsql = f"""call sp_update_expenditure();"""
    psql.execute_sql(tsql)
    
def update_filer_type_short():     
    tsql = f"""call sp_update_filer_type_short();"""
    psql.execute_sql(tsql)
    
        
        
        
        
def main():
    load_filers()      

if __name__ == '__main__':
    main()
    # drop_stage_contributions()
    # drop_stage_expenditures()
    
    
    # update_contribution()
    # update_expenditure()    
    # update_filer_type_short()
    