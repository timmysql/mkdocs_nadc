from sqlmodel import  SQLModel, Field, Column, VARCHAR, DateTime, ARRAY
from typing import Optional
from datetime import date, datetime, time, timedelta
from sqlalchemy import BigInteger, inspect, Integer, String
from rich import inspect
from db_config import DbConfig
from typing import Optional, List, Union
from dataclasses import dataclass, field, MISSING


engine = db_engine = DbConfig.get_central_engine()

class FecLoadLog(SQLModel, table=True):
    __tablename__ = 'fec_load_log'
    id: Optional[int] = Field(default=None, primary_key=True)     
    committee_id: Optional[str]
    page: int
    num_pages: int 
    last_index: Optional[str]
    last_crd: Optional[str] 
    per_page: int
    count: int

class FecCommittees(SQLModel, table=True):
    __tablename__ = "fec_committees"  
    affiliated_committee_name: Optional[str] = Field(default=None) 
    candidate_ids: List[str]
    committee_id: str = Field(default=None, primary_key=True)
    committee_type: str
    committee_type_full: str
    cycles: List[int] = Field(sa_column=Column(ARRAY(String)))
    designation: Optional[str]
    designation_full: Optional[str]
    filing_frequency: str
    first_f1_date: Optional[str]
    first_file_date: str
    last_f1_date: Optional[str]
    last_file_date: str
    name: str
    organization_type: Optional[str]
    organization_type_full: Optional[str]
    party: Optional[str] = Field(default=None) 
    party_full: Optional[str] = Field(default=None) 
    sponsor_candidate_ids: Optional[List[str]] = Field(sa_column=Column(ARRAY(String)))    
    sponsor_candidate_list: Optional[List[str]] = Field(sa_column=Column(ARRAY(String)))   
    # sponsor_candidate_list: List[Dict[str, str]] = Field(sa_column=Column(ARRAY(String)))  
    state: str
    treasurer_name: Optional[str]

class FecCandidates(SQLModel, table=True):
    __tablename__ = "fec_candidates"  
    active_through: int
    candidate_id: str = Field(default=None, primary_key=True)
    candidate_inactive: bool
    candidate_status: str
    cycles: List[int] = Field(sa_column=Column(ARRAY(Integer)))
    district: str
    district_number: int
    election_districts: Optional[List[str]] = Field(sa_column=Column(ARRAY(String)))    
    election_years: List[int] = Field(sa_column=Column(ARRAY(Integer)))
    federal_funds_flag: bool
    first_file_date: Optional[str] = Field(default=None) 
    flags: Optional[str]
    has_raised_funds: bool
    inactive_election_years: List[int] = Field(sa_column=Column(ARRAY(Integer)))
    incumbent_challenge: Optional[str]
    incumbent_challenge_full: Optional[str]
    last_f2_date: Optional[str] = Field(default=None) 
    last_file_date: Optional[str] = Field(default=None) 
    load_date: Optional[str] = Field(default=None) 
    name: str
    office:str
    office_full: str
    party: Optional[str]
    party_full: Optional[str]
    state: str  


class ScheduleB(SQLModel, table=True): 
    __tablename__ = "fec_schedule_b" 
    # id: Optional[int] = Field(default=None, primary_key=True)     
    
    amendment_indicator: Optional[str]
    amendment_indicator_desc: Optional[str]
    back_reference_schedule_id: Optional[str]
    back_reference_transaction_id: Optional[str]
    beneficiary_committee_name: Optional[str]
    candidate_first_name: Optional[str]
    candidate_id: Optional[str]
    candidate_last_name: Optional[str]
    candidate_middle_name: Optional[str]
    candidate_name: Optional[str]
    candidate_office: Optional[str]
    candidate_office_description: Optional[str]
    candidate_office_district: Optional[str]
    candidate_office_state: Optional[str]
    candidate_office_state_full: Optional[str]
    candidate_prefix: Optional[str]
    candidate_suffix: Optional[str]
    category_code: Optional[str]
    category_code_full: Optional[str]
    comm_dt: Optional[str]
    committee: Optional[str]
    committee_id: Optional[str]
    conduit_committee_city: Optional[str]
    conduit_committee_name: Optional[str]
    conduit_committee_state: Optional[str]
    conduit_committee_street1: Optional[str]
    conduit_committee_street2: Optional[str]
    conduit_committee_zip: Optional[int]
    disbursement_amount: Optional[float]
    disbursement_date: Optional[str]
    disbursement_description: Optional[str]
    disbursement_purpose_category: Optional[str]
    disbursement_type: Optional[str]
    disbursement_type_description: Optional[str]
    election_type: Optional[str]
    election_type_description: Optional[str]
    entity_type: Optional[str]
    entity_type_desc: Optional[str]
    fec_election_type_desc: Optional[str]
    fec_election_year: Optional[str]
    file_number: Optional[int]
    filing_form: Optional[str]
    image_number: Optional[str]
    line_number: Optional[str]
    line_number_laber: Optional[str]
    link_id: Optional[str]  = Field(default=None, primary_key=True) 
    load_date: Optional[str]
    memo_code: Optional[str]
    memo_code_full: Optional[str]
    memo_text: Optional[str]
    memoed_subtotal: Optional[bool]
    national_committee_nonfederal_account: Optional[str]
    original_sub_id: Optional[str]
    payee_employer: Optional[str]
    payee_first_name: Optional[str]
    payee_last_name: Optional[str]
    payee_middle_name: Optional[str]
    payee_occupation: Optional[str]
    payee_prefix: Optional[str]
    payee_suffix: Optional[str]
    pdf_url: Optional[str]
    recipient_city: Optional[str]
    recipient_committee: Optional[str]
    recipient_committee_id: Optional[str]
    recipient_name: Optional[str]
    recipient_state: Optional[str]
    recipient_zip: Optional[str]
    ref_disp_excess_flg: Optional[str]
    report_type: Optional[str]
    report_year: Optional[int]
    schedule_type: Optional[str]
    schedule_type_full: Optional[str]
    semi_annual_bundled_refund: Optional[float]
    spender_committee_designation: Optional[str]
    spender_committee_org_type: Optional[str]
    sub_id: Optional[str] = Field(default=None, primary_key=True) 
    transaction_id: Optional[str]
    two_year_transaction_period: Optional[int]
    unused_recipient_committee_id: Optional[str]
    


