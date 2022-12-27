from db_dal_classes import SelectPayee, SelectPayee, SelectPayeeExpenditures
import os
import shutil
import markdown_refresh_directories as dirs
# from refresh_filers import EXP_YAML_DIR

# CWD = os.getcwd()
# BUILDER_OUTPUT_PAYEES = dirs.BUILDER_OUTPUT_PAYEES
OUTPUT_PATH_PAYEES = dirs.CWD + '\\' + dirs.BUILDER_OUTPUT_PAYEES
PAYEES_PREFIX = dirs.PAYEES_PREFIX
PAYEES_OUTPUT_PATH = dirs.PAYEES_OUTPUT_PATH
PAYEES_SINGLE_FILE_OUTPUT_PATH = dirs.PAYEES_SINGLE_FILE_OUTPUT_PATH

# PAYEES_YAML_DIR = dirs.PAYEES_YAML_DIR
PAYEES_YAML_DIR = dirs.PAYEES_YAML_DIR 
RCP_YAML_DIR = dirs.RCP_YAML_DIR
EXP_YAML_DIR = dirs.EXP_YAML_DIR
    
class BuildMkDocsYamlRecord:
    def __init__(self, payee_name, file_name):
        self.payee_directory = PAYEES_YAML_DIR
        self.payee_name = payee_name
        self.file_name = file_name
        
    def get_payee_record(self):
        record = f"""        - "{self.payee_name}": {self.payee_directory}{self.file_name}\n"""
        return record

          
class BuildAPayeeSingleFile:
    def __init__(self, payee_object):
        self.payee_object = payee_object
        self.payee_id = self.payee_object.id
        self.payee_name = self.payee_object.payee_name
        self.payee_type = self.payee_object.payee_type
        self.markdown_file = self.payee_object.markdown_file
        self.city_state = self.payee_object.city_state
                            
    def build_md_payee_hdr(self) -> str:
        payees_link_name = self.payee_name.replace(",",'')\
                .replace("'",'')        
        name_len = len(payees_link_name)
        underline = '---' + (name_len*'-')
        md_payee_head = ''
        md_payee_head += f"### {payees_link_name}\n" 
        md_payee_head += underline + '\n'
        if self.city_state != '':
            md_payee_head += f"{self.city_state}\n"         
            md_payee_head += '\n'                                                  
        return md_payee_head
        
                
    
    def build_payee_table(self) -> str:
        table = ''
        hdr_columns = """| Filer | Expenditure { data-sort-method='number' } | Date { data-sort-method='date' } |"""
        hdr_break =   '| :--------------------------------- | :--------------------------------- | :--------------------------------- |'
        hdr = hdr_columns + '\n' + hdr_break + '\n'           
        table += hdr 
        try:               
            expenditures = SelectPayeeExpenditures(payee_id=self.payee_id).all()
        except Exception as e:
            raise
        # if len(receipts) > 0:
        for exp in expenditures:
            filer_name = exp.filer_name 
            exp_amt = str(exp.expenditure_amount)
            formatted_exp_amt = "${:,.2f}".format(exp.expenditure_amount)
            exp_date = str(exp.expenditure_date)        
            row = '| '  
            # row += filer_name + ' | '
            row += f"[{filer_name}](/{EXP_YAML_DIR}{exp.filer_markdown_file}) | "
            row += formatted_exp_amt + ' { ' f""" data-sort='{exp_amt}' """ + ' } | '
            row += exp_date + ' |'
            # row += rcp_amt + ' | '            
            row += '\n' 
            table += row 
            table + '\n'
        return table               

