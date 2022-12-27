-- FUNCTION: public.get_expenditures_key_values(bigint)

-- DROP FUNCTION public.get_expenditures_key_values(bigint);

CREATE OR REPLACE FUNCTION public.get_expenditures_key_values(
	p_expenditure_id bigint)
    RETURNS TABLE(srt integer, return_expenditure_id bigint, return_key text, return_value text) 
    LANGUAGE 'plpgsql'
    COST 100
    VOLATILE PARALLEL UNSAFE
    ROWS 1000

AS $BODY$
BEGIN 
	return query 
				SELECT 1 AS srt,
					expenditure.expenditure_id::bigint,
					'filer_name'::text AS return_key,
					expenditure.filer_name::text AS return_value
				   FROM expenditure
				  WHERE expenditure_id::bigint = p_expenditure_id
				UNION
				 SELECT 2 AS srt,
					expenditure.expenditure_id,
					'candidate_name'::text AS return_key,
					expenditure.candidate_name AS return_value
				   FROM expenditure
				  WHERE expenditure_id::bigint = p_expenditure_id
				UNION
				 SELECT 3 AS srt,
					expenditure.expenditure_id,
					'expenditure_transaction_type'::text AS return_key,
					expenditure.expenditure_transaction_type AS return_value
				   FROM expenditure
				  WHERE expenditure_id::bigint = p_expenditure_id
				UNION
				 SELECT 4 AS srt,
					expenditure.expenditure_id,
					'expenditure_sub_type'::text AS return_key,
					expenditure.expenditure_sub_type AS return_value
				   FROM expenditure
				  WHERE expenditure_id = p_expenditure_id
				UNION
				 SELECT 5 AS srt,
					expenditure.expenditure_id,
					'expenditure_date'::text AS return_key,
					expenditure.expenditure_date::text AS return_value
				   FROM expenditure
				  WHERE expenditure_id::bigint = p_expenditure_id
				UNION
				 SELECT 6 AS srt,
					expenditure.expenditure_id,
					'expenditure_amount'::text AS return_key,
					expenditure.expenditure_amount::text AS return_value
				   FROM expenditure
				  WHERE expenditure_id::bigint = p_expenditure_id
				UNION
				 SELECT 7 AS srt,
					expenditure.expenditure_id,
					'description'::text AS return_key,
					expenditure.description AS return_value
				   FROM expenditure
				  WHERE expenditure_id::bigint = p_expenditure_id
				UNION
				 SELECT 8 AS srt,
					expenditure.expenditure_id,
					'payee_or_contributor_type'::text AS return_key,
					expenditure.payee_or_recipient_or_in_kind_contributor_type AS return_value
				   FROM expenditure
				  WHERE expenditure_id::bigint = p_expenditure_id
				UNION
				 SELECT 9 AS srt,
					expenditure.expenditure_id,
					'payee_or_contributor_name'::text AS return_key,
					expenditure.payee_or_recipient_or_in_kind_contributor_name AS return_value
				   FROM expenditure
				  WHERE expenditure_id::bigint = p_expenditure_id
				UNION
				 SELECT 10 AS srt,
					expenditure.expenditure_id,
					'address1'::text AS return_key,
					expenditure.address_1 AS return_value
				   FROM expenditure
				  WHERE expenditure_id::bigint = p_expenditure_id
				UNION
				 SELECT 11 AS srt,
					expenditure.expenditure_id,
					'address2'::text AS return_key,
					COALESCE(expenditure.address_2, ''::text) AS return_value
				   FROM expenditure
				  WHERE expenditure_id::bigint = p_expenditure_id
				UNION
				 SELECT 12 AS srt,
					expenditure.expenditure_id,
					'city'::text AS return_key,
					expenditure.city AS return_value
				   FROM expenditure
				   WHERE expenditure_id::bigint = p_expenditure_id
				UNION
				 SELECT 13 AS srt,
					expenditure.expenditure_id,
					'state'::text AS return_key,
					expenditure.state AS return_value
				   FROM expenditure
				  WHERE expenditure_id::bigint = p_expenditure_id
				UNION
				 SELECT 14 AS srt,
					expenditure.expenditure_id,
					'zip'::text AS return_key,
					expenditure.zip AS return_value
				   FROM expenditure
				  WHERE expenditure_id::bigint = p_expenditure_id
				  ORDER BY 2, 1;
	
END;
$BODY$;

ALTER FUNCTION public.get_expenditures_key_values(bigint)
    OWNER TO osint;
