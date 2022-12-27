import markdown_refresh_filers as flrs
import markdown_refresh_payors as pyrs
import markdown_refresh_payees as pyes
import markdown_refresh_top_lists as top
import time
from datetime import datetime
import markdown_refresh_directories as dirs

SITE_DIR = dirs.SITE_DIR

# datetime object containing current date and time
now = datetime.now()
 
# print("now =", now)

# dd/mm/YY H:M:S
DT_STRING = now.strftime("%Y-%m-%d %H:%M:%S")
# print("date and time =", dt_string)	


def update_site_index():

    try:
        with open('stub_site_index.md', 'r') as tempfile :
            filedata = tempfile.read()
    except Exception as e:
        raise        

    try:
        filedata = filedata.replace('@LastRefresh',DT_STRING)                
    except Exception as e:
        raise
    time.sleep(10)

    with open(f'{SITE_DIR}\\docs\index.md', 'w') as outputfile:
        outputfile.write(filedata)

def update_yaml_file():
    try:
        with open('rcp_yaml.txt','r') as rcp_file:
            rcp_yaml = rcp_file.read()
    except Exception as e:
        raise
    
    try:    
        with open('exp_yaml.txt','r') as exp_file:
            exp_yaml = exp_file.read() 
    except Exception as e:
        raise  

    try:
        with open('stub.yml', 'r') as tempfile :
            filedata = tempfile.read()
    except Exception as e:
        raise        

    try:
        filedata = filedata.replace('@ReceiptsStub',rcp_yaml)
        # print(rcp_yaml)
    except Exception as e:
        raise
    time.sleep(10)
    
    try:
        filedata = filedata.replace('@ExpendituresStub',exp_yaml)
    except Exception as e:
        raise
    time.sleep(10)
    
    with open(f'{SITE_DIR}\\mkdocs.yml', 'w') as outputfile:
        outputfile.write(filedata)




def cleanup_dirs():
    flrs.cleanup_dirs()
    pyrs.cleanup_dirs()
    pyes.cleanup_dirs()

def cleanup_single_file():
    flrs.cleanup_dirs()
    pyrs.remove_single_file()
    pyes.remove_single_file()
    
    
def main_multi_file():
    print('doing filers...')    
    flrs.main_by_name_multi()
    
    print('doing payors...')    
    pyrs.main_multi_file()
    
    print('doing payees...')    
    pyes.main_multi_file()
    
    print('doing top lists...')    
    top.main()    
    
    print('doing yaml file...')    
    update_yaml_file() 
    
    print('doing site index...')    
    update_site_index()            
    
    print('done with refresh_main')    
    
if __name__ == "__main__":
    main_multi_file()
    # update_site_index()

    
    
# def main_by_name_sample():
#     flrs.main_by_name_sample()
#     pyrs.main_by_name_sample()
#     pyes.main_by_name_sample()
#     top.main()

#     update_yaml_file()    
    
# def main_by_name_select():
#     flrs.main_by_name_select()
#     pyrs.main_by_name_sample()
#     pyes.main_by_name_sample()
#     top.main()

#     update_yaml_file()    
    
    
    
# def main_by_name():
#     flrs.main_by_name()
#     pyrs.main_by_name()
#     pyes.main_by_name()
#     top.main()    

#     update_yaml_file()     
    
    
# def main_single_file():
#     flrs.main_by_name()
#     pyrs.main_single_file()
#     pyes.main_single_file()
    
#     top.main()    

#     update_yaml_file() 
#     update_site_index()       

# def update_site_index():

#     try:
#         with open('stub_site_index.md', 'r') as tempfile :
#             filedata = tempfile.read()
#     except Exception as e:
#         raise        
#     # print(filedata)
#     try:
#         filedata = filedata.replace('@LastRefresh',DT_STRING)
#         # print(rcp_yaml)
#     except Exception as e:
#         raise
#     time.sleep(10)
#     # try:
#     #     filedata = filedata.replace('@ExpendituresStub',exp_yaml)
#     # except Exception as e:
#     #     raise
#     # time.sleep(10)    
#     with open('datanebraska\\docs\index.md', 'w') as outputfile:
#         outputfile.write(filedata)

# def update_yaml_file():
#     try:
#         with open('rcp_yaml.txt','r') as rcp_file:
#             rcp_yaml = rcp_file.read()
#     except Exception as e:
#         raise
#     # print(rcp_yaml)
    
#     try:    
#         with open('exp_yaml.txt','r') as exp_file:
#             exp_yaml = exp_file.read() 
#     except Exception as e:
#         raise  
#     # print(exp_yaml)   
    
#     # try:
#     #     with open('payors_yaml.txt', 'r') as payors_file:
#     #         payors_yaml = payors_file.read()
#     # except Exception as e:
#     #     raise         
#     # # print(payors_yaml)
#     # try:    
#     #     with open('payees_yaml.txt', 'r') as payees_file:
#     #         payees_yaml = payees_file.read()              
#     # except Exception as e:
#     #     raise    
#     # print(payees_yaml.txt)
#     try:
#         with open('stub.yml', 'r') as tempfile :
#             filedata = tempfile.read()
#     except Exception as e:
#         raise        
#     # print(filedata)
#     try:
#         filedata = filedata.replace('@ReceiptsStub',rcp_yaml)
#         # print(rcp_yaml)
#     except Exception as e:
#         raise
#     time.sleep(10)
#     try:
#         filedata = filedata.replace('@ExpendituresStub',exp_yaml)
#     except Exception as e:
#         raise
#     time.sleep(10)
#     # try:
#     #     filedata = filedata.replace('@PayorsStub',payors_yaml)
#     # except Exception as e:
#     #     raise
#     # time.sleep(10)
#     # try:
#     #     filedata = filedata.replace('@PayeesStub',payees_yaml)
#     # except Exception as e:
#     #     raise
#     # time.sleep(10)
    
#     with open('datanebraska\\mkdocs.yml', 'w') as outputfile:
#         outputfile.write(filedata)

# # def main():
# #     flrs.main()
# #     pyrs.main()
# #     pyes.main()

# #     update_yaml_file()    