class BuildEachPayeeSingleFileOld:
    def __init__(self, sample = False):
        self.sample = sample
        if sample == True:
            self.payees = SelectPayee().sample()
        else:        
            self.payees = SelectPayee().all()          
                                    
            
    def build_each_payee_by_name_multi(self) -> None:
                            
        payees_file_other = 'payees_other.md'
        payees_file_a_c   = 'payees_a_c.md'
        payees_file_d_f   = 'payees_d_f.md'
        payees_file_g_j   = 'payees_g_j.md'
        payees_file_k_m   = 'payees_k_m.md'
        payees_file_n_p   = 'payees_n_p.md'
        payees_file_q_s   = 'payees_q_s.md'
        payees_file_t_v   = 'payees_t_v.md'
        payees_file_w_z   = 'payees_w_z.md'
        # payees_full_path = PAYEES_OUTPUT_PATH + payees_file_name  
        payees_other_full_path = PAYEES_OUTPUT_PATH + payees_file_other
        payees_a_c_full_path = PAYEES_OUTPUT_PATH + payees_file_a_c
        payees_d_f_full_path = PAYEES_OUTPUT_PATH + payees_file_d_f    
        payees_g_j_full_path = PAYEES_OUTPUT_PATH + payees_file_g_j
        payees_k_m_full_path = PAYEES_OUTPUT_PATH + payees_file_k_m
        payees_n_p_full_path = PAYEES_OUTPUT_PATH + payees_file_n_p
        payees_q_s_full_path = PAYEES_OUTPUT_PATH + payees_file_q_s
        payees_t_v_full_path = PAYEES_OUTPUT_PATH + payees_file_t_v
        payees_w_z_full_path = PAYEES_OUTPUT_PATH + payees_file_w_z
        
               
        f_payee_other = open(payees_other_full_path, 'w', encoding='utf-8')
        f_payee_a_c = open(payees_a_c_full_path, 'w', encoding='utf-8')          
        f_payee_d_f = open(payees_d_f_full_path, 'w', encoding='utf-8')          
        f_payee_g_j = open(payees_g_j_full_path, 'w', encoding='utf-8')          
        f_payee_k_m = open(payees_k_m_full_path, 'w', encoding='utf-8')          
        f_payee_n_p = open(payees_n_p_full_path, 'w', encoding='utf-8')          
        f_payee_q_s = open(payees_q_s_full_path, 'w', encoding='utf-8')          
        f_payee_t_v = open(payees_t_v_full_path, 'w', encoding='utf-8')          
        f_payee_w_z = open(payees_w_z_full_path, 'w', encoding='utf-8')          
         
        
        f_payee_other.write('# Expenditure Payees' + '\n') 
        f_payee_other.write('## Other' + '\n') 
        f_payee_other.write('\n')         
        f_payee_a_c.write('# Expenditure Payees' + '\n') 
        f_payee_a_c.write('## A-C' + '\n') 
        f_payee_a_c.write('\n')         
        f_payee_d_f.write('# Expenditure Payees' + '\n') 
        f_payee_d_f.write('## D-F' + '\n') 
        f_payee_d_f.write('\n') 
        
        f_payee_g_j.write('# Expenditure Payees' + '\n') 
        f_payee_g_j.write('## G-J' + '\n') 
        f_payee_g_j.write('\n') 
        
        f_payee_k_m.write('# Expenditure Payees' + '\n') 
        f_payee_k_m.write('## K-M' + '\n') 
        f_payee_k_m.write('\n') 
        
        f_payee_n_p.write('# Expenditure Payees' + '\n') 
        f_payee_n_p.write('## N-P' + '\n') 
        f_payee_n_p.write('\n') 
        
        f_payee_q_s.write('# Expenditure Payees' + '\n') 
        f_payee_q_s.write('## Q-S' + '\n') 
        f_payee_q_s.write('\n') 
        
        f_payee_t_v.write('# Expenditure Payees' + '\n') 
        f_payee_t_v.write('## T-V' + '\n') 
        f_payee_t_v.write('\n') 
        
        f_payee_w_z.write('# Expenditure Payees' + '\n') 
        f_payee_w_z.write('## W-Z' + '\n') 
        f_payee_w_z.write('\n')                         
        
             
        for payee in self.payees:
            pchar = payee.payee_name[:1]
            # BUILD HEADER AND TABLE
            x = BuildAPayeeSingleFile(payee_object = payee)
            
            md_payee_head = x.build_md_payee_hdr()
            payee_table = x.build_payee_table() 
            # print(md_payee_head)       
            # print(payee_table)
            if pchar.isalpha():
                if pchar.lower() in ['a','b','c']:
                    f_payee_a_c.write('\n')
                    f_payee_a_c.write(md_payee_head)
                    f_payee_a_c.write('\n')
                    f_payee_a_c.write(payee_table)
                    f_payee_a_c.write('\n')                          
                    
                if pchar.lower() in ['d','e','f']:
                    f_payee_d_f.write('\n')
                    f_payee_d_f.write(md_payee_head)
                    f_payee_d_f.write('\n')
                    f_payee_d_f.write(payee_table)
                    f_payee_d_f.write('\n')    
                if pchar.lower() in ['g','h','i','j']:
                    f_payee_g_j.write('\n')
                    f_payee_g_j.write(md_payee_head)
                    f_payee_g_j.write('\n')
                    f_payee_g_j.write(payee_table)
                    f_payee_g_j.write('\n')    
                if pchar.lower() in ['k','l','m']:
                    f_payee_k_m.write('\n')
                    f_payee_k_m.write(md_payee_head)
                    f_payee_k_m.write('\n')
                    f_payee_k_m.write(payee_table)
                    f_payee_k_m.write('\n')    
                if pchar.lower() in ['n','o','p']:
                    f_payee_n_p.write('\n')
                    f_payee_n_p.write(md_payee_head)
                    f_payee_n_p.write('\n')
                    f_payee_n_p.write(payee_table)
                    f_payee_n_p.write('\n')    
                if pchar.lower() in ['q','r','s']:
                    f_payee_q_s.write('\n')
                    f_payee_q_s.write(md_payee_head)
                    f_payee_q_s.write('\n')
                    f_payee_q_s.write(payee_table)
                    f_payee_q_s.write('\n')    
                if pchar.lower() in ['t','u','v']:
                    f_payee_t_v.write('\n')
                    f_payee_t_v.write(md_payee_head)
                    f_payee_t_v.write('\n')
                    f_payee_t_v.write(payee_table)
                    f_payee_t_v.write('\n')    
                if pchar.lower() in ['w','x','y','z']:
                    f_payee_w_z.write('\n')
                    f_payee_w_z.write(md_payee_head)
                    f_payee_w_z.write('\n')
                    f_payee_w_z.write(payee_table)
                    f_payee_w_z.write('\n')                      
                
            else:
                f_payee_other.write('\n')
                f_payee_other.write(md_payee_head)
                f_payee_other.write('\n')
                f_payee_other.write(payee_table)
                f_payee_other.write('\n')                  

