-- Table: public.stage_expenditures

-- DROP TABLE public.stage_expenditures;

CREATE TABLE IF NOT EXISTS public.stage_expenditures
(
    index bigint,
    expenditure_id bigint,
    org_id bigint,
    filer_type text COLLATE pg_catalog."default",
    filer_name text COLLATE pg_catalog."default",
    candidate_name text COLLATE pg_catalog."default",
    expenditure_transaction_type text COLLATE pg_catalog."default",
    expenditure_sub_type text COLLATE pg_catalog."default",
    expenditure_date text COLLATE pg_catalog."default",
    expenditure_amount double precision,
    description text COLLATE pg_catalog."default",
    payee_or_recipient_or_in_kind_contributor_type text COLLATE pg_catalog."default",
    payee_or_recipient_or_in_kind_contributor_name text COLLATE pg_catalog."default",
    first_name text COLLATE pg_catalog."default",
    middle_name text COLLATE pg_catalog."default",
    suffix text COLLATE pg_catalog."default",
    address_1 text COLLATE pg_catalog."default",
    address_2 text COLLATE pg_catalog."default",
    city text COLLATE pg_catalog."default",
    state text COLLATE pg_catalog."default",
    zip text COLLATE pg_catalog."default",
    filed_date text COLLATE pg_catalog."default",
    support_or_oppose text COLLATE pg_catalog."default",
    candidate_name_or_ballot_issue text COLLATE pg_catalog."default",
    jurisdiction_office_district_or_ballot_description text COLLATE pg_catalog."default",
    amended text COLLATE pg_catalog."default",
    employer text COLLATE pg_catalog."default",
    occupation text COLLATE pg_catalog."default",
    principal_place_of_business text COLLATE pg_catalog."default"
)

TABLESPACE pg_default;

ALTER TABLE public.stage_expenditures
    OWNER to osint;
-- Index: ix_stage_expenditures_index

-- DROP INDEX public.ix_stage_expenditures_index;

CREATE INDEX ix_stage_expenditures_index
    ON public.stage_expenditures USING btree
    (index ASC NULLS LAST)
    TABLESPACE pg_default;