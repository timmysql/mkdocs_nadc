-- View: public.v_contribution_filer

-- DROP VIEW public.v_contribution_filer;

CREATE OR REPLACE VIEW public.v_contribution_filer
 AS
 SELECT x.org_id,
    x.filer_type,
    x.filer_type_short,
    x.filer_name,
    count(1) AS receipt_count,
    sum(x.receipt_amount)::numeric(16,2) AS receipt_total_amount
   FROM ( SELECT contribution.org_id,
            first_value(contribution.filer_type) OVER (PARTITION BY contribution.org_id ORDER BY contribution.receipt_id DESC) AS filer_type,
            first_value(contribution.filer_type_short) OVER (PARTITION BY contribution.org_id ORDER BY contribution.receipt_id DESC) AS filer_type_short,
            first_value(contribution.filer_name) OVER (PARTITION BY contribution.org_id ORDER BY contribution.receipt_id DESC) AS filer_name,
            contribution.receipt_id,
            contribution.receipt_amount::numeric(16,2) AS receipt_amount
           FROM contribution) x
  GROUP BY x.org_id, x.filer_type, x.filer_type_short, x.filer_name
  ORDER BY (count(1)) DESC;

ALTER TABLE public.v_contribution_filer
    OWNER TO postgres;

