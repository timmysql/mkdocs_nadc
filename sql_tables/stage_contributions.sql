-- Table: public.stage_contributions

-- DROP TABLE public.stage_contributions;

CREATE TABLE IF NOT EXISTS public.stage_contributions
(
    index bigint,
    receipt_id bigint,
    org_id bigint,
    filer_type text COLLATE pg_catalog."default",
    filer_name text COLLATE pg_catalog."default",
    candidate_name text COLLATE pg_catalog."default",
    receipt_transaction_contribution_type text COLLATE pg_catalog."default",
    other_funds_type text COLLATE pg_catalog."default",
    receipt_date text COLLATE pg_catalog."default",
    receipt_amount double precision,
    description text COLLATE pg_catalog."default",
    contributor_or_transaction_source_type text COLLATE pg_catalog."default",
    contributor_or_source_name_individual_last_name text COLLATE pg_catalog."default",
    first_name text COLLATE pg_catalog."default",
    middle_name text COLLATE pg_catalog."default",
    suffix text COLLATE pg_catalog."default",
    address_1 text COLLATE pg_catalog."default",
    address_2 text COLLATE pg_catalog."default",
    city text COLLATE pg_catalog."default",
    state text COLLATE pg_catalog."default",
    zip text COLLATE pg_catalog."default",
    filed_date text COLLATE pg_catalog."default",
    amended text COLLATE pg_catalog."default",
    employer text COLLATE pg_catalog."default",
    occupation text COLLATE pg_catalog."default"
)

TABLESPACE pg_default;

ALTER TABLE public.stage_contributions
    OWNER to osint;
-- Index: ix_stage_contributions_index

-- DROP INDEX public.ix_stage_contributions_index;

CREATE INDEX ix_stage_contributions_index
    ON public.stage_contributions USING btree
    (index ASC NULLS LAST)
    TABLESPACE pg_default;