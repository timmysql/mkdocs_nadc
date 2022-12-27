-- View: public.v_load_expenditure

-- DROP VIEW public.v_load_expenditure;

CREATE OR REPLACE VIEW public.v_load_expenditure
 AS
 SELECT stage_expenditures.expenditure_id,
    stage_expenditures.org_id,
    stage_expenditures.filer_type,
    COALESCE(stage_expenditures.filer_name, ''::text) AS filer_name,
    COALESCE(stage_expenditures.candidate_name, ''::text) AS candidate_name,
    COALESCE(stage_expenditures.expenditure_transaction_type, ''::text) AS expenditure_type,
    COALESCE(stage_expenditures.expenditure_sub_type, ''::text) AS expenditure_sub_type,
    stage_expenditures.expenditure_date::date AS expenditure_date,
    stage_expenditures.expenditure_amount::numeric(16,2) AS expenditure_amount,
    COALESCE(stage_expenditures.description, ''::text) AS description,
    COALESCE(stage_expenditures.payee_or_recipient_or_in_kind_contributor_type, ''::text) AS payee_type,
    COALESCE(stage_expenditures.payee_or_recipient_or_in_kind_contributor_name, ''::text) AS payee_name,
    COALESCE(stage_expenditures.first_name, ''::text) AS first_name,
    COALESCE(stage_expenditures.middle_name, ''::text) AS middle_name,
    COALESCE(stage_expenditures.suffix, ''::text) AS suffix,
    COALESCE(stage_expenditures.address_1, ''::text) AS address_1,
    COALESCE(stage_expenditures.address_2, ''::text) AS address_2,
    COALESCE(stage_expenditures.city, ''::text) AS city,
    COALESCE(stage_expenditures.state, ''::text) AS state,
    COALESCE(stage_expenditures.zip, ''::text) AS zip,
    stage_expenditures.filed_date::date AS filed_date,
    COALESCE(stage_expenditures.support_or_oppose, ''::text) AS support_or_oppose,
    COALESCE(stage_expenditures.candidate_name_or_ballot_issue, ''::text) AS candidate_name_or_ballot_issue,
    COALESCE(stage_expenditures.jurisdiction_office_district_or_ballot_description, ''::text) AS jurisdiction_office_district_or_ballot_description,
    COALESCE(stage_expenditures.amended, ''::text) AS amended,
    COALESCE(stage_expenditures.employer, ''::text) AS employer,
    COALESCE(stage_expenditures.occupation, ''::text) AS occupation,
    COALESCE(stage_expenditures.principal_place_of_business, ''::text) AS principal_place_of_business,
    CURRENT_TIMESTAMP AS create_dt,
    0 AS tweet_sent
   FROM stage_expenditures;

ALTER TABLE public.v_load_expenditure
    OWNER TO postgres;

