# from fec_dataclasses import DcScheduleA
from db_models import ScheduleA, ScheduleB
from db_dal_classes import SelectOneFecScheduleB, SelectFecScheduleA, SelectFecCandidates,SelectFecCommittees, SelectOneFecScheduleA
from db_config import DbConfig
from sqlmodel import Field, Session, SQLModel, create_engine, select, or_, insert
engine = db_engine = DbConfig.get_central_engine()
from sqlmodel.sql.expression import Select, SelectOfScalar
import logging    
SelectOfScalar.inherit_cache = True  # type: ignore
Select.inherit_cache = True  # type: ignore     
logging.basicConfig(level=logging.DEBUG)  
from db_models import ScheduleB, FecLoadLog



class InsertScheduleB:
    def __init__(self,dc_object):
        self.dc_object = dc_object
        
    # def check_insert(self):
    #     x = SelectOneFecScheduleB(link_id=self.dc_object.link_id, sub_id=self.dc_object.sub_id)
    #     result = x.select()
    #     if result:
    #         result = True
    #     else:
    #         result = False
    #     return result
        
    def insert(self):
        # if self.check_insert() == False:
            try:
                with Session(engine) as session:
                    schedule_a = ScheduleB(
                            amendment_indicator = self.dc_object.amendment_indicator
                            ,amendment_indicator_desc = self.dc_object.amendment_indicator_desc
                            ,back_reference_schedule_id = self.dc_object.back_reference_schedule_id
                            ,back_reference_transaction_id = self.dc_object.back_reference_transaction_id
                            ,beneficiary_committee_name = self.dc_object.beneficiary_committee_name
                            ,candidate_first_name = self.dc_object.candidate_first_name
                            ,candidate_id = self.dc_object.candidate_id
                            ,candidate_last_name = self.dc_object.candidate_last_name
                            ,candidate_middle_name = self.dc_object.candidate_middle_name
                            ,candidate_name = self.dc_object.candidate_name
                            ,candidate_office = self.dc_object.candidate_office
                            ,candidate_office_description = self.dc_object.candidate_office_description
                            ,candidate_office_district = self.dc_object.candidate_office_district
                            ,candidate_office_state = self.dc_object.candidate_office_state
                            ,candidate_office_state_full = self.dc_object.candidate_office_state_full
                            ,candidate_prefix = self.dc_object.candidate_prefix
                            ,candidate_suffix = self.dc_object.candidate_suffix
                            ,category_code = self.dc_object.category_code
                            ,category_code_full = self.dc_object.category_code_full
                            ,comm_dt = self.dc_object.comm_dt
                            ,committee = self.dc_object.committee
                            ,committee_id = self.dc_object.committee_id
                            ,conduit_committee_city = self.dc_object.conduit_committee_city
                            ,conduit_committee_name = self.dc_object.conduit_committee_name
                            ,conduit_committee_state = self.dc_object.conduit_committee_state
                            ,conduit_committee_street1 = self.dc_object.conduit_committee_street1
                            ,conduit_committee_street2 = self.dc_object.conduit_committee_street2
                            ,conduit_committee_zip = self.dc_object.conduit_committee_zip
                            ,disbursement_amount = self.dc_object.disbursement_amount
                            ,disbursement_date = self.dc_object.disbursement_date
                            ,disbursement_description = self.dc_object.disbursement_description
                            ,disbursement_purpose_category = self.dc_object.disbursement_purpose_category
                            ,disbursement_type = self.dc_object.disbursement_type
                            ,disbursement_type_description = self.dc_object.disbursement_type_description
                            ,election_type = self.dc_object.election_type
                            ,election_type_description = self.dc_object.election_type_description
                            ,entity_type = self.dc_object.entity_type
                            ,entity_type_desc = self.dc_object.entity_type_desc
                            ,fec_election_type_desc = self.dc_object.fec_election_type_desc
                            ,fec_election_year = self.dc_object.fec_election_year
                            ,file_number = self.dc_object.file_number
                            ,filing_form = self.dc_object.filing_form
                            ,image_number = self.dc_object.image_number
                            ,line_number = self.dc_object.line_number
                            ,line_number_laber = self.dc_object.line_number_laber
                            ,link_id = self.dc_object.link_id
                            ,load_date = self.dc_object.load_date
                            ,memo_code = self.dc_object.memo_code
                            ,memo_code_full = self.dc_object.memo_code_full
                            ,memo_text = self.dc_object.memo_text
                            ,memoed_subtotal = self.dc_object.memoed_subtotal
                            ,national_committee_nonfederal_account = self.dc_object.national_committee_nonfederal_account
                            ,original_sub_id = self.dc_object.original_sub_id
                            ,payee_employer = self.dc_object.payee_employer
                            ,payee_first_name = self.dc_object.payee_first_name
                            ,payee_last_name = self.dc_object.payee_last_name
                            ,payee_middle_name = self.dc_object.payee_middle_name
                            ,payee_occupation = self.dc_object.payee_occupation
                            ,payee_prefix = self.dc_object.payee_prefix
                            ,payee_suffix = self.dc_object.payee_suffix
                            ,pdf_url = self.dc_object.pdf_url
                            ,recipient_city = self.dc_object.recipient_city
                            ,recipient_committee = self.dc_object.recipient_committee
                            ,recipient_committee_id = self.dc_object.recipient_committee_id
                            ,recipient_name = self.dc_object.recipient_name
                            ,recipient_state = self.dc_object.recipient_state
                            ,recipient_zip = self.dc_object.recipient_zip
                            ,ref_disp_excess_flg = self.dc_object.ref_disp_excess_flg
                            ,report_type = self.dc_object.report_type
                            ,report_year = self.dc_object.report_year
                            ,schedule_type = self.dc_object.schedule_type
                            ,schedule_type_full = self.dc_object.schedule_type_full
                            ,semi_annual_bundled_refund = self.dc_object.semi_annual_bundled_refund
                            ,spender_committee_designation = self.dc_object.spender_committee_designation
                            ,spender_committee_org_type = self.dc_object.spender_committee_org_type
                            ,sub_id = self.dc_object.sub_id
                            ,transaction_id = self.dc_object.transaction_id
                            ,two_year_transaction_period = self.dc_object.two_year_transaction_period
                            ,unused_recipient_committee_id = self.dc_object.unused_recipient_committee_id
                           

                    )
                    session.add(schedule_a)
                    session.commit()

            except Exception as e:
                raise        
            # return None       