class ScheduleA(SQLModel, table=True): 
    __tablename__ = "fec_schedule_a" 
    # id: Optional[int] = Field(default=None, primary_key=True)     
    amendment_indicator: Optional[str]
    amendment_indicator_desc: Optional[str]
    back_reference_schedule_name: Optional[str]
    back_reference_transaction_id: Optional[str]
    candidate_first_name: Optional[str]
    candidate_id: Optional[str]
    candidate_last_name: Optional[str]
    candidate_middle_name: Optional[str]
    candidate_name: Optional[str]
    candidate_office: Optional[str]
    candidate_office_district: Optional[str]
    candidate_office_full: Optional[str]
    candidate_office_state: Optional[str]
    candidate_office_state_full: Optional[str]
    candidate_prefix: Optional[str]
    candidate_suffix: Optional[str]
    committee: Optional[str]
    committee_id: Optional[str]
    committee_name: Optional[str]
    conduit_committee_city: Optional[str]
    conduit_committee_id: Optional[str]
    conduit_committee_name: Optional[str]
    conduit_committee_state: Optional[str]
    conduit_committee_street1: Optional[str]
    conduit_committee_street2: Optional[str]
    conduit_committee_zip: Optional[int]
    contribution_receipt_amount: Optional[float]
    contribution_receipt_date: Optional[str]
    contributor: Optional[str]
    contributor_aggregate_ytd: Optional[str]
    contributor_city: Optional[str]
    contributor_employer: Optional[str]
    contributor_first_name: Optional[str]
    contributor_id: Optional[str]
    contributor_last_name: Optional[str]
    contributor_middle_name: Optional[str]
    contributor_name: Optional[str]
    contributor_occupation: Optional[str]
    contributor_prefix: Optional[str]
    contributor_state: Optional[str]
    contributor_street_1: Optional[str]
    contributor_street_2: Optional[str]
    contributor_suffix: Optional[str]
    contributor_zip: Optional[str]
    donor_committee_name: Optional[str]
    election_type: Optional[str]
    election_type_full: Optional[str]
    entity_type: Optional[str]
    entity_type_desc: Optional[str]
    fec_election_type_desc: Optional[str]
    fec_election_year: Optional[str]
    file_number: Optional[str]
    filing_form: Optional[str]
    image_number: Optional[str]
    increased_limit: Optional[str]
    is_individual: Optional[bool]
    line_number: Optional[str]
    line_number_label: Optional[str]
    # link_id: Optional[str]
    link_id: Optional[str]  = Field(default=None, primary_key=True) 
    load_date: Optional[str]
    memo_code: Optional[str]
    memo_code_full: Optional[str]
    memo_text: Optional[str]
    memoed_subtotal: bool
    national_committee_nonfederal_account: Optional[str]
    original_sub_id: Optional[str]
    pdf_url: Optional[str]
    receipt_type: Optional[str]
    receipt_type_desc: Optional[str]
    receipt_type_full: Optional[str]
    recipient_committee_designation: Optional[str]
    recipient_committee_org_type: Optional[str]
    recipient_committee_type: Optional[str]
    report_type: Optional[str]
    report_year: Optional[int]
    schedule_type: Optional[str]
    schedule_type_full: Optional[str]
    sub_id: Optional[str] = Field(default=None, primary_key=True) 
    # sub_id: Optional[str]
    transaction_id: Optional[str] 
    two_year_transaction_period: Optional[int]
    unused_contbr_id:  Optional[str]   


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