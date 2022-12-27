-- FUNCTION: public.get_expenditures_key_values_unnest(bigint)

-- DROP FUNCTION public.get_expenditures_key_values_unnest(bigint);

CREATE OR REPLACE FUNCTION public.get_expenditures_key_values_unnest(
	p_expenditure_id bigint)
    RETURNS TABLE(return_expenditure_id bigint, return_key text, return_value text) 
    LANGUAGE 'plpgsql'
    COST 100
    VOLATILE PARALLEL UNSAFE
    ROWS 1000

AS $BODY$
BEGIN 
	return query 
	SELECT 
		expenditure_id as return_expenditure_id,
		unnest(array['expenditure_id', 'org_id', 'filer_name', 'filer_type', 'candidate_name', 'trans_type', 
			   'amount', 'description',  'sub_type', 'date',  
			    'entity_name', 'entity_type',
			   'first_name', 'middle_name', 'suffix', 'address_1', 'address_2', 'city', 'state', 'zip', 'filed_date', 
			   'support_or_oppose', 'candidate_name_or_ballot_issue', 'jurisdiction_office_district_or_ballot_description', 
			   'amended', 'employer', 'occupation', 'principal_place_of_business', 'create_dt', 'update_dt', 'delete_flag', 'delete_dt']) as return_key
	   ,unnest(array[expenditure_id::text, org_id::text, filer_name, filer_type, candidate_name, expenditure_transaction_type, 
		       expenditure_amount::text,  description, expenditure_sub_type, expenditure_date::text,  
		       payee_or_recipient_or_in_kind_contributor_name, payee_or_recipient_or_in_kind_contributor_type, 
		       first_name, middle_name, suffix, address_1, address_2, city, state, zip, filed_date::text, 
		       support_or_oppose, candidate_name_or_ballot_issue, jurisdiction_office_district_or_ballot_description, 
		       amended, employer, occupation, principal_place_of_business, create_dt::text, update_dt::text, delete_flag::text, delete_dt::text]) as return_value
	FROM public.expenditure
	WHERE expenditure_id = p_expenditure_id;	
	
END;
$BODY$;

ALTER FUNCTION public.get_expenditures_key_values_unnest(bigint)
    OWNER TO osint;
