-- PROCEDURE: public.sp_load_expenditure()

-- DROP PROCEDURE public.sp_load_expenditure();

CREATE OR REPLACE PROCEDURE public.sp_load_expenditure(
	)
LANGUAGE 'sql'
AS $BODY$
-- -- stuff goes here
insert into public.expenditure
(
	expenditure_id, org_id, filer_type, filer_name, candidate_name, expenditure_type, 
	expenditure_sub_type, expenditure_date, 
	expenditure_amount, description, 
	original_payee_type, 
	original_payee_name, 
	original_first_name, 
	original_middle_name, 
	original_suffix, 
	address_1, address_2, city, state, zip, filed_date, support_or_oppose, candidate_name_or_ballot_issue, 
	jurisdiction_office_district_or_ballot_description, amended, employer, occupation, principal_place_of_business, create_dt, tweet_sent
)
SELECT 
		expenditure_id, 
		org_id, 
		filer_type, filer_name, 
		candidate_name, 
		expenditure_type, 
		expenditure_sub_type, 
		expenditure_date, 
		expenditure_amount, 
		description, 
		payee_type, 
		payee_name, 
		first_name, 
		middle_name, 
		suffix, 
		address_1, 
		address_2, 
		city, 
		state, 
		zip, 
		filed_date, 
		support_or_oppose, 
		candidate_name_or_ballot_issue, 
		jurisdiction_office_district_or_ballot_description, 
		amended, 
		employer, 
		occupation, 
		principal_place_of_business,
		create_dt,
		0 tweet_sent
FROM public.v_load_expenditure
WHERE expenditure_id not in (select expenditure_id from public.expenditure);

update public.expenditure
set
		
		org_id = src.org_id
		,filer_type = src.filer_type
		,filer_name = src.filer_name
		,candidate_name = src.candidate_name
		,expenditure_type = src.expenditure_type
		,expenditure_sub_type = src.expenditure_sub_type
		,expenditure_date = src.expenditure_date
		,expenditure_amount= src.expenditure_amount
		,description = src.description
		,original_payee_type = src.payee_type
		,original_payee_name = src.payee_name
		,original_first_name = src.first_name
		,original_middle_name = src.middle_name
		,original_suffix = src.suffix 
		,address_1 = src.address_1
		,address_2 = src.address_2 
		,city = src.city
		,state = src.state
		,zip = src.zip
		,filed_date = src.filed_date
		,support_or_oppose = src.support_or_oppose
		,candidate_name_or_ballot_issue = src.candidate_name_or_ballot_issue
		,jurisdiction_office_district_or_ballot_description = src.jurisdiction_office_district_or_ballot_description
		,amended = src.amended
		,employer = src.employer
		,occupation = src.occupation 
		,principal_place_of_business = src.principal_place_of_business
from  
		public.v_load_expenditure as src
		
where 
        (public.expenditure.expenditure_id = src.expenditure_id)
		AND (
		public.expenditure.org_id <> src.org_id
		OR public.expenditure.filer_type <> src.filer_type
		OR public.expenditure.filer_name <> src.filer_name
		OR public.expenditure.candidate_name <> src.candidate_name
		OR public.expenditure.expenditure_type <> src.expenditure_type
		OR public.expenditure.expenditure_sub_type <> src.expenditure_sub_type
		OR public.expenditure.expenditure_date <> src.expenditure_date
		OR public.expenditure.expenditure_amount <> src.expenditure_amount
		OR public.expenditure.description <> src.description
		
		OR public.expenditure.original_payee_type <> src.payee_type
		OR public.expenditure.original_payee_name <> src.payee_name
		OR public.expenditure.original_first_name <> src.first_name
		OR public.expenditure.original_middle_name <> src.middle_name
		OR public.expenditure.original_suffix <> src.suffix
		OR public.expenditure.address_1 <> src.address_1
		OR public.expenditure.address_2 <> src.address_2 
		OR public.expenditure.city <> src.city
		OR public.expenditure.state <> src.state
		OR public.expenditure.zip <> src.zip
		OR public.expenditure.filed_date <> src.filed_date
		OR public.expenditure.support_or_oppose <> src.support_or_oppose
		OR public.expenditure.candidate_name_or_ballot_issue <> src.candidate_name_or_ballot_issue
		OR public.expenditure.jurisdiction_office_district_or_ballot_description <> src.jurisdiction_office_district_or_ballot_description
		OR public.expenditure.amended <> src.amended
		OR public.expenditure.employer <> src.employer
		OR public.expenditure.occupation <> src.occupation
		OR public.expenditure.principal_place_of_business <> src.principal_place_of_business		
		)

;
	
	
-- soft delete
-- update public.expenditure
-- set 
-- 	delete_flag = 1
-- 	delete_dt = current_timestamp
-- where
$BODY$;
