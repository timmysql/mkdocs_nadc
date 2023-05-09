import os
import urllib.request
import shutil
# import fileinput
import pandas as pd

from db_config import DbConfig
import database_psql_procedures as prc
import database_psql_generic as psql
import csv
# import datetime
from rich import inspect



class ProcessSingleFile:
    encoding_ = 'windows-1250'    
    def __init__(self, file_type, year):
        self.file_type = file_type
        self.year = year     
        self.base_url = 'https://nadc-e.nebraska.gov/PublicSite/Docs/BulkDataDownloads/' 
        self.base_pdf_url = 'https://nadc-e.nebraska.gov/PublicSite/Resources/PublicDocuments/'        
        self.csv_dir = 'csv_files'
        self.pdf_dir = 'pdf_dir'
        self.root_dir = os.getcwd() 
        if file_type == 'contributions':
            self.stage_table = 'stage_contributions'
        if file_type == 'expenditures':
            self.stage_table = 'stage_expenditures'
       
        if os.name == 'nt':
            self.csv_path = self.root_dir + '\\' + self.csv_dir + '\\'
            self.pdf_path = self.root_dir + '\\' + self.pdf_dir + '\\'
        else:
            self.csv_path = self.root_dir + '/' + self.csv_dir + '/'
            self.pdf_path = self.root_dir + '/' + self.pdf_dir + '/'            
        
    def zip_file_name_builder(self):
        file_name = ''
        if self.file_type == 'expenditures':
            print('exp: ' + str(self.year))
            file_name = str(self.year) + '_ExpenditureExtract.csv.zip'
        elif self.file_type == 'contributions':
            print('cont: ' + str(self.year))
            file_name = str(self.year) + '_ContributionLoanExtract.csv.zip' 
        else:
            print('file_type: ', self.file_type)
            print('YO... not sure what file type you just tried to use')           
        print(file_name)
        return file_name      
            
        
    def get_file(self):        
        zip_file_name = self.zip_file_name_builder()
        get_file_url = self.base_url + zip_file_name
        download_file_path = self.csv_path + zip_file_name        
        # csv_file_name = self.csv_file_name_builder(file_type=file_type, year=year)
        print('zip:', zip_file_name)
        # print('csv:', csv_file_name)
        try:
            urllib.request.urlretrieve(get_file_url, download_file_path)
        except Exception as e:
            raise
        # self.get_file_and_unpack(file_name=zip_file_name)
        return zip_file_name 
    
    
    def unpack_file(self, file_name):   
        download_file_path = self.csv_path + file_name   
        shutil.unpack_archive(download_file_path, self.csv_path, 'zip')
        csv_file_name = file_name.replace('.zip','')
        return csv_file_name    
    
    def csv_string_fixer(self, csv_file_name):
        strout_file_name = csv_file_name.replace('.csv','_StrOut.csv')
        full_file_path = self.csv_path + csv_file_name
        full_outfile_path =self.csv_path + strout_file_name
        # full_file_path = """C:\\Users\\timko\\code\\nadc_bravo\csv_files\\2022_ExpenditureExtract.csv"""
        # full_outfile_path = """C:\\Users\\timko\\code\\nadc_bravo\csv_files\\2022_ExpenditureExtract_Out.csv"""
        full_outfile_path = full_file_path.replace('.csv','_StrOut.csv')
        print(full_outfile_path)
        
        with open(full_file_path, 'r', encoding=self.encoding_) as strIN:
            with open(full_outfile_path, "wt") as strOUT:
                for line in strIN:
                    line = line.replace('"O"','O')
                    strOUT.write(line)
        return strout_file_name   
              
    def csv_crlf_fixer(self, strout_file_name):
        crlf_file_name = strout_file_name.replace('.csv','_CrlfOut.csv')
        full_file_path = self.csv_path + strout_file_name
        full_outfile_path = self.csv_path + crlf_file_name
        # full_file_path = """C:\\Users\\timko\\code\\nadc_bravo\csv_files\\2022_ExpenditureExtract.csv"""
        # full_outfile_path = """C:\\Users\\timko\\code\\nadc_bravo\csv_files\\2022_ExpenditureExtract_Out.csv"""
        # full_outfile_path = full_file_path.replace('.csv','_Out.csv')
        print(full_outfile_path)
        
        with open(full_file_path, 'r', encoding=self.encoding_) as csvIN:
            # file_reader = csv.reader(csvIN, delimiter=',', quoting=csv.QUOTE_ALL)
            file_reader = csv.DictReader(csvIN, delimiter=',', quoting=csv.QUOTE_ALL)
            fieldnames = file_reader.fieldnames
            # print(fieldnames)
            # print(file_reader)
            with open(full_outfile_path, 'w', newline='', encoding=self.encoding_) as csvOUT:
                file_writer = csv.DictWriter(csvOUT, fieldnames=fieldnames, quoting=csv.QUOTE_ALL)
                file_writer.writeheader()
                for row in file_reader:
                    # print(row)
                    row.update({"Description":row['Description'].replace("\n", "")})
                    # row.update({"Description":row['Address 1'].replace('\"O\"', "")})
                    file_writer.writerow(row)
        return crlf_file_name        
              
    def truncate_table(self):
        table_name = self.stage_table
        # sql_ = f"""truncate table {self.stage_table};"""
        sql_ = f"""DO $$
BEGIN
if (SELECT to_regclass('public.{table_name}')) != NULL THEN 
    truncate table {table_name};
end if;
END $$"""        
        
        psql.execute_sql(sql=sql_)

    def load_table(self):
        if self.stage_table == 'stage_contributions':        
            prc.load_contributions()
        if self.stage_table == 'stage_expenditures':        
            prc.load_expenditures()           
                
    def load_to_stage(self, file_name):
        full_path = self.csv_path + file_name
        print("file_path: " + self.csv_path)
        print("table_name: " + self.stage_table)
        # df = pd.read_csv(full_path, sep=',', engine='python', quoting=1, encoding='ascii')
        # df = pd.read_csv(full_path, sep=',', engine='python', quoting=1, encoding='utf-8', on_bad_lines='error')
        # df = pd.read_csv(full_path, sep=',', engine='python', quoting=1, encoding='ascii', on_bad_lines='error')
        df = pd.read_csv(full_path, sep=',', engine='python', quoting=1, encoding=self.encoding_, on_bad_lines='error')
            
        df = df.rename(columns=str.lower)
        df.columns = df.columns.str.replace(' - ','_', regex=True)    
        df.columns = df.columns.str.replace(' ','_', regex=True)
        df.columns = df.columns.str.replace('/','_', regex=True)
        # df.columns = df.columns.str.replace(")","", regex=True)
        # df.columns = df.columns.str.replace('(','', regex=True)
        df.columns = df.columns.str.replace('-','_', regex=True)
        
        db_engine =  DbConfig.get_central_engine()
        print('db_engine: ', db_engine)
        with db_engine.connect() as connection:
        
            try:
                df.to_sql(self.stage_table, con=db_engine, if_exists='append')
            except Exception as e:
                raise                
                
                
   
        
