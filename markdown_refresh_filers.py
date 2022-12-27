from db_dal_classes import SelectOrgContributions, SelectFiler, SelectOrgExpenditures
import os
import shutil
import markdown_refresh_directories as dirs
# from refresh_payees import PAYEES_YAML_DIR
# from refresh_payors import PAYORS_YAML_DIR

CWD = os.getcwd()
BUILDER_OUTPUT_RCP = dirs.BUILDER_OUTPUT_RCP
BUILDER_OUTPUT_EXP = dirs.BUILDER_OUTPUT_EXP
OUTPUT_PATH_RCP = CWD + '\\' + BUILDER_OUTPUT_RCP
OUTPUT_PATH_EXP = CWD + '\\' + BUILDER_OUTPUT_EXP
# OUTPUT_PATH_RCP = CWD + '\\' + BUILDER_OUTPUT_RCP + '\\'
# OUTPUT_PATH_EXP = CWD + '\\' + BUILDER_OUTPUT_EXP + '\\'
RCP_PREFIX = 'rcp_'
EXP_PREFIX = 'exp_'
RCP_OUTPUT_PATH = OUTPUT_PATH_RCP + '\\'
EXP_OUTPUT_PATH = OUTPUT_PATH_EXP + '\\'

PAYORS_YAML_DIR = dirs.PAYORS_YAML_DIR
PAYEES_YAML_DIR = dirs.PAYEES_YAML_DIR 
RCP_YAML_DIR = dirs.RCP_YAML_DIR
EXP_YAML_DIR = dirs.EXP_YAML_DIR

