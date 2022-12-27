from db_dal_classes import SelectPayor, SelectPayor, SelectPayorContributions
import os
import shutil
import markdown_refresh_directories as dirs
# from refresh_filers import RCP_YAML_DIR

# CWD = os.getcwd()
# BUILDER_OUTPUT_PAYORS = 'datanebraska\\docs\\campaign_finance\\receipts\\payors'
OUTPUT_PATH_PAYORS = dirs.CWD + '\\' + dirs.BUILDER_OUTPUT_PAYORS
PAYORS_PREFIX = dirs.PAYORS_PREFIX
PAYORS_OUTPUT_PATH = dirs.PAYORS_OUTPUT_PATH
PAYORS_SINGLE_FILE_OUTPUT_PATH = dirs.PAYORS_SINGLE_FILE_OUTPUT_PATH

PAYORS_YAML_DIR = dirs.PAYORS_YAML_DIR
RCP_YAML_DIR = dirs.RCP_YAML_DIR
EXP_YAML_DIR = dirs.EXP_YAML_DIR


class BuildMkDocsYamlRecord:
    def __init__(self, payor_name, file_name):
        self.payor_directory = PAYORS_YAML_DIR
        self.payor_name = payor_name
        self.file_name = file_name
        
    def get_payor_record(self):
        payor_rec = f"""        - "{self.payor_name}": {self.payor_directory}{self.file_name}\n"""
        return payor_rec


class BuildAPayor:
    def __init__(self, payor_object):
        self.payor_object = payor_object
        self.payor_id = self.payor_object.id
        self.payor_name = self.payor_object.payor_name
        self.payor_type = self.payor_object.payor_type
        self.markdown_file = self.payor_object.markdown_file
        self.city_state = self.payor_object.city_state        
     
               
        
    def build_md_payor_hdr(self) -> str:
        md_payor_head = ''
        md_payor_head += "\n"
        md_payor_head += f"# {self.payor_name}\n" 
        md_payor_head += f"{self.city_state}\n"                 
        md_payor_head += '\n'
        md_payor_head += f"**Contribution Payor**\n"
                      
        md_payor_head += '\n'
        md_payor_head += "######\n"
        md_payor_head += '\n'                                          
        
        return md_payor_head                        
    
    def build_payor_table(self) -> str:
        table = ''
        hdr_columns = "| Filer | Receipt { data-sort-method='number' } | Date { data-sort-method='date' } |"
        hdr_break =   '| :--------------------------------- | :--------------------------------- | :--------------------------------- |'
        hdr = hdr_columns + '\n' + hdr_break + '\n'           
        table += hdr                
        receipts = SelectPayorContributions(payor_id=self.payor_id).all()
        
        for rcp in receipts:
            filer_name = rcp.filer_name 
            rcp_amt = str(rcp.receipt_amount)
            formatted_rcp_amt = "${:,.2f}".format(rcp.receipt_amount)
            rcp_date = str(rcp.receipt_date)
            row = '| '
            row += f"""[{filer_name}](/{RCP_YAML_DIR}{rcp.filer_markdown_file}) | """
            
            row += formatted_rcp_amt
            row += rcp_date + ' { ' f""" data-sort='{rcp_amt}' """ + ' } | '
            row += '\n' 
            table += row 
        return table   
                              
    
    

        