class BuildEachPayeeSingleFile:
    def __init__(self, sample = False):
        self.sample = sample
        if sample == True:
            self.payees = SelectPayee().sample()
        else:        
            self.payees = SelectPayee().all()                                                  
    
    def build_each_payee_by_name_multi(self) -> None:
                            
        payees_file_other = 'payees_other.md'
        payees_file_a   = 'payees_a.md'
        payees_file_b   = 'payees_b.md'
        payees_file_c   = 'payees_c.md'
        payees_file_d   = 'payees_d.md'
        payees_file_e   = 'payees_e.md'
        payees_file_f   = 'payees_f.md'
        payees_file_g   = 'payees_g.md'
        payees_file_h   = 'payees_h.md'
        payees_file_i   = 'payees_i.md'
        payees_file_j   = 'payees_j.md'
        payees_file_k   = 'payees_k.md'
        payees_file_l   = 'payees_l.md'
        payees_file_m   = 'payees_m.md'
        payees_file_n   = 'payees_n.md'
        payees_file_o   = 'payees_o.md'
        payees_file_p   = 'payees_p.md'
        payees_file_q   = 'payees_q.md'
        payees_file_r   = 'payees_r.md'
        payees_file_s   = 'payees_s.md'
        payees_file_t   = 'payees_t.md'
        payees_file_u   = 'payees_u.md'
        payees_file_v   = 'payees_v.md'
        payees_file_w   = 'payees_w.md'
        payees_file_x   = 'payees_x.md'
        payees_file_y   = 'payees_y.md'
        payees_file_z   = 'payees_z.md'
        
        payees_other_full_path = PAYEES_OUTPUT_PATH + payees_file_other
        payees_a_full_path = PAYEES_OUTPUT_PATH + payees_file_a
        payees_b_full_path = PAYEES_OUTPUT_PATH + payees_file_b
        payees_c_full_path = PAYEES_OUTPUT_PATH + payees_file_c
        payees_d_full_path = PAYEES_OUTPUT_PATH + payees_file_d
        payees_e_full_path = PAYEES_OUTPUT_PATH + payees_file_e
        payees_f_full_path = PAYEES_OUTPUT_PATH + payees_file_f
        payees_g_full_path = PAYEES_OUTPUT_PATH + payees_file_g
        payees_h_full_path = PAYEES_OUTPUT_PATH + payees_file_h
        payees_i_full_path = PAYEES_OUTPUT_PATH + payees_file_i
        payees_j_full_path = PAYEES_OUTPUT_PATH + payees_file_j
        payees_k_full_path = PAYEES_OUTPUT_PATH + payees_file_k
        payees_l_full_path = PAYEES_OUTPUT_PATH + payees_file_l
        payees_m_full_path = PAYEES_OUTPUT_PATH + payees_file_m
        payees_n_full_path = PAYEES_OUTPUT_PATH + payees_file_n
        payees_o_full_path = PAYEES_OUTPUT_PATH + payees_file_o
        payees_p_full_path = PAYEES_OUTPUT_PATH + payees_file_p
        payees_q_full_path = PAYEES_OUTPUT_PATH + payees_file_q
        payees_r_full_path = PAYEES_OUTPUT_PATH + payees_file_r
        payees_s_full_path = PAYEES_OUTPUT_PATH + payees_file_s
        payees_t_full_path = PAYEES_OUTPUT_PATH + payees_file_t
        payees_u_full_path = PAYEES_OUTPUT_PATH + payees_file_u
        payees_v_full_path = PAYEES_OUTPUT_PATH + payees_file_v
        payees_w_full_path = PAYEES_OUTPUT_PATH + payees_file_w
        payees_x_full_path = PAYEES_OUTPUT_PATH + payees_file_x
        payees_y_full_path = PAYEES_OUTPUT_PATH + payees_file_y
        payees_z_full_path = PAYEES_OUTPUT_PATH + payees_file_z
        
                   
        f_payee_other = open(payees_other_full_path, 'w', encoding='utf-8')
        f_payee_a = open(payees_a_full_path, 'w', encoding='utf-8')
        f_payee_b = open(payees_b_full_path, 'w', encoding='utf-8')
        f_payee_c = open(payees_c_full_path, 'w', encoding='utf-8')
        f_payee_d = open(payees_d_full_path, 'w', encoding='utf-8')
        f_payee_e = open(payees_e_full_path, 'w', encoding='utf-8')
        f_payee_f = open(payees_f_full_path, 'w', encoding='utf-8')
        f_payee_g = open(payees_g_full_path, 'w', encoding='utf-8')
        f_payee_h = open(payees_h_full_path, 'w', encoding='utf-8')
        f_payee_i = open(payees_i_full_path, 'w', encoding='utf-8')
        f_payee_j = open(payees_j_full_path, 'w', encoding='utf-8')
        f_payee_k = open(payees_k_full_path, 'w', encoding='utf-8')
        f_payee_l = open(payees_l_full_path, 'w', encoding='utf-8')
        f_payee_m = open(payees_m_full_path, 'w', encoding='utf-8')
        f_payee_n = open(payees_n_full_path, 'w', encoding='utf-8')
        f_payee_o = open(payees_o_full_path, 'w', encoding='utf-8')
        f_payee_p = open(payees_p_full_path, 'w', encoding='utf-8')
        f_payee_q = open(payees_q_full_path, 'w', encoding='utf-8')
        f_payee_r = open(payees_r_full_path, 'w', encoding='utf-8')
        f_payee_s = open(payees_s_full_path, 'w', encoding='utf-8')
        f_payee_t = open(payees_t_full_path, 'w', encoding='utf-8')
        f_payee_u = open(payees_u_full_path, 'w', encoding='utf-8')
        f_payee_v = open(payees_v_full_path, 'w', encoding='utf-8')
        f_payee_w = open(payees_w_full_path, 'w', encoding='utf-8')
        f_payee_x = open(payees_x_full_path, 'w', encoding='utf-8')
        f_payee_y = open(payees_y_full_path, 'w', encoding='utf-8')
        f_payee_z = open(payees_z_full_path, 'w', encoding='utf-8')

       
        
        f_payee_other.write('# Contribution Payors' + '\n') 
        f_payee_other.write('## Other' + '\n') 
        f_payee_other.write('\n')         
        f_payee_a.write('# Contribution Payors' + '\n') 
        f_payee_a.write('## A' + '\n') 
        f_payee_a.write('\n')
        f_payee_b.write('# Contribution Payors' + '\n') 
        f_payee_b.write('## B' + '\n') 
        f_payee_b.write('\n')
        f_payee_c.write('# Contribution Payors' + '\n') 
        f_payee_c.write('## C' + '\n') 
        f_payee_c.write('\n')
        f_payee_d.write('# Contribution Payors' + '\n') 
        f_payee_d.write('## D' + '\n') 
        f_payee_d.write('\n')
        f_payee_e.write('# Contribution Payors' + '\n') 
        f_payee_e.write('## E' + '\n') 
        f_payee_e.write('\n')
        f_payee_f.write('# Contribution Payors' + '\n') 
        f_payee_f.write('## F' + '\n') 
        f_payee_f.write('\n')
        f_payee_g.write('# Contribution Payors' + '\n') 
        f_payee_g.write('## G' + '\n') 
        f_payee_g.write('\n')
        f_payee_h.write('# Contribution Payors' + '\n') 
        f_payee_h.write('## H' + '\n') 
        f_payee_h.write('\n')
        f_payee_i.write('# Contribution Payors' + '\n') 
        f_payee_i.write('## I' + '\n') 
        f_payee_i.write('\n')
        f_payee_j.write('# Contribution Payors' + '\n') 
        f_payee_j.write('## J' + '\n') 
        f_payee_j.write('\n')
        f_payee_k.write('# Contribution Payors' + '\n') 
        f_payee_k.write('## K' + '\n') 
        f_payee_k.write('\n')
        f_payee_l.write('# Contribution Payors' + '\n') 
        f_payee_l.write('## L' + '\n') 
        f_payee_l.write('\n')
        f_payee_m.write('# Contribution Payors' + '\n') 
        f_payee_m.write('## M' + '\n') 
        f_payee_m.write('\n')
        f_payee_n.write('# Contribution Payors' + '\n') 
        f_payee_n.write('## N' + '\n') 
        f_payee_n.write('\n')
        f_payee_o.write('# Contribution Payors' + '\n') 
        f_payee_o.write('## O' + '\n') 
        f_payee_o.write('\n')
        f_payee_p.write('# Contribution Payors' + '\n') 
        f_payee_p.write('## P' + '\n') 
        f_payee_p.write('\n')
        f_payee_q.write('# Contribution Payors' + '\n') 
        f_payee_q.write('## Q' + '\n') 
        f_payee_q.write('\n')
        f_payee_r.write('# Contribution Payors' + '\n') 
        f_payee_r.write('## R' + '\n') 
        f_payee_r.write('\n')
        f_payee_s.write('# Contribution Payors' + '\n') 
        f_payee_s.write('## S' + '\n') 
        f_payee_s.write('\n')
        f_payee_t.write('# Contribution Payors' + '\n') 
        f_payee_t.write('## T' + '\n') 
        f_payee_t.write('\n')
        f_payee_u.write('# Contribution Payors' + '\n') 
        f_payee_u.write('## U' + '\n') 
        f_payee_u.write('\n')
        f_payee_v.write('# Contribution Payors' + '\n') 
        f_payee_v.write('## V' + '\n') 
        f_payee_v.write('\n')
        f_payee_w.write('# Contribution Payors' + '\n') 
        f_payee_w.write('## W' + '\n') 
        f_payee_w.write('\n')
        f_payee_x.write('# Contribution Payors' + '\n') 
        f_payee_x.write('## X' + '\n') 
        f_payee_x.write('\n')
        f_payee_y.write('# Contribution Payors' + '\n') 
        f_payee_y.write('## Y' + '\n') 
        f_payee_y.write('\n')
        f_payee_z.write('# Contribution Payors' + '\n') 
        f_payee_z.write('## Z' + '\n') 
        f_payee_z.write('\n')
        
        
                                                                                                                                                                                                                         
             
             
        for payee in self.payees:
            pchar = payee.payee_name[:1]
            # BUILD HEADER AND TABLE
            x = BuildAPayeeSingleFile(payee_object = payee)
            
            md_payee_head = x.build_md_payee_hdr()
            payee_table = x.build_payee_table() 
            if pchar.isalpha():
                if pchar.lower() == 'a':
                    f_payee_a.write('\n')
                    f_payee_a.write(md_payee_head)
                    f_payee_a.write('\n')
                    f_payee_a.write(payee_table)
                    f_payee_a.write('\n')    
                
                if pchar.lower() == 'b':
                    f_payee_b.write('\n')
                    f_payee_b.write(md_payee_head)
                    f_payee_b.write('\n')
                    f_payee_b.write(payee_table)
                    f_payee_b.write('\n')                                                
                if pchar.lower() == 'c':
                    f_payee_c.write('\n')
                    f_payee_c.write(md_payee_head)
                    f_payee_c.write('\n')
                    f_payee_c.write(payee_table)
                    f_payee_c.write('\n')                                                
                if pchar.lower() == 'd':
                    f_payee_d.write('\n')
                    f_payee_d.write(md_payee_head)
                    f_payee_d.write('\n')
                    f_payee_d.write(payee_table)
                    f_payee_d.write('\n')                                                
                if pchar.lower() == 'e':
                    f_payee_e.write('\n')
                    f_payee_e.write(md_payee_head)
                    f_payee_e.write('\n')
                    f_payee_e.write(payee_table)
                    f_payee_e.write('\n')                                                
                if pchar.lower() == 'f':
                    f_payee_f.write('\n')
                    f_payee_f.write(md_payee_head)
                    f_payee_f.write('\n')
                    f_payee_f.write(payee_table)
                    f_payee_f.write('\n')                                                
                if pchar.lower() == 'g':
                    f_payee_g.write('\n')
                    f_payee_g.write(md_payee_head)
                    f_payee_g.write('\n')
                    f_payee_g.write(payee_table)
                    f_payee_g.write('\n')                                                
                if pchar.lower() == 'h':
                    f_payee_h.write('\n')
                    f_payee_h.write(md_payee_head)
                    f_payee_h.write('\n')
                    f_payee_h.write(payee_table)
                    f_payee_h.write('\n')                                                
                if pchar.lower() == 'i':
                    f_payee_i.write('\n')
                    f_payee_i.write(md_payee_head)
                    f_payee_i.write('\n')
                    f_payee_i.write(payee_table)
                    f_payee_i.write('\n')                                                
                if pchar.lower() == 'j':
                    f_payee_j.write('\n')
                    f_payee_j.write(md_payee_head)
                    f_payee_j.write('\n')
                    f_payee_j.write(payee_table)
                    f_payee_j.write('\n')                                                
                if pchar.lower() == 'k':
                    f_payee_k.write('\n')
                    f_payee_k.write(md_payee_head)
                    f_payee_k.write('\n')
                    f_payee_k.write(payee_table)
                    f_payee_k.write('\n')                                                
                if pchar.lower() == 'l':
                    f_payee_l.write('\n')
                    f_payee_l.write(md_payee_head)
                    f_payee_l.write('\n')
                    f_payee_l.write(payee_table)
                    f_payee_l.write('\n')                                                
                if pchar.lower() == 'm':
                    f_payee_m.write('\n')
                    f_payee_m.write(md_payee_head)
                    f_payee_m.write('\n')
                    f_payee_m.write(payee_table)
                    f_payee_m.write('\n')                                                
                if pchar.lower() == 'n':
                    f_payee_n.write('\n')
                    f_payee_n.write(md_payee_head)
                    f_payee_n.write('\n')
                    f_payee_n.write(payee_table)
                    f_payee_n.write('\n')                                                
                if pchar.lower() == 'o':
                    f_payee_o.write('\n')
                    f_payee_o.write(md_payee_head)
                    f_payee_o.write('\n')
                    f_payee_o.write(payee_table)
                    f_payee_o.write('\n')                                                
                if pchar.lower() == 'p':
                    f_payee_p.write('\n')
                    f_payee_p.write(md_payee_head)
                    f_payee_p.write('\n')
                    f_payee_p.write(payee_table)
                    f_payee_p.write('\n')                                                
                if pchar.lower() == 'q':
                    f_payee_q.write('\n')
                    f_payee_q.write(md_payee_head)
                    f_payee_q.write('\n')
                    f_payee_q.write(payee_table)
                    f_payee_q.write('\n')                                                
                if pchar.lower() == 'r':
                    f_payee_r.write('\n')
                    f_payee_r.write(md_payee_head)
                    f_payee_r.write('\n')
                    f_payee_r.write(payee_table)
                    f_payee_r.write('\n')                                                
                if pchar.lower() == 's':
                    f_payee_s.write('\n')
                    f_payee_s.write(md_payee_head)
                    f_payee_s.write('\n')
                    f_payee_s.write(payee_table)
                    f_payee_s.write('\n')                                                
                if pchar.lower() == 't':
                    f_payee_t.write('\n')
                    f_payee_t.write(md_payee_head)
                    f_payee_t.write('\n')
                    f_payee_t.write(payee_table)
                    f_payee_t.write('\n')                                                
                if pchar.lower() == 'u':
                    f_payee_t.write('\n')
                    f_payee_t.write(md_payee_head)
                    f_payee_t.write('\n')
                    f_payee_t.write(payee_table)
                    f_payee_t.write('\n')                                                
                if pchar.lower() == 'v':
                    f_payee_v.write('\n')
                    f_payee_v.write(md_payee_head)
                    f_payee_v.write('\n')
                    f_payee_v.write(payee_table)
                    f_payee_v.write('\n')                                                
                if pchar.lower() == 'w':
                    f_payee_w.write('\n')
                    f_payee_w.write(md_payee_head)
                    f_payee_w.write('\n')
                    f_payee_w.write(payee_table)
                    f_payee_w.write('\n')                                                
                if pchar.lower() == 'x':
                    f_payee_x.write('\n')
                    f_payee_x.write(md_payee_head)
                    f_payee_x.write('\n')
                    f_payee_x.write(payee_table)
                    f_payee_x.write('\n')                                                
                if pchar.lower() == 'y':
                    f_payee_y.write('\n')
                    f_payee_y.write(md_payee_head)
                    f_payee_y.write('\n')
                    f_payee_y.write(payee_table)
                    f_payee_y.write('\n')                                                
                if pchar.lower() == 'z':
                    f_payee_z.write('\n')
                    f_payee_z.write(md_payee_head)
                    f_payee_z.write('\n')
                    f_payee_z.write(payee_table)
                    f_payee_z.write('\n')                                                
                                                                 
                
            else:
                f_payee_other.write('\n')
                f_payee_other.write(md_payee_head)
                f_payee_other.write('\n')
                f_payee_other.write(payee_table)
                f_payee_other.write('\n')                  



