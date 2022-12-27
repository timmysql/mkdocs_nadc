-- View: public.v_expenditure_filer

-- DROP VIEW public.v_expenditure_filer;

CREATE OR REPLACE VIEW public.v_expenditure_filer
 AS
 SELECT x.org_id,
    x.filer_type,
    x.filer_type_short,
    x.filer_name,
    count(1) AS expenditure_count,
    sum(x.expenditure_amount)::numeric(16,2) AS expenditure_total_amount
   FROM ( SELECT expenditure.org_id,
            first_value(expenditure.filer_type) OVER (PARTITION BY expenditure.org_id ORDER BY expenditure.expenditure_id DESC) AS filer_type,
            first_value(expenditure.filer_type_short) OVER (PARTITION BY expenditure.org_id ORDER BY expenditure.expenditure_id DESC) AS filer_type_short,
            first_value(expenditure.filer_name) OVER (PARTITION BY expenditure.org_id ORDER BY expenditure.expenditure_id DESC) AS filer_name,
            expenditure.expenditure_id,
            expenditure.expenditure_amount::numeric(16,2) AS expenditure_amount
           FROM expenditure) x
  GROUP BY x.org_id, x.filer_type, x.filer_type_short, x.filer_name
  ORDER BY (count(1)) DESC;

ALTER TABLE public.v_expenditure_filer
    OWNER TO postgres;