class BuildAPayorSingleFile:
    def __init__(self, payor_object):
        self.payor_object = payor_object
        self.payor_id = self.payor_object.id
        self.payor_name = self.payor_object.payor_name
        self.payor_type = self.payor_object.payor_type
        self.markdown_file = self.payor_object.markdown_file
        self.city_state = self.payor_object.city_state
                            
    def build_md_payor_hdr(self) -> str:
        payors_link_name = self.payor_name.replace(",",'')\
                .replace("'",'')        
        name_len = len(payors_link_name)
        underline = '---' + (name_len*'-')
        md_payor_head = ''
        md_payor_head += f"## {payors_link_name}\n" 
        md_payor_head += underline + '\n'
        if self.city_state != '':
            md_payor_head += f"{self.city_state}\n"         
            md_payor_head += '\n'                                                  
        return md_payor_head
        
                
    
    def build_payor_table(self) -> str:
        table = ''
        hdr_columns = "| Filer | Receipt { data-sort-method='number' } | Date { data-sort-method='date' } |"
        hdr_break =   '| :--------------------------------- | :--------------------------------- | :--------------------------------- |'
        hdr = hdr_columns + '\n' + hdr_break + '\n'           
        table += hdr                
        receipts = SelectPayorContributions(payor_id=self.payor_id).all()
        # if len(receipts) > 0:
        for rcp in receipts:
            filer_name = rcp.filer_name 
            rcp_amt = str(rcp.receipt_amount)
            formatted_rcp_amt = "${:,.2f}".format(rcp.receipt_amount)            
            rcp_date = str(rcp.receipt_date)        
            row = '| '  
            row += f"[{filer_name}](/{RCP_YAML_DIR}{rcp.filer_markdown_file}) | "
            # row += rcp_amt + ' | ' 
            row += formatted_rcp_amt + ' { ' f""" data-sort='{rcp_amt}' """ + ' } | '            
            row += rcp_date + ' |'
            row += '\n' 
            table += row  
            table + '\n'
        return table               


class BuildEachPayorSingleFileNew:
    def __init__(self, sample = False):
        self.sample = sample
        if sample == True:
            self.payors = SelectPayor().sample()
        else:        
            self.payors = SelectPayor().all() 
    
    def build_each_payor(self) -> None:
        # payor_file = self.payors.payor_folder
        for x in self.payors:        
            print(x.payor_folder)

