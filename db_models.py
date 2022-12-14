from sqlmodel import  SQLModel, Field, Column, VARCHAR, DateTime
from typing import Optional
from datetime import date, datetime, time, timedelta
from sqlalchemy import BigInteger, inspect
from rich import inspect
from db_config import DbConfig

engine = db_engine = DbConfig.get_central_engine()

class PppData(SQLModel, table=True): 
    __tablename__ = "ppp_data" 
    index: Optional[int] = Field(default=None, primary_key=True)   
    loannumber: int = None 
    dateapproved: str = None
    sbaofficecode: int = None 
    processingmethod: str = None
    borrowername: str = None
    borroweraddress: str = None
    borrowercity: str = None
    borrowerstate: str = None
    borrowerzip: str = None
    loanstatusdate: str = None
    loanstatus: str = None
    term: int = None 
    sbaguarantypercentage: int = None 
    initialapprovalamount: str = None
    currentapprovalamount: str = None
    undisbursedamount: str = None
    franchisename: str = None
    servicinglenderlocationid: int = None 
    servicinglendername: str = None
    servicinglenderaddress: str = None
    servicinglendercity: str = None
    servicinglenderstate: str = None
    servicinglenderzip: str = None
    ruralurbanindicator: str = None
    hubzoneindicator: str = None
    lmiindicator: str = None
    businessagedescription: str = None
    projectcity: str = None
    projectcountyname: str = None
    projectstate: str = None
    projectzip: str = None
    cd: str = None
    jobsreported: int = None 
    naicscode: str = None
    race: str = None
    ethnicity: str = None
    utilities_proceed: float = None 
    payroll_proceed: str = None
    mortgage_interest_proceed: str = None
    rent_proceed: str = None
    refinance_eidl_proceed: str = None
    health_care_proceed: str = None
    debt_interest_proceed: str = None
    businesstype: str = None
    originatinglenderlocationid: int = None 
    originatinglender: str = None
    originatinglendercity: str = None
    originatinglenderstate: str = None
    gender: str = None
    veteran: str = None
    nonprofit: str = None
    forgivenessamount: float = None 
    forgivenessdate: str = None


