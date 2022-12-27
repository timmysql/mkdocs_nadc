from db_dal_classes import SelectExpenditures, SelectContributions
import os
import shutil
from rich import inspect
import markdown_refresh_directories as dirs
# from refresh_filers import EXP_YAML_DIR

CWD = os.getcwd()
SITE_DIR = dirs.SITE_DIR
BUILDER_OUTPUT_LEADERBOARDS_EXP = f'{SITE_DIR}\\docs\\expenditures'
BUILDER_OUTPUT_LEADERBOARDS_RCP = f'{SITE_DIR}\\docs\\receipts'
RCP_YAML_DIR = dirs.RCP_YAML_DIR
EXP_YAML_DIR = dirs.EXP_YAML_DIR


class BuildExpendituresTables:
    def __init__(self):
        pass
      
    def build_new_header(self) -> str:            
        header = ""                 
        header += f"| Rank | Filer | Candidate | Payee | Amount | Date | Type | Description |\n"
        header += f"| ---- | ----- | --------- | ----- | ------ | ---- | ---- | ----------- |\n"            
        
        return header
    
    
    def build_new_table(self, row, index) -> str:
        formatted_amt = "${:,.2f}".format(row.expenditure_amount)         
        table = ''                 
        table += f"| {index} | "
        table += f"""[{row.filer_name}](/{EXP_YAML_DIR}{row.filer_markdown_file}) | """ 
        table += f"{row.candidate_name} | "
        table += f"""[{row.payee_name}](/expenditures/payees/{row.payee_folder}/#{row.payee_markdown_file}) | """
        table += f"{formatted_amt} | {row.expenditure_date} | "
        table += f"{row.expenditure_type} | {row.description}\n"      
        return table                   
    

                
    def md_header_top_100(self) -> str:
        file_header = '# Expenditures: Top 500\n\n'
        return file_header
    
    def md_header_last_100(self) -> str:
        file_header = '# Expenditures: Last 1500\n\n'
        return file_header    
    
    def top_100(self) -> str:
        i = 1 
        big_table = ''
        x = SelectExpenditures()
        y = x.top_500()
        
        for row in y:
            # inspect(row, all=True)
            # input('testes')
            single_table = self.build_new_table(row = row, index=i)
            big_table += single_table
            i += 1
        return big_table
    
    def last_100(self) -> str:
        i = 1 
        big_table = ''
        x = SelectExpenditures()
        y = x.last_1500()
        
        for row in y:
            # inspect(row, all=True)
            # input('testes')
            single_table = self.build_new_table(row = row, index=i)
            big_table += single_table
            i += 1
        return big_table    
    
    def build_file_content_top_100(self):
        md_header = self.md_header_top_100()
        table_header = self.build_new_header()
        big_table = self.top_100()
        file_content = ''        
        file_content += md_header
        file_content += table_header
        file_content += big_table  
        return file_content 
    
    
    def build_file_content_last_100(self):
        md_header = self.md_header_last_100()
        table_header = self.build_new_header()
        big_table = self.last_100()
        file_content = ''        
        file_content += md_header
        file_content += table_header
        file_content += big_table  
        return file_content      
         
    
    def write_file(self) -> None:
        # top 500 
        file_content = self.build_file_content_top_100()
        with open(f'{SITE_DIR}\\docs\\expenditures\\expenditures_top_500.md', 'w', encoding='utf-8') as outputfile:
            outputfile.write(file_content)
        # last 1500    
        file_content = self.build_file_content_last_100()
        with open(f'{SITE_DIR}\\docs\\expenditures\\expenditures_last_1500.md', 'w', encoding='utf-8') as outputfile:
            outputfile.write(file_content)            
    
    
class BuildReceiptsTables:
    def __init__(self):
        pass
        # self.receipts = receipts
    def build_new_header(self) -> str:            
        header = ''                 
        header += """| Rank | Filer | Candidate | Payor | Amount | Date | Type |\n"""
        header += """| ---- | ----- | --------- | ----- | ------ | ---- | ---- |\n"""
        return header
    
    def build_new_table(self, row, index) -> str:
        formatted_amt = "${:,.2f}".format(row.receipt_amount)         
        table = ''                 
        table += f"| {index} | "
        table += f"""[{row.filer_name}](/{RCP_YAML_DIR}{row.filer_markdown_file}) | """ 
        table += f"{row.candidate_name} | "
        table += f"""[{row.payor_name}](/receipts/payors/{row.payor_folder}/#{row.payor_markdown_file}) | """ 
        # table += f"{row.payor_name} | "
        table += f"{formatted_amt} | {row.receipt_date} | {row.contribution_type} |\n"      
        return table      
                
    def build_table(self, row, index) -> str:
        formatted_amt = "${:,.2f}".format(row.receipt_amount)         
        table = ''  
               
        table += f"| Rank | {index}  |\n"
        table += f"| ---- | ---- |\n"
        # table += f"| **************************** | **************************** |\n"        
        table += f"| Filer | {row.filer_name} |\n"
        table += f"| Candidate | {row.candidate_name} |\n"
        table += f"| Payor | {row.payor_name} |\n"
        table += f"| Amount | {formatted_amt} |\n"
        table += f"| Date | {row.receipt_date} |\n"
        table += f"| Type | {row.contribution_type} |\n"

        table += f"\n"
        return table
        
    def build_table_header(self) -> str:
        header = '| | |\n'
        header +=   '| :------------------------------------ | :----------------------------------- |\n'
        return header
                
    def md_header_top_100(self) -> str:
        file_header = '# Receipts: Top 500\n\n'
        return file_header
    
    def md_header_last_100(self) -> str:
        file_header = '# Receipts: Last 1500\n\n'
        return file_header    
    
    def top_100(self) -> str:
        i = 1 
        big_table = ''
        x = SelectContributions()
        y = x.top_500()
        
        for row in y:
            # inspect(row, all=True)
            # input('testes')
            single_table = self.build_new_table(row = row, index=i)
            big_table += single_table
            i += 1
        return big_table
    
    
    def last_100(self) -> str:
        i = 1 
        big_table = ''
        x = SelectContributions()
        y = x.last_1500()
        
        for row in y:
            # inspect(row, all=True)
            # input('testes')
            single_table = self.build_new_table(row = row, index=i)
            big_table += single_table
            i += 1
        return big_table    
    
    def build_file_content_top_100(self):
        md_header = self.md_header_top_100()
        table_header = self.build_new_header()
        big_table = self.top_100()
        file_content = ''        
        file_content += md_header
        file_content += table_header
        file_content += big_table  
        return file_content   
    
    def build_file_content_last_100(self):
        md_header = self.md_header_last_100()
        table_header = self.build_new_header()
        big_table = self.last_100()
        file_content = ''        
        file_content += md_header
        file_content += table_header
        file_content += big_table  
        return file_content          
    
    def write_file(self) -> None:
        # Top 500
        file_content = self.build_file_content_top_100()
        with open(f'{SITE_DIR}\\docs\\receipts\\receipts_top_500.md', 'w', encoding='utf-8') as outputfile:
            outputfile.write(file_content)
        # Last 1500
        file_content = self.build_file_content_last_100()
        with open(f'{SITE_DIR}\\docs\\receipts\\receipts_last_1500.md', 'w', encoding='utf-8') as outputfile:
            outputfile.write(file_content)        
        
        
            
        
   
        
def main():
    rcp = BuildReceiptsTables()
    rcp.write_file()
    
    exp = BuildExpendituresTables()
    exp.write_file()    
    
    

if __name__ == "__main__":
    main()
   