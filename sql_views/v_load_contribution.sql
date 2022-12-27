-- View: public.v_load_contribution

-- DROP VIEW public.v_load_contribution;

CREATE OR REPLACE VIEW public.v_load_contribution
 AS
 SELECT stage_contributions.receipt_id,
    stage_contributions.org_id,
    stage_contributions.filer_type,
    stage_contributions.filer_name,
    COALESCE(stage_contributions.candidate_name, ''::text) AS candidate_name,
    COALESCE(stage_contributions.receipt_transaction_contribution_type, ''::text) AS contribution_type,
    COALESCE(stage_contributions.other_funds_type, ''::text) AS other_funds_type,
    stage_contributions.receipt_date::date AS receipt_date,
    stage_contributions.receipt_amount::numeric(16,2) AS receipt_amount,
    COALESCE(stage_contributions.description, ''::text) AS description,
    COALESCE(stage_contributions.contributor_or_transaction_source_type, ''::text) AS payor_type,
    COALESCE(stage_contributions.contributor_or_source_name_individual_last_name, ''::text) AS payor_name,
    COALESCE(stage_contributions.first_name, ''::text) AS first_name,
    COALESCE(stage_contributions.middle_name, ''::text) AS middle_name,
    COALESCE(stage_contributions.suffix, ''::text) AS suffix,
    COALESCE(stage_contributions.address_1, ''::text) AS address_1,
    COALESCE(stage_contributions.address_2, ''::text) AS address_2,
    COALESCE(stage_contributions.city, ''::text) AS city,
    COALESCE(stage_contributions.state, ''::text) AS state,
    COALESCE(stage_contributions.zip, ''::text) AS zip,
    stage_contributions.filed_date::date AS filed_date,
    COALESCE(stage_contributions.amended, ''::text) AS amended,
    COALESCE(stage_contributions.employer, ''::text) AS employer,
    COALESCE(stage_contributions.occupation, ''::text) AS occupation,
    CURRENT_TIMESTAMP AS create_dt,
    0 AS tweet_sent
   FROM stage_contributions;

ALTER TABLE public.v_load_contribution
    OWNER TO postgres;