def get_payees_file(payee_name):
    payees_file = get_payees_dir(payee_name) + '.md'
    return payees_file
                                                             
def get_payees_dir(payee_name):
    prefix ='payees_'
    pchar = payee_name[:1]
    if pchar.isalpha():
        payees_dir = prefix + '_' + pchar
    else: 
        payees_dir = prefix + '_other'        
    return payees_dir
    
                                                        
def remove_files(dir):
    for files in os.listdir(dir):
        path = os.path.join(dir, files)
        try:
            shutil.rmtree(path)
        except OSError:
            os.remove(path)     
    
def cleanup_dirs():  
    remove_files(OUTPUT_PATH_PAYEES) 
    # remove_files(OUTPUT_PATH_EXP)
          
          
# def main_by_name_sample():
#     cleanup_dirs()
#     x = BuildEachPayee(sample=True)
#     x.build_each_payee_by_name()
    
    
# def main_by_name():
#     cleanup_dirs()
#     x = BuildEachPayee(sample=False)
#     x.build_each_payee_by_name()  
    
# def main_single_file():
#     x = BuildEachPayeeSingleFile()
#     x.build_each_payee_by_name()
#     # x.build_each_payee_by_name_multi()
#     # print(payee_hdr)     
    
def main_multi_file():
    cleanup_dirs()
    x = BuildEachPayeeSingleFile()
    x.build_each_payee_by_name_multi()
    remove_single_file()
    
def remove_single_file():
    file = PAYEES_SINGLE_FILE_OUTPUT_PATH + '\\' + 'payees.md'
    if os.path.exists(file):
        os.remove(file)     


if __name__ == "__main__":
    # remove_single_file()
    cleanup_dirs()
    main_multi_file()
    remove_single_file()
