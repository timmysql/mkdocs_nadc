
from dataclasses import dataclass
from dataclasses_json import dataclass_json
from typing import Optional, List, Union

# https://api.open.fec.gov/swagger/
# back_reference_schedule_id
@dataclass_json
@dataclass
class DcScheduleB:
    amendment_indicator: Optional[str]
    amendment_indicator_desc: Optional[str]
    back_reference_schedule_id: Optional[str] = None
    back_reference_transaction_id: Optional[str] = None
    beneficiary_committee_name: Optional[str] = None
    candidate_first_name: Optional[str] = None
    candidate_id: Optional[str] = None
    candidate_last_name: Optional[str] = None
    candidate_middle_name: Optional[str] = None
    candidate_name: Optional[str] = None
    candidate_office: Optional[str] = None
    candidate_office_description: Optional[str] = None
    candidate_office_district: Optional[str] = None
    candidate_office_state: Optional[str] = None
    candidate_office_state_full: Optional[str] = None
    candidate_prefix: Optional[str] = None
    candidate_suffix: Optional[str] = None
    category_code: Optional[str] = None
    category_code_full: Optional[str] = None
    comm_dt: Optional[str] = None
    committee: Optional[str] = None
    committee_id: Optional[str] = None
    conduit_committee_city: Optional[str] = None
    conduit_committee_name: Optional[str] = None
    conduit_committee_state: Optional[str] = None
    conduit_committee_street1: Optional[str] = None
    conduit_committee_street2: Optional[str] = None
    conduit_committee_zip: Optional[int] = None
    disbursement_amount: Optional[float] = None
    disbursement_date: Optional[str] = None
    disbursement_description: Optional[str] = None
    disbursement_purpose_category: Optional[str] = None
    disbursement_type: Optional[str] = None
    disbursement_type_description: Optional[str] = None
    election_type: Optional[str] = None
    election_type_description: Optional[str] = None
    entity_type: Optional[str] = None
    entity_type_desc: Optional[str] = None
    fec_election_type_desc: Optional[str] = None
    fec_election_year: Optional[str] = None
    file_number: Optional[int] = None
    filing_form: Optional[str] = None
    image_number: Optional[str] = None
    line_number: Optional[str] = None
    line_number_laber: Optional[str] = None
    link_id: Optional[str] = None
    load_date: Optional[str] = None
    memo_code: Optional[str] = None
    memo_code_full: Optional[str] = None
    memo_text: Optional[str] = None
    memoed_subtotal: Optional[bool] = None
    national_committee_nonfederal_account: Optional[str] = None
    original_sub_id: Optional[str] = None
    payee_employer: Optional[str] = None
    payee_first_name: Optional[str] = None
    payee_last_name: Optional[str] = None
    payee_middle_name: Optional[str] = None
    payee_occupation: Optional[str] = None
    payee_prefix: Optional[str] = None
    payee_suffix: Optional[str] = None
    pdf_url: Optional[str] = None
    recipient_city: Optional[str] = None
    recipient_committee: Optional[str] = None
    recipient_committee_id: Optional[str] = None
    recipient_name: Optional[str] = None
    recipient_state: Optional[str] = None
    recipient_zip: Optional[str] = None
    ref_disp_excess_flg: Optional[str] = None
    report_type: Optional[str] = None
    report_year: Optional[int] = None
    schedule_type: Optional[str] = None
    schedule_type_full: Optional[str] = None
    semi_annual_bundled_refund: Optional[float] = None
    spender_committee_designation: Optional[str] = None
    spender_committee_org_type: Optional[str] = None
    sub_id: Optional[str] = None
    transaction_id: Optional[str] = None
    two_year_transaction_period: Optional[int] = None
    unused_recipient_committee_id: Optional[str] = None
    
    
        


@dataclass_json
@dataclass
class DcScheduleA:
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
    link_id: Optional[str]
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
    sub_id: Optional[str]
    transaction_id: Optional[str]
    two_year_transaction_period: Optional[int]
    unused_contbr_id:  Optional[str]   