class BuildAFiler:
    def __init__(self, filer_object):
        self.filer_object = filer_object
        self.org_id = self.filer_object.org_id
        self.filer_name = self.filer_object.filer_name
        self.filer_type = self.filer_object.filer_type
        # self.filer_markdown_file = self.filer_object.filer_markdown_file
   
            
    def build_rcp_tags(self) -> str:
        tags = ''
        tag_header = ''
        tag_header += '---\n'
        tag_header += 'tags:\n'
        tag_footer = ''
        tag_footer += '---\n\n'
        tag_body = ''
        if self.org_id in [7688,7707,7582,7695,7417,7579]:
            tag_body = '  - Governor 2022 - Receipts\n'
                                
        if self.org_id in [7620,7325,7425,7680,7582,7375,7357,7513,7394,7520,7476,7579,7356,7659,7491,7411,7360\
            ,7564,7345,7431,7457,7339,7405,7374,7551,7413,7473,7699,7319,7626,7541,7586,7642,7452\
            ,7649,7458,7548,7456,7388,7365,7347,7430,7636,7445,7550,7591,7321,7530,7404,7624,7640]:
            tag_body += 'Current Unicam - Expenditures\n'
        if tag_body != '':
            tags = tag_header + tag_body + tag_footer             
        return tags
    
    def build_exp_tags(self) -> str:
        tags = ''
        tag_header = ''
        tag_header += '---\n'
        tag_header += 'tags:\n'
        tag_footer = ''
        tag_footer += '---\n\n'
        tag_body = ''
        if self.org_id in [7688,7707,7582,7695,7417,7579]:
            tag_body += '  - Governor 2022 - Expenditures\n'
                                
        if self.org_id in [7620,7325,7425,7680,7582,7375,7357,7513,7394,7520,7476,7579,7356,7659,7491,7411,7360\
            ,7564,7345,7431,7457,7339,7405,7374,7551,7413,7473,7699,7319,7626,7541,7586,7642,7452\
            ,7649,7458,7548,7456,7388,7365,7347,7430,7636,7445,7550,7591,7321,7530,7404,7624,7640]:
            tag_body += 'Current Unicam - Expenditures\n'
        if tag_body != '':
            tags = tag_header + tag_body + tag_footer        
        return tags             
               
        
    def build_md_rcp_hdr(self) -> str:
        tags = self.build_rcp_tags()
        
        # filer_underline = (len(self.filer_name)+2) * '-'
        md_filer_head = ''
        
        if tags != '':
            md_filer_head = tags
        
        md_filer_head += f"# {self.filer_name}\n" 
        md_filer_head += '\n'
        md_filer_head += f"Contribution Receipts\n"
        md_filer_head += '\n'
        md_filer_head += "######\n"
        md_filer_head += '\n'                                          
        
        return md_filer_head      
        
        
    def build_md_exp_hdr(self) -> str:
        tags = self.build_exp_tags()        
        # filer_underline = (len(self.filer_name)+2) * '-'
        md_filer_head = ''
        
        if tags != '':
            md_filer_head = tags        
        
        md_filer_head += f"# {self.filer_name}\n" 
        md_filer_head += '\n'        
        md_filer_head += f"Expenditures\n"
        md_filer_head += '\n'        
        md_filer_head += "######\n"
        md_filer_head += '\n'                
               
        return md_filer_head         
   
    
    def build_receipt_table_multi(self) -> str:
        table = ''
        hdr_columns = "| Payor | City | State |Receipt { data-sort-method='number' } | Date { data-sort-method='date' } |"
        hdr_break =   '| :--------------------------------- | :--------------------------------- | :--------------------------------- | :--------------------------------- | :--------------------------------- |'
        hdr = hdr_columns + '\n' + hdr_break + '\n'           
        table += hdr                
        receipts = SelectOrgContributions(org_id=self.org_id).all()
        # if len(receipts) > 0:    
        for rcp in receipts:
            pchar = rcp.payor_name[:1]
            payors_file_other = 'payors_other'
            payors_file_a_c   = 'payors_a_c'
            payors_file_d_f   = 'payors_d_f'
            payors_file_g_j   = 'payors_g_j'
            payors_file_k_m   = 'payors_k_m'
            payors_file_n_p   = 'payors_n_p'
            payors_file_q_s   = 'payors_q_s'
            payors_file_t_v   = 'payors_t_v'
            payors_file_w_z   = 'payors_w_z'            
            if pchar.isalpha():

                if pchar.lower() in ['a','b','c']:
                    payors_file_name = payors_file_a_c                                          
                if pchar.lower() in ['d','e','f']:
                    payors_file_name = payors_file_d_f
                if pchar.lower() in ['g','h','i','j']:
                    payors_file_name = payors_file_g_j   
                if pchar.lower() in ['k','l','m']:
                    payors_file_name = payors_file_k_m 
                if pchar.lower() in ['n','o','p']:
                    payors_file_name = payors_file_n_p   
                if pchar.lower() in ['q','r','s']:
                    payors_file_name = payors_file_q_s    
                if pchar.lower() in ['t','u','v']:
                    payors_file_name = payors_file_t_v   
                if pchar.lower() in ['w','x','y','z']:
                    payors_file_name = payors_file_w_z                                     
            else:
                payors_file_name = payors_file_other
            payor_name = rcp.payor_name 
            rcp_amt = str(rcp.receipt_amount)
            formatted_rcp_amt = "${:,.2f}".format(rcp.receipt_amount)               
            rcp_date = str(rcp.receipt_date)        
            row = '| '  
            
            row += f"[{payor_name}](/{PAYORS_YAML_DIR}{rcp.payor_folder}/#{rcp.payor_markdown_file}) | "            
            row += rcp.city + ' | '
            row += rcp.state + ' | '
            row += formatted_rcp_amt + ' { ' f""" data-sort='{rcp_amt}' """ + ' } | '            
            row += rcp_date + ' |'
            row += '\n' 
            table += row 
        return table                  
    
    
    def build_expenditure_table_multi(self) -> str:
        table = ''
        hdr_columns = "| Payee | City | State | Expenditure { data-sort-method='number' } | Date { data-sort-method='date' } |"
        hdr_break =   '| :--------------------------------- | :--------------------------------- | :--------------------------------- | :--------------------------------- | :--------------------------------- |'
        hdr = hdr_columns + '\n' + hdr_break + '\n'           
        table += hdr                
        expenditures = SelectOrgExpenditures(org_id=self.org_id).all()
        for exp in expenditures:
            # pchar = exp.payee_name[:1]
            # payees_file_other = 'payees_other'
            # payees_file_a_c   = 'payees_a_c'
            # payees_file_d_f   = 'payees_d_f'
            # payees_file_g_j   = 'payees_g_j'
            # payees_file_k_m   = 'payees_k_m'
            # payees_file_n_p   = 'payees_n_p'
            # payees_file_q_s   = 'payees_q_s'
            # payees_file_t_v   = 'payees_t_v'
            # payees_file_w_z   = 'payees_w_z'            
            # if pchar.isalpha():

            #     if pchar.lower() in ['a','b','c']:
            #         payees_file_name = payees_file_a_c                                          
            #     if pchar.lower() in ['d','e','f']:
            #         payees_file_name = payees_file_d_f
            #     if pchar.lower() in ['g','h','i','j']:
            #         payees_file_name = payees_file_g_j   
            #     if pchar.lower() in ['k','l','m']:
            #         payees_file_name = payees_file_k_m 
            #     if pchar.lower() in ['n','o','p']:
            #         payees_file_name = payees_file_n_p   
            #     if pchar.lower() in ['q','r','s']:
            #         payees_file_name = payees_file_q_s    
            #     if pchar.lower() in ['t','u','v']:
            #         payees_file_name = payees_file_t_v   
            #     if pchar.lower() in ['w','x','y','z']:
            #         payees_file_name = payees_file_w_z                                     
            # else:
            #     payees_file_name = payees_file_other
            payee_name = exp.payee_name 
            exp_amt = str(exp.expenditure_amount)
            formatted_exp_amt = "${:,.2f}".format(exp.expenditure_amount)               
            exp_date = str(exp.expenditure_date)        
            row = '| '  
            # row += payee_name + ' | '
            row += f"[{payee_name}](/{PAYEES_YAML_DIR}{exp.payee_folder}/#{exp.payee_markdown_file}) | "            
            # row += exp_amt + ' | ' 
            row += exp.city + ' | '
            row += exp.state + ' | '            
            row += formatted_exp_amt + ' { ' f""" data-sort='{exp_amt}' """ + ' } | '            
            row += exp_date + ' |'
            row += '\n' 
            table += row 
        return table            
                   
    
    
