-- View: public.v_load_payor

-- DROP VIEW public.v_load_payor;

CREATE OR REPLACE VIEW public.v_load_payor
 AS
 SELECT x.row_id,
    x.original_payor_type,
    x.original_payor_name,
    x.original_first_name,
    x.original_middle_name,
    x.original_suffix,
    x.payor_type,
    x.payor_type_short,
    x.payor_name,
    x.last_name,
    x.first_name,
    x.middle_name,
    x.suffix,
    x.address_1,
    x.address_2,
    x.city,
    x.state,
    x.zip
   FROM ( SELECT row_number() OVER (PARTITION BY c.original_payor_type, c.original_payor_name, c.original_first_name, c.original_middle_name, c.original_suffix ORDER BY c.receipt_date DESC) AS row_id,
            c.original_payor_type,
            c.original_payor_name,
            c.original_first_name,
            c.original_middle_name,
            c.original_suffix,
            c.payor_type,
            c.payor_type_short,
                CASE
                    WHEN c.payor_name::text = ''::text THEN 'NO PAYOR INDICATED'::character varying
                    ELSE c.payor_name
                END AS payor_name,
            c.last_name,
            c.first_name,
            c.middle_name,
            c.suffix,
            c.address_1,
            c.address_2,
            c.city,
            c.state,
            c.zip
           FROM contribution c) x
  WHERE x.row_id = 1;

ALTER TABLE public.v_load_payor
    OWNER TO postgres;

