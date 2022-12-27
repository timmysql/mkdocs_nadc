-- View: public.v_load_payee

-- DROP VIEW public.v_load_payee;

CREATE OR REPLACE VIEW public.v_load_payee
 AS
 SELECT x.row_id,
    x.original_payee_type,
    x.original_payee_name,
    x.original_first_name,
    x.original_middle_name,
    x.original_suffix,
    x.payee_type,
    x.payee_type_short,
    x.payee_name,
    x.last_name,
    x.first_name,
    x.middle_name,
    x.suffix,
    x.address_1,
    x.address_2,
    x.city,
    x.state,
    x.zip
   FROM ( SELECT row_number() OVER (PARTITION BY c.original_payee_type, c.original_payee_name, c.original_first_name, c.original_middle_name, c.original_suffix ORDER BY c.expenditure_date DESC) AS row_id,
            c.original_payee_type,
            c.original_payee_name,
            c.original_first_name,
            c.original_middle_name,
            c.original_suffix,
            c.payee_type,
            c.payee_type_short,
                CASE
                    WHEN c.payee_name::text = ''::text THEN 'NO PAYEE INDICATED'::character varying
                    ELSE c.payee_name
                END AS payee_name,
            c.last_name,
            c.first_name,
            c.middle_name,
            c.suffix,
            c.address_1,
            c.address_2,
            c.city,
            c.state,
            c.zip
           FROM expenditure c) x
  WHERE x.row_id = 1;

ALTER TABLE public.v_load_payee
    OWNER TO postgres;