class BuildMkDocsYamlRecord:
    def __init__(self, filer_name, file_name):
        self.rcp_directory = RCP_YAML_DIR
        self.exp_directory = EXP_YAML_DIR
        self.filer_name = filer_name
        self.file_name = file_name
        
    def get_rcp_record(self):
        record = f"""        - "{self.filer_name}": {self.rcp_directory}{self.file_name}\n"""
        return record
            
    def get_exp_record(self):
        record = f"""        - "{self.filer_name}": {self.exp_directory}{self.file_name}\n"""
        return record



class BuildEachFiler:
    def __init__(self, sample = False, select = False):
        self.sample = sample
        if sample:
            self.filers = SelectFiler().sample()
        elif select:
            self.filers = SelectFiler().select_group()
        else:
            self.filers = SelectFiler().all()
        
    

    def build_each_filer_multi(self) -> None:                                
        rcp_yaml_file = open('rcp_yaml.txt', 'w', encoding='utf-8')
        exp_yaml_file = open('exp_yaml.txt', 'w', encoding='utf-8')
                                                        
        for filer in self.filers:
            exp_cnt = filer.expenditure_count    
            rcp_cnt = filer.receipt_count
            
            # DEFINE FILE NAME & PATH 
            if rcp_cnt >= 1:
                rcp_file_name = filer.markdown_file + '.md'           
                rcp_full_path = RCP_OUTPUT_PATH + rcp_file_name         
                f_rcp = open(rcp_full_path, 'w', encoding='utf-8')     
            
            if exp_cnt >= 1:
                exp_file_name = filer.markdown_file + '.md'
                exp_full_path = EXP_OUTPUT_PATH + exp_file_name
                f_exp = open(exp_full_path, 'w', encoding='utf-8')            
            
            
            # BUILD HEADER AND TABLE
            x = BuildAFiler(filer_object = filer)
            
            # FOR RECEIPTS
            if rcp_cnt >= 1:
                md_rcp_head = x.build_md_rcp_hdr()
                rcp_table = x.build_receipt_table_multi()        
                f_rcp.write(md_rcp_head)
                f_rcp.write(rcp_table)
                # print(md_rcp_head)       
                # print(rcp_table)                  
            
            # FOR EXPENDITURES
            if exp_cnt >= 1:
                md_exp_head = x.build_md_exp_hdr()
                exp_table = x.build_expenditure_table_multi()        
                f_exp.write(md_exp_head)
                f_exp.write(exp_table) 
                # print(md_exp_head)       
                # print(exp_table)       
            
            # WRITE RCP YAML RECORD
            if rcp_cnt >= 1:
                yaml = BuildMkDocsYamlRecord(filer_name=x.filer_name, file_name = rcp_file_name )
                rcp_yaml_file.write(yaml.get_rcp_record())
            
            # WRITE EXP YAML RECORD 
            if exp_cnt >= 1:
                yaml = BuildMkDocsYamlRecord(filer_name=x.filer_name, file_name = exp_file_name )
                exp_yaml_file.write(yaml.get_exp_record())   




def remove_files(dir):
    for files in os.listdir(dir):
        path = os.path.join(dir, files)
        try:
            shutil.rmtree(path)
        except OSError:
            os.remove(path)     
    
def cleanup_dirs():  
    remove_files(OUTPUT_PATH_RCP) 
    remove_files(OUTPUT_PATH_EXP)
                     
   
# def main_by_name_sample():    
#     cleanup_dirs()
#     x = BuildEachFiler(sample=True)
#     x.build_each_filer_by_name()
    
# def main_by_name():    
#     cleanup_dirs()
#     x = BuildEachFiler(sample=False)
#     x.build_each_filer_by_name()  
    
# def main_by_name_select():    
#     cleanup_dirs()
#     x = BuildEachFiler(sample=False, select=True)
#     x.build_each_filer_by_name()       
    
    
# def main_by_id_sample():    
#     cleanup_dirs()
#     x = BuildEachFiler(sample=True)
#     x.build_each_filer_by_id()    
    
def main_by_name_multi():    
    cleanup_dirs()
    x = BuildEachFiler(sample=False)
    x.build_each_filer_multi()      
    
if __name__ == "__main__":
    main_by_name_multi()
  