class BuildEachPayorSingleFile:
    def __init__(self, sample = False):
        self.sample = sample
        if sample == True:
            self.payors = SelectPayor().sample()
        else:        
            self.payors = SelectPayor().all()                                                  
    
    def build_each_payor_by_name_multi(self) -> None:
                            
        payors_file_other = 'payors_other.md'
        payors_file_a   = 'payors_a.md'
        payors_file_b   = 'payors_b.md'
        payors_file_c   = 'payors_c.md'
        payors_file_d   = 'payors_d.md'
        payors_file_e   = 'payors_e.md'
        payors_file_f   = 'payors_f.md'
        payors_file_g   = 'payors_g.md'
        payors_file_h   = 'payors_h.md'
        payors_file_i   = 'payors_i.md'
        payors_file_j   = 'payors_j.md'
        payors_file_k   = 'payors_k.md'
        payors_file_l   = 'payors_l.md'
        payors_file_m   = 'payors_m.md'
        payors_file_n   = 'payors_n.md'
        payors_file_o   = 'payors_o.md'
        payors_file_p   = 'payors_p.md'
        payors_file_q   = 'payors_q.md'
        payors_file_r   = 'payors_r.md'
        payors_file_s   = 'payors_s.md'
        payors_file_t   = 'payors_t.md'
        payors_file_u   = 'payors_u.md'
        payors_file_v   = 'payors_v.md'
        payors_file_w   = 'payors_w.md'
        payors_file_x   = 'payors_x.md'
        payors_file_y   = 'payors_y.md'
        payors_file_z   = 'payors_z.md'
        
        payors_other_full_path = PAYORS_OUTPUT_PATH + payors_file_other
        payors_a_full_path = PAYORS_OUTPUT_PATH + payors_file_a
        payors_b_full_path = PAYORS_OUTPUT_PATH + payors_file_b
        payors_c_full_path = PAYORS_OUTPUT_PATH + payors_file_c
        payors_d_full_path = PAYORS_OUTPUT_PATH + payors_file_d
        payors_e_full_path = PAYORS_OUTPUT_PATH + payors_file_e
        payors_f_full_path = PAYORS_OUTPUT_PATH + payors_file_f
        payors_g_full_path = PAYORS_OUTPUT_PATH + payors_file_g
        payors_h_full_path = PAYORS_OUTPUT_PATH + payors_file_h
        payors_i_full_path = PAYORS_OUTPUT_PATH + payors_file_i
        payors_j_full_path = PAYORS_OUTPUT_PATH + payors_file_j
        payors_k_full_path = PAYORS_OUTPUT_PATH + payors_file_k
        payors_l_full_path = PAYORS_OUTPUT_PATH + payors_file_l
        payors_m_full_path = PAYORS_OUTPUT_PATH + payors_file_m
        payors_n_full_path = PAYORS_OUTPUT_PATH + payors_file_n
        payors_o_full_path = PAYORS_OUTPUT_PATH + payors_file_o
        payors_p_full_path = PAYORS_OUTPUT_PATH + payors_file_p
        payors_q_full_path = PAYORS_OUTPUT_PATH + payors_file_q
        payors_r_full_path = PAYORS_OUTPUT_PATH + payors_file_r
        payors_s_full_path = PAYORS_OUTPUT_PATH + payors_file_s
        payors_t_full_path = PAYORS_OUTPUT_PATH + payors_file_t
        payors_u_full_path = PAYORS_OUTPUT_PATH + payors_file_u
        payors_v_full_path = PAYORS_OUTPUT_PATH + payors_file_v
        payors_w_full_path = PAYORS_OUTPUT_PATH + payors_file_w
        payors_x_full_path = PAYORS_OUTPUT_PATH + payors_file_x
        payors_y_full_path = PAYORS_OUTPUT_PATH + payors_file_y
        payors_z_full_path = PAYORS_OUTPUT_PATH + payors_file_z
        
                   
        f_payor_other = open(payors_other_full_path, 'w', encoding='utf-8')
        f_payor_a = open(payors_a_full_path, 'w', encoding='utf-8')
        f_payor_b = open(payors_b_full_path, 'w', encoding='utf-8')
        f_payor_c = open(payors_c_full_path, 'w', encoding='utf-8')
        f_payor_d = open(payors_d_full_path, 'w', encoding='utf-8')
        f_payor_e = open(payors_e_full_path, 'w', encoding='utf-8')
        f_payor_f = open(payors_f_full_path, 'w', encoding='utf-8')
        f_payor_g = open(payors_g_full_path, 'w', encoding='utf-8')
        f_payor_h = open(payors_h_full_path, 'w', encoding='utf-8')
        f_payor_i = open(payors_i_full_path, 'w', encoding='utf-8')
        f_payor_j = open(payors_j_full_path, 'w', encoding='utf-8')
        f_payor_k = open(payors_k_full_path, 'w', encoding='utf-8')
        f_payor_l = open(payors_l_full_path, 'w', encoding='utf-8')
        f_payor_m = open(payors_m_full_path, 'w', encoding='utf-8')
        f_payor_n = open(payors_n_full_path, 'w', encoding='utf-8')
        f_payor_o = open(payors_o_full_path, 'w', encoding='utf-8')
        f_payor_p = open(payors_p_full_path, 'w', encoding='utf-8')
        f_payor_q = open(payors_q_full_path, 'w', encoding='utf-8')
        f_payor_r = open(payors_r_full_path, 'w', encoding='utf-8')
        f_payor_s = open(payors_s_full_path, 'w', encoding='utf-8')
        f_payor_t = open(payors_t_full_path, 'w', encoding='utf-8')
        f_payor_u = open(payors_u_full_path, 'w', encoding='utf-8')
        f_payor_v = open(payors_v_full_path, 'w', encoding='utf-8')
        f_payor_w = open(payors_w_full_path, 'w', encoding='utf-8')
        f_payor_x = open(payors_x_full_path, 'w', encoding='utf-8')
        f_payor_y = open(payors_y_full_path, 'w', encoding='utf-8')
        f_payor_z = open(payors_z_full_path, 'w', encoding='utf-8')

       
        
        f_payor_other.write('# Contribution Payors' + '\n') 
        f_payor_other.write('## Other' + '\n') 
        f_payor_other.write('\n')         
        f_payor_a.write('# Contribution Payors' + '\n') 
        f_payor_a.write('## A' + '\n') 
        f_payor_a.write('\n')
        f_payor_b.write('# Contribution Payors' + '\n') 
        f_payor_b.write('## B' + '\n') 
        f_payor_b.write('\n')
        f_payor_c.write('# Contribution Payors' + '\n') 
        f_payor_c.write('## C' + '\n') 
        f_payor_c.write('\n')
        f_payor_d.write('# Contribution Payors' + '\n') 
        f_payor_d.write('## D' + '\n') 
        f_payor_d.write('\n')
        f_payor_e.write('# Contribution Payors' + '\n') 
        f_payor_e.write('## E' + '\n') 
        f_payor_e.write('\n')
        f_payor_f.write('# Contribution Payors' + '\n') 
        f_payor_f.write('## F' + '\n') 
        f_payor_f.write('\n')
        f_payor_g.write('# Contribution Payors' + '\n') 
        f_payor_g.write('## G' + '\n') 
        f_payor_g.write('\n')
        f_payor_h.write('# Contribution Payors' + '\n') 
        f_payor_h.write('## H' + '\n') 
        f_payor_h.write('\n')
        f_payor_i.write('# Contribution Payors' + '\n') 
        f_payor_i.write('## I' + '\n') 
        f_payor_i.write('\n')
        f_payor_j.write('# Contribution Payors' + '\n') 
        f_payor_j.write('## J' + '\n') 
        f_payor_j.write('\n')
        f_payor_k.write('# Contribution Payors' + '\n') 
        f_payor_k.write('## K' + '\n') 
        f_payor_k.write('\n')
        f_payor_l.write('# Contribution Payors' + '\n') 
        f_payor_l.write('## L' + '\n') 
        f_payor_l.write('\n')
        f_payor_m.write('# Contribution Payors' + '\n') 
        f_payor_m.write('## M' + '\n') 
        f_payor_m.write('\n')
        f_payor_n.write('# Contribution Payors' + '\n') 
        f_payor_n.write('## N' + '\n') 
        f_payor_n.write('\n')
        f_payor_o.write('# Contribution Payors' + '\n') 
        f_payor_o.write('## O' + '\n') 
        f_payor_o.write('\n')
        f_payor_p.write('# Contribution Payors' + '\n') 
        f_payor_p.write('## P' + '\n') 
        f_payor_p.write('\n')
        f_payor_q.write('# Contribution Payors' + '\n') 
        f_payor_q.write('## Q' + '\n') 
        f_payor_q.write('\n')
        f_payor_r.write('# Contribution Payors' + '\n') 
        f_payor_r.write('## R' + '\n') 
        f_payor_r.write('\n')
        f_payor_s.write('# Contribution Payors' + '\n') 
        f_payor_s.write('## S' + '\n') 
        f_payor_s.write('\n')
        f_payor_t.write('# Contribution Payors' + '\n') 
        f_payor_t.write('## T' + '\n') 
        f_payor_t.write('\n')
        f_payor_u.write('# Contribution Payors' + '\n') 
        f_payor_u.write('## U' + '\n') 
        f_payor_u.write('\n')
        f_payor_v.write('# Contribution Payors' + '\n') 
        f_payor_v.write('## V' + '\n') 
        f_payor_v.write('\n')
        f_payor_w.write('# Contribution Payors' + '\n') 
        f_payor_w.write('## W' + '\n') 
        f_payor_w.write('\n')
        f_payor_x.write('# Contribution Payors' + '\n') 
        f_payor_x.write('## X' + '\n') 
        f_payor_x.write('\n')
        f_payor_y.write('# Contribution Payors' + '\n') 
        f_payor_y.write('## Y' + '\n') 
        f_payor_y.write('\n')
        f_payor_z.write('# Contribution Payors' + '\n') 
        f_payor_z.write('## Z' + '\n') 
        f_payor_z.write('\n')
        
        
                                                                                                                                                                                                                         
             
             
        for payor in self.payors:
            pchar = payor.payor_name[:1]
            # BUILD HEADER AND TABLE
            x = BuildAPayorSingleFile(payor_object = payor)
            
            md_payor_head = x.build_md_payor_hdr()
            payor_table = x.build_payor_table() 
            if pchar.isalpha():
                if pchar.lower() == 'a':
                    f_payor_a.write('\n')
                    f_payor_a.write(md_payor_head)
                    f_payor_a.write('\n')
                    f_payor_a.write(payor_table)
                    f_payor_a.write('\n')    
                
                if pchar.lower() == 'b':
                    f_payor_b.write('\n')
                    f_payor_b.write(md_payor_head)
                    f_payor_b.write('\n')
                    f_payor_b.write(payor_table)
                    f_payor_b.write('\n')                                                
                if pchar.lower() == 'c':
                    f_payor_c.write('\n')
                    f_payor_c.write(md_payor_head)
                    f_payor_c.write('\n')
                    f_payor_c.write(payor_table)
                    f_payor_c.write('\n')                                                
                if pchar.lower() == 'd':
                    f_payor_d.write('\n')
                    f_payor_d.write(md_payor_head)
                    f_payor_d.write('\n')
                    f_payor_d.write(payor_table)
                    f_payor_d.write('\n')                                                
                if pchar.lower() == 'e':
                    f_payor_e.write('\n')
                    f_payor_e.write(md_payor_head)
                    f_payor_e.write('\n')
                    f_payor_e.write(payor_table)
                    f_payor_e.write('\n')                                                
                if pchar.lower() == 'f':
                    f_payor_f.write('\n')
                    f_payor_f.write(md_payor_head)
                    f_payor_f.write('\n')
                    f_payor_f.write(payor_table)
                    f_payor_f.write('\n')                                                
                if pchar.lower() == 'g':
                    f_payor_g.write('\n')
                    f_payor_g.write(md_payor_head)
                    f_payor_g.write('\n')
                    f_payor_g.write(payor_table)
                    f_payor_g.write('\n')                                                
                if pchar.lower() == 'h':
                    f_payor_h.write('\n')
                    f_payor_h.write(md_payor_head)
                    f_payor_h.write('\n')
                    f_payor_h.write(payor_table)
                    f_payor_h.write('\n')                                                
                if pchar.lower() == 'i':
                    f_payor_i.write('\n')
                    f_payor_i.write(md_payor_head)
                    f_payor_i.write('\n')
                    f_payor_i.write(payor_table)
                    f_payor_i.write('\n')                                                
                if pchar.lower() == 'j':
                    f_payor_j.write('\n')
                    f_payor_j.write(md_payor_head)
                    f_payor_j.write('\n')
                    f_payor_j.write(payor_table)
                    f_payor_j.write('\n')                                                
                if pchar.lower() == 'k':
                    f_payor_k.write('\n')
                    f_payor_k.write(md_payor_head)
                    f_payor_k.write('\n')
                    f_payor_k.write(payor_table)
                    f_payor_k.write('\n')                                                
                if pchar.lower() == 'l':
                    f_payor_l.write('\n')
                    f_payor_l.write(md_payor_head)
                    f_payor_l.write('\n')
                    f_payor_l.write(payor_table)
                    f_payor_l.write('\n')                                                
                if pchar.lower() == 'm':
                    f_payor_m.write('\n')
                    f_payor_m.write(md_payor_head)
                    f_payor_m.write('\n')
                    f_payor_m.write(payor_table)
                    f_payor_m.write('\n')                                                
                if pchar.lower() == 'n':
                    f_payor_n.write('\n')
                    f_payor_n.write(md_payor_head)
                    f_payor_n.write('\n')
                    f_payor_n.write(payor_table)
                    f_payor_n.write('\n')                                                
                if pchar.lower() == 'o':
                    f_payor_o.write('\n')
                    f_payor_o.write(md_payor_head)
                    f_payor_o.write('\n')
                    f_payor_o.write(payor_table)
                    f_payor_o.write('\n')                                                
                if pchar.lower() == 'p':
                    f_payor_p.write('\n')
                    f_payor_p.write(md_payor_head)
                    f_payor_p.write('\n')
                    f_payor_p.write(payor_table)
                    f_payor_p.write('\n')                                                
                if pchar.lower() == 'q':
                    f_payor_q.write('\n')
                    f_payor_q.write(md_payor_head)
                    f_payor_q.write('\n')
                    f_payor_q.write(payor_table)
                    f_payor_q.write('\n')                                                
                if pchar.lower() == 'r':
                    f_payor_r.write('\n')
                    f_payor_r.write(md_payor_head)
                    f_payor_r.write('\n')
                    f_payor_r.write(payor_table)
                    f_payor_r.write('\n')                                                
                if pchar.lower() == 's':
                    f_payor_s.write('\n')
                    f_payor_s.write(md_payor_head)
                    f_payor_s.write('\n')
                    f_payor_s.write(payor_table)
                    f_payor_s.write('\n')                                                
                if pchar.lower() == 't':
                    f_payor_t.write('\n')
                    f_payor_t.write(md_payor_head)
                    f_payor_t.write('\n')
                    f_payor_t.write(payor_table)
                    f_payor_t.write('\n')                                                
                if pchar.lower() == 'u':
                    f_payor_t.write('\n')
                    f_payor_t.write(md_payor_head)
                    f_payor_t.write('\n')
                    f_payor_t.write(payor_table)
                    f_payor_t.write('\n')                                                
                if pchar.lower() == 'v':
                    f_payor_v.write('\n')
                    f_payor_v.write(md_payor_head)
                    f_payor_v.write('\n')
                    f_payor_v.write(payor_table)
                    f_payor_v.write('\n')                                                
                if pchar.lower() == 'w':
                    f_payor_w.write('\n')
                    f_payor_w.write(md_payor_head)
                    f_payor_w.write('\n')
                    f_payor_w.write(payor_table)
                    f_payor_w.write('\n')                                                
                if pchar.lower() == 'x':
                    f_payor_x.write('\n')
                    f_payor_x.write(md_payor_head)
                    f_payor_x.write('\n')
                    f_payor_x.write(payor_table)
                    f_payor_x.write('\n')                                                
                if pchar.lower() == 'y':
                    f_payor_y.write('\n')
                    f_payor_y.write(md_payor_head)
                    f_payor_y.write('\n')
                    f_payor_y.write(payor_table)
                    f_payor_y.write('\n')                                                
                if pchar.lower() == 'z':
                    f_payor_z.write('\n')
                    f_payor_z.write(md_payor_head)
                    f_payor_z.write('\n')
                    f_payor_z.write(payor_table)
                    f_payor_z.write('\n')                                                
                                                                 
                
            else:
                f_payor_other.write('\n')
                f_payor_other.write(md_payor_head)
                f_payor_other.write('\n')
                f_payor_other.write(payor_table)
                f_payor_other.write('\n')                  



   
def remove_files(dir):
    for files in os.listdir(dir):
        path = os.path.join(dir, files)
        try:
            shutil.rmtree(path)
        except OSError:
            os.remove(path)     
            
            
def remove_single_file():
    file = PAYORS_SINGLE_FILE_OUTPUT_PATH + '\\' + 'payors.md'
    if os.path.exists(file):
        os.remove(file) 
         
    
def cleanup_dirs():  
    remove_files(OUTPUT_PATH_PAYORS) 
    # remove_files(OUTPUT_PATH_EXP)
          

def main_multi_file():
    cleanup_dirs()
    x = BuildEachPayorSingleFile()
    x.build_each_payor_by_name_multi()        
    remove_single_file()
    
def new_multi_file():
    cleanup_dirs()
    x = BuildEachPayorSingleFileNew()
    x.build_each_payor()        
    # remove_single_file()    

if __name__ == "__main__":
    # cleanup_dirs()
    main_multi_file()
    # remove_single_file()
    # new_multi_file()
   