def main_single(file_type_, year_):
    psf = ProcessSingleFile(file_type=file_type_, year=year_)
    zip_file_name = psf.get_file()
    csv_file_name = psf.unpack_file(file_name=zip_file_name)
    strout_file_name = psf.csv_string_fixer(csv_file_name=csv_file_name)
    crlf_file_name = psf.csv_crlf_fixer(strout_file_name=strout_file_name)
    
    psf.truncate_table()    
    
    psf.load_to_stage(file_name=crlf_file_name)
    # print(psf.stage_table)
    psf.load_table()
    psf.truncate_table()     


def main_files():
    file_type_ = 'expenditures'
    
    year_ = 2021    
    main_single(file_type_=file_type_, year_=year_)
    
    year_ = 2022
    main_single(file_type_=file_type_, year_=year_)
    
    year_ = 2023
    main_single(file_type_=file_type_, year_=year_)    
    
    
    file_type_ = 'contributions'
    
    year_ = 2021    
    main_single(file_type_=file_type_, year_=year_)
    
    year_ = 2022
    main_single(file_type_=file_type_, year_=year_)   
    
    year_ = 2023
    main_single(file_type_=file_type_, year_=year_)       
    

def main_post_load():
    print('main_post_load')
    print('update_contribution')
    prc.update_contribution()
    prc.update_expenditure()    
    prc.update_filer_type_short()
    prc.load_filers()      
    prc.load_payees()
    prc.load_payors()
    print('end_main_post_load')
            
def main_all():
    main_files()
    main_post_load()
    
def main():
    main_files()
    
def download_extract_only(file_type_, year_):
    psf = ProcessSingleFile(file_type=file_type_, year=year_)
    zip_file_name = psf.get_file()
    csv_file_name = psf.unpack_file(file_name=zip_file_name)
    # strout_file_name = psf.csv_string_fixer(csv_file_name=csv_file_name)
    # crlf_file_name = psf.csv_crlf_fixer(strout_file_name=strout_file_name)    
     
def main_files_download_extract():
    file_type_ = 'expenditures'
    
    year_ = 2021    
    download_extract_only(file_type_=file_type_, year_=year_)
    
    year_ = 2022
    download_extract_only(file_type_=file_type_, year_=year_)
    
    
    file_type_ = 'contributions'
    
    year_ = 2021    
    download_extract_only(file_type_=file_type_, year_=year_)
    
    year_ = 2022
    download_extract_only(file_type_=file_type_, year_=year_)          
    
if __name__ == '__main__':
    main()
    # main_files_download_extract()