class InsertScheduleA:
    def __init__(self,dc_object):
        self.dc_object = dc_object
        
    def check_insert(self):
        x = SelectOneFecScheduleA(link_id=self.dc_object.link_id, sub_id=self.dc_object.sub_id)
        result = x.select()
        if result:
            result = True
        else:
            result = False
        return result
        
    def insert(self):
        if self.check_insert() == False:
            try:
                with Session(engine) as session:
                    schedule_a = ScheduleA(
                        amendment_indicator = self.dc_object.amendment_indicator
                        ,amendment_indicator_desc = self.dc_object.amendment_indicator_desc
                        ,back_reference_schedule_name = self.dc_object.back_reference_schedule_name
                        ,back_reference_transaction_id = self.dc_object.back_reference_transaction_id
                        ,candidate_first_name = self.dc_object.candidate_first_name
                        ,candidate_id = self.dc_object.candidate_id
                        ,candidate_last_name = self.dc_object.candidate_last_name
                        ,candidate_middle_name = self.dc_object.candidate_middle_name
                        ,candidate_name = self.dc_object.candidate_name
                        ,candidate_office = self.dc_object.candidate_office
                        ,candidate_office_district = self.dc_object.candidate_office_district
                        ,candidate_office_full = self.dc_object.candidate_office_full
                        ,candidate_office_state = self.dc_object.candidate_office_state
                        ,candidate_office_state_full = self.dc_object.candidate_office_state_full
                        ,candidate_prefix = self.dc_object.candidate_prefix
                        ,candidate_suffix = self.dc_object.candidate_suffix
                        ,committee = self.dc_object.committee
                        ,committee_id = self.dc_object.committee_id
                        ,committee_name = self.dc_object.committee_name
                        ,conduit_committee_city = self.dc_object.conduit_committee_city
                        ,conduit_committee_id = self.dc_object.conduit_committee_id
                        ,conduit_committee_name = self.dc_object.conduit_committee_name
                        ,conduit_committee_state = self.dc_object.conduit_committee_state
                        ,conduit_committee_street1 = self.dc_object.conduit_committee_street1
                        ,conduit_committee_street2 = self.dc_object.conduit_committee_street2
                        ,conduit_committee_zip = self.dc_object.conduit_committee_zip 
                        ,contribution_receipt_amount = self.dc_object.contribution_receipt_amount
                        ,contribution_receipt_date = self.dc_object.contribution_receipt_date
                        ,contributor = self.dc_object.contributor
                        ,contributor_aggregate_ytd = self.dc_object.contributor_aggregate_ytd
                        ,contributor_city = self.dc_object.contributor_city
                        ,contributor_employer = self.dc_object.contributor_employer
                        ,contributor_first_name = self.dc_object.contributor_first_name
                        ,contributor_id = self.dc_object.contributor_id
                        ,contributor_last_name = self.dc_object.contributor_last_name
                        ,contributor_middle_name = self.dc_object.contributor_middle_name
                        ,contributor_name = self.dc_object.contributor_name
                        ,contributor_occupation = self.dc_object.contributor_occupation
                        ,contributor_prefix = self.dc_object.contributor_prefix
                        ,contributor_state = self.dc_object.contributor_state
                        ,contributor_street_1 = self.dc_object.contributor_street_1 
                        ,contributor_street_2 = self.dc_object.contributor_street_2
                        ,contributor_suffix = self.dc_object.contributor_suffix
                        ,contributor_zip = self.dc_object.contributor_zip
                        ,donor_committee_name = self.dc_object.donor_committee_name
                        ,election_type = self.dc_object.election_type
                        ,election_type_full = self.dc_object.election_type_full
                        ,entity_type = self.dc_object.entity_type
                        ,entity_type_desc = self.dc_object.entity_type_desc
                        ,fec_election_type_desc = self.dc_object.fec_election_type_desc
                        ,fec_election_year = self.dc_object.fec_election_year
                        ,file_number = self.dc_object.file_number
                        ,filing_form = self.dc_object.filing_form 
                        ,image_number = self.dc_object.image_number
                        ,increased_limit = self.dc_object.increased_limit
                        ,is_individual = self.dc_object.is_individual
                        ,line_number = self.dc_object.line_number
                        ,line_number_label = self.dc_object.line_number_label
                        ,link_id = self.dc_object.link_id
                        ,load_date = self.dc_object.load_date 
                        ,memo_code = self.dc_object.memo_code
                        ,memo_code_full = self.dc_object.memo_code_full
                        ,memo_text = self.dc_object.memo_text
                        ,memoed_subtotal = self.dc_object.memoed_subtotal
                        ,national_committee_nonfederal_account = self.dc_object.national_committee_nonfederal_account
                        ,original_sub_id = self.dc_object.original_sub_id
                        ,pdf_url = self.dc_object.pdf_url
                        ,receipt_type = self.dc_object.receipt_type
                        ,receipt_type_desc = self.dc_object.receipt_type_desc
                        ,receipt_type_full = self.dc_object.receipt_type_full
                        ,recipient_committee_designation = self.dc_object.recipient_committee_designation
                        ,recipient_committee_org_type = self.dc_object.recipient_committee_org_type
                        ,recipient_committee_type = self.dc_object.recipient_committee_type
                        ,report_type = self.dc_object.report_type
                        ,report_year = self.dc_object.report_year
                        ,schedule_type = self.dc_object.schedule_type
                        ,schedule_type_full = self.dc_object.schedule_type_full
                        ,sub_id = self.dc_object.sub_id
                        ,transaction_id = self.dc_object.transaction_id
                        ,two_year_transaction_period = self.dc_object.two_year_transaction_period
                        ,unused_contbr_id = self.dc_object.unused_contbr_id    

                    )
                    session.add(schedule_a)
                    session.commit()

            except Exception as e:
                raise        
            # return None       

class InsertLoadLog:
    def __init__(self,committee_id, page, num_pages, last_index, last_crd, per_page, count):
        self.committee_id = committee_id 
        self.page = page
        self.num_pages = num_pages
        self.last_index = last_index 
        self.last_crd = last_crd 
        self.per_page = per_page
        self.count = count
        # self.org_id = org_id
        # pass
    def insert(self):
        try:
            with Session(engine) as session:
                load_log = FecLoadLog(
                            committee_id=self.committee_id
                            ,page = self.page
                            ,num_pages = self.num_pages
                            ,last_index = self.last_index
                            ,last_crd = self.last_crd 
                            ,per_page = self.per_page
                            ,count = self.count
                )
                session.add(load_log)
                session.commit()
        except Exception as e:
            raise  