class LogExceptions(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    api_codes: str = None
    api_errors: str = None
    api_messages: str = None
    response: str = None
    status: str = None
    in_reply_to_status_id: str = None
    error_dt: datetime = Field(default=datetime.now())

       
class ErrorLog(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    error_message: str = None
    error_dt: datetime = Field(default=datetime.now())



class Candidate(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True) 
    candidate_name: str
    create_dt: datetime = Field(default=datetime.now())
    update_dt: datetime = None       
         

class Contribution(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    receipt_id: int
    org_id: int
    filer_type: str
    filer_type_short: str = None
    filer_name: str
    candidate_name: str = None
    contribution_type: str = None
    other_funds_type: str = None
    receipt_date: date = None
    receipt_amount: float
    description: str = None

    original_payor_type: str = None    
    original_payor_name: str = None
    original_first_name: str = None
    original_middle_name: str = None
    original_suffix: str = None   
   
    payor_type: str = None
    payor_type_short: str = None       
    payor_name: str = None
    last_name: str = None
    first_name: str = None
    middle_name: str = None
    suffix: str = None
    address_1: str = None
    address_2: str = None
    city: str = None
    state: str = None
    zip: str = None
    filed_date: date = None
    amended: str = None
    employer: str = None
    occupation: str = None
    create_dt: datetime = None
    update_dt: datetime = None
    delete_flag: int = None
    delete_dt: datetime = None
    tweet_sent: int = 0
    tweet_dt: datetime = None
    tweet_id: str = None
    tweet_message: str = None   
    tweet_message_update_dt: datetime = None
    tweet_sent_text: str = None
    replied_to_status_id: str = None 
    create_dt: datetime = Field(default=datetime.now())
    update_dt: datetime = None   
    bot_retweeted_id: str = None    
    bot_retweeted_dt: datetime = None
    payor_id: int = None
    filer_markdown_file: str = None     
    payor_markdown_file: str = None 
    payor_folder: str = None          

         
                      
# class Expenditure(SQLModel, table=True):
#     id: Optional[int] = Field(default=None, primary_key=True)
#     expenditure_id: int
#     org_id: int
#     filer_type: str  
#     filer_type_short: str = None
#     filer_name: str
#     candidate_name: str = None
#     expenditure_type: str = None
#     expenditure_sub_type: str = None
#     expenditure_date: date = None
#     expenditure_amount: float = None
#     description: str = None
    
#     original_payee_type: str = None    
#     original_payee_name: str = None
#     original_first_name: str = None
#     original_middle_name: str = None
#     original_suffix: str = None
    
#     payee_type: str = None
#     payee_type_short: str = None    
#     payee_name: str = None
#     last_name: str = None
#     first_name: str = None
#     middle_name: str = None
#     suffix: str = None
    
#     address_1: str = None
#     address_2: str = None
#     city: str = None
#     state: str = None
#     zip: str = None
#     filed_date: date = None
#     support_or_oppose: str = None
#     candidate_name_or_ballot_issue: str = None
#     jurisdiction_office_district_or_ballot_description: str = None
#     amended: str = None
#     employer: str = None
#     occupation: str = None
#     principal_place_of_business: str = None
#     create_dt: datetime = None
#     update_dt: datetime = None
#     delete_flag: int = None
#     delete_dt: datetime = None
#     tweet_sent: int = 0
#     tweet_dt: datetime = None
#     tweet_id: str = None
#     tweet_message: str = None
#     tweet_message_update_dt: datetime = None
#     tweet_sent_text: str = None
#     replied_to_status_id: str = None
#     create_dt: datetime = Field(default=datetime.now())
#     update_dt: datetime = None   
#     bot_retweeted_id: str = None    
#     bot_retweeted_dt: datetime = None 
#     payee_id: int = None       
         
class Expenditure(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    expenditure_id: int
    org_id: int
    filer_type: str  
    filer_type_short: str = None
    filer_name: str
    candidate_name: str = None
    expenditure_type: str = None
    expenditure_sub_type: str = None
    expenditure_date: date = None
    expenditure_amount: float = None
    description: str = None
    
    original_payee_type: str = None    
    original_payee_name: str = None
    original_first_name: str = None
    original_middle_name: str = None
    original_suffix: str = None
    
    payee_type: str = None
    payee_type_short: str = None    
    payee_name: str = None
    last_name: str = None
    first_name: str = None
    middle_name: str = None
    suffix: str = None
    
    address_1: str = None
    address_2: str = None
    city: str = None
    state: str = None
    zip: str = None
    filed_date: date = None
    support_or_oppose: str = None
    candidate_name_or_ballot_issue: str = None
    jurisdiction_office_district_or_ballot_description: str = None
    amended: str = None
    employer: str = None
    occupation: str = None
    principal_place_of_business: str = None
    create_dt: datetime = None
    update_dt: datetime = None
    delete_flag: int = None
    delete_dt: datetime = None
    tweet_sent: int = 0
    tweet_dt: datetime = None
    tweet_id: str = None
    tweet_message: str = None
    tweet_message_update_dt: datetime = None
    tweet_sent_text: str = None
    replied_to_status_id: str = None
    create_dt: datetime = Field(default=datetime.now())
    update_dt: datetime = None   
    bot_retweeted_id: str = None    
    bot_retweeted_dt: datetime = None  
    payee_id: int = None 
    filer_markdown_file: str = None     
    payee_markdown_file: str = None 
    payee_folder: str = None             
    

    
    
         
class ExpenditureFiler(SQLModel, table=True): 
    id: Optional[int] = Field(default=None, primary_key=True)   
    org_id: int 
    # org_id: int
    filer_type: str
    filer_type_short: str = None    
    filer_name: str
    filer_short_name: str = None
    expenditure_count: int = None       
    # contribution_count: int = None
    tweet_header_id: str = None
    tweet_header_text: str = None
    text_update_dt: datetime = None  
    text_tweeted_dt: datetime = None 
    create_dt: datetime = Field(default=datetime.now())
    update_dt: datetime = None   
    expenditure_total_amount: float = None        
    
    
class ContributionFiler(SQLModel, table=True): 
    id: Optional[int] = Field(default=None, primary_key=True)   
    org_id: int 
    # org_id: int
    filer_type: str
    filer_type_short: str = None    
    filer_name: str
    filer_short_name: str = None
    receipt_count: int = None       
    # contribution_count: int = None
    tweet_header_id: str = None
    tweet_header_text: str = None
    text_update_dt: datetime = None  
    text_tweeted_dt: datetime = None 
    create_dt: datetime = Field(default=datetime.now())
    update_dt: datetime = None   
    receipt_total_amount: float = None                       
                 
 
# class Filer(SQLModel, table=True): 
#     id: Optional[int] = Field(default=None, primary_key=True)   
#     org_id: int 
#     # org_id: int
#     filer_type: str
#     filer_type_short: str = None    
#     filer_name: str
#     filer_short_name: str = None
#     expenditure_count: int = None
#     receipt_count: int = None
#     tweet_header_id: str = None
#     tweet_header_text: str = None
#     text_update_dt: datetime = None    
#     create_dt: datetime = Field(default=datetime.now())
#     update_dt: datetime = None 
#     receipt_total_amount: float = None                  
#     expenditure_total_amount: float = None  
    

class Filer(SQLModel, table=True): 
    id: Optional[int] = Field(default=None, primary_key=True)   
    org_id: int 
    # org_id: int
    filer_type: str
    filer_type_short: str = None    
    filer_name: str
    filer_short_name: str = None
    expenditure_count: int = None
    receipt_count: int = None
    tweet_header_id: str = None
    tweet_header_text: str = None
    text_update_dt: datetime = None    
    create_dt: datetime = Field(default=datetime.now())
    update_dt: datetime = None 
    receipt_total_amount: float = None                  
    expenditure_total_amount: float = None  
    markdown_file: str = None    
    
 
class Payor(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    original_payor_type: str = None 
    original_payor_name: str = None 
    original_first_name: str = None
    original_middle_name: str = None
    original_suffix: str = None
    payor_type: str = None
    payor_type_short: str = None
    payor_name: str = Field(default=None)    
    last_name: str = None
    first_name: str = None
    middle_name: str = None
    suffix: str = None
    address_1: str = None
    address_2: str = None
    city: str = None
    state: str = None
    zip: str = None  
    expenditure_payee_count: int = None
    expenditure_payee_total_amount: float = None          
    receipt_payor_count: int = None
    receipt_payor_total_amount: float = None     
    create_dt: datetime = Field(default=datetime.now())
    update_dt: datetime = None 
    markdown_file: str = None
    city_state: str = None
    payor_folder: str = None  
                    
    
# class Payee(SQLModel, table=True):
#     id: Optional[int] = Field(default=None, primary_key=True) 
#     original_payee_type: str = None
#     original_payee_name: str = None
#     original_first_name: str = None
#     original_middle_name: str = None
#     original_suffix: str = None
#     payee_type: str = None
#     payee_type_short: str = None
#     payee_name: str = None  
#     # unique, the sqlalchemy way
#     # name: str =Field(sa_column=Column("payee_name", VARCHAR, unique=True))  
#     last_name: str = None
#     first_name: str = None
#     middle_name: str = None
#     suffix: str = None
#     address_1: str = None
#     address_2: str = None
#     city: str = None
#     state: str = None
#     zip: str = None  
#     expenditure_payee_count: int = None
#     expenditure_payee_total_amount: float = None 
#     receipt_payor_count: int = None
#     receipt_payor_total_amount: float = None          
#     create_dt: datetime = Field(default=datetime.now())
#     update_dt: datetime = None    
   
class Payee(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True) 
    original_payee_type: str = None
    original_payee_name: str = None
    original_first_name: str = None
    original_middle_name: str = None
    original_suffix: str = None
    payee_type: str = None
    payee_type_short: str = None
    payee_name: str = None  
    # unique, the sqlalchemy way
    # name: str =Field(sa_column=Column("payee_name", VARCHAR, unique=True))  
    last_name: str = None
    first_name: str = None
    middle_name: str = None
    suffix: str = None
    address_1: str = None
    address_2: str = None
    city: str = None
    state: str = None
    zip: str = None  
    expenditure_payee_count: int = None
    expenditure_payee_total_amount: float = None 
    receipt_payor_count: int = None
    receipt_payor_total_amount: float = None          
    create_dt: datetime = Field(default=datetime.now())
    update_dt: datetime = None
    markdown_file: str = None
    city_state: str = None
    payee_folder: str = None  
                     
    
# class StageContributions(SQLModel, table=True):
#     __tablename__ = "stage_contributions"   
#     index: Optional[int] = Field(default=None, primary_key=True) 
#     receipt_id: int = None 
#     org_id: int = None
#     filer_type: str = None
#     filer_name: str = None
#     candidate_name: str = None
#     receipt_transaction_contribution_type: str = None
#     other_funds_type: str = None
#     receipt_date: str = None
#     receipt_amount: float = None 
#     description: str = None
#     contributor_or_transaction_source_type: str = None
#     contributor_or_source_name_individual_last_name: str = None
#     first_name: str = None
#     middle_name: str = None
#     suffix: str = None
#     address_1: str = None
#     address_2: str = None
#     city: str = None
#     state: str = None
#     zip: str = None
#     filed_date: str = None
#     amended: str = None
#     employer: str = None
#     occupation: str = None



# class StageExpenditures(SQLModel, table=True):
#     __tablename__ = "stage_expenditures"  
#     index: Optional[int] = Field(default=None, primary_key=True) 
#     expenditure_id: int = None
#     org_id: int = None
#     filer_type: str = None 
#     filer_name: str = None
#     candidate_name: str = None
#     expenditure_transaction_type: str = None
#     expenditure_sub_type: str = None
#     expenditure_date: str = None
#     expenditure_amount: float = None
#     description: str = None
#     payee_or_recipient_or_in_kind_contributor_type: str = None
#     payee_or_recipient_or_in_kind_contributor_name: str = None
#     first_name: str = None
#     middle_name: str = None
#     suffix: str = None
#     address_1: str = None
#     address_2: str = None
#     city: str = None
#     state: str = None
#     zip: str = None
#     filed_date: str = None
#     support_or_oppose: str = None
#     candidate_name_or_ballot_issue: str = None
#     jurisdiction_office_district_or_ballot_description: str = None
#     amended: str = None
#     employer: str = None
#     occupation: str = None
#     principal_place_of_business: str = None

  
def main():    
    SQLModel.metadata.create_all(engine) 


if __name__ == "__main__":
    main() 