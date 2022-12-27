-- PROCEDURE: public.sp_load_contribution()

-- DROP PROCEDURE public.sp_load_contribution();

CREATE OR REPLACE PROCEDURE public.sp_load_contribution(
	)
LANGUAGE 'sql'
AS $BODY$
-- stuff goes here
insert into public.contribution
(
	receipt_id, org_id, filer_type, filer_name, candidate_name, contribution_type, other_funds_type, 
 	receipt_date, receipt_amount, description, 
	original_payor_type, 
	original_payor_name,
 	original_first_name, 
	original_middle_name, 
	original_suffix, 
	address_1, address_2, city, state, zip, filed_date, amended, employer, occupation, create_dt, tweet_sent)
SELECT 
		receipt_id, 
		org_id, 
		filer_type, 
		filer_name, 
		candidate_name, 
		contribution_type, 
		other_funds_type, 
		receipt_date, 
		receipt_amount, 
		description, 
		payor_type,
		payor_name,
		first_name, 
		middle_name, 
		suffix, 
		address_1, 
		address_2, 
		city, 
		state, 
		zip, 
		filed_date, 

		amended, 
		employer, 
		occupation,
		create_dt,
		0 tweet_sent
FROM public.v_load_contribution
WHERE receipt_id not in (select receipt_id from public.contribution);

update public.contribution
set
		receipt_id = src.receipt_id
		,org_id = src.org_id
		,filer_type = src.filer_type
		,filer_name = src.filer_name
		,candidate_name = src.candidate_name
		,contribution_type = src.contribution_type
		,other_funds_type = src.other_funds_type
		,receipt_date = src.receipt_date
		,receipt_amount = src.receipt_amount
		,description = src.description
		,original_payor_type = src.payor_type
		,original_payor_name = src.payor_name
		,original_first_name = src.first_name
		,original_middle_name = src.middle_name
		,original_suffix  = src.suffix
		,address_1 = src.address_1 
		,address_2 = src.address_2
		,city = src.city
		,state = src.state
		,zip = src.zip
		,filed_date = src.filed_date
		,amended = src.amended
		,employer = src.employer
		,occupation = src.occupation 
from 
		public.v_load_contribution as src
		
where 
        (public.contribution.receipt_id = src.receipt_id)
		AND (
		public.contribution.receipt_id <> src.receipt_id
		OR public.contribution.org_id <> src.org_id
		OR public.contribution.filer_type <> src.filer_type
		OR public.contribution.filer_name <> src.filer_name
		OR public.contribution.candidate_name <> src.candidate_name
		OR public.contribution.contribution_type <> src.contribution_type
		OR public.contribution.other_funds_type <> src.other_funds_type
		OR public.contribution.receipt_date <> src.receipt_date
		OR public.contribution.receipt_amount <> src.receipt_amount
		OR public.contribution.description <> src.description

		OR public.contribution.original_payor_type <> src.payor_type
		OR public.contribution.original_payor_name <> src.payor_name
		OR public.contribution.original_first_name <> src.first_name
		OR public.contribution.original_middle_name <> src.middle_name
		OR public.contribution.original_suffix  <> src.suffix
		
		OR public.contribution.address_1 <> src.address_1 
		OR public.contribution.address_2 <> src.address_2
		OR public.contribution.city <> src.city
		OR public.contribution.state <> src.state
		OR public.contribution.zip <> src.zip
		OR public.contribution.filed_date <> src.filed_date
		OR public.contribution.amended <> src.amended
		OR public.contribution.employer <> src.employer
		OR public.contribution.occupation <> src.occupation )

;
	
	
-- soft delete
-- update public.contribution
-- set 
-- 	delete_flag = 1
-- 	delete_dt = current_timestamp
-- where
$BODY$;
