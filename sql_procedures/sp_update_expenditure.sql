-- PROCEDURE: public.sp_update_expenditure()

-- DROP PROCEDURE public.sp_update_expenditure();

CREATE OR REPLACE PROCEDURE public.sp_update_expenditure(
	)
LANGUAGE 'sql'
AS $BODY$
--INDIVIDUALS NOT $250
UPDATE 		
		public.expenditure
SET 
		payee_type = original_payee_type,
-- 		payee_type_short = 'Indv',
		payee_name = CASE 
							WHEN original_middle_name = '' AND original_suffix = ''
								THEN original_payee_name || ', ' || original_first_name
							WHEN original_middle_name != '' AND original_suffix = ''
								THEN original_payee_name || ', ' || original_first_name || ' ' || original_middle_name
							WHEN original_middle_name != '' AND original_suffix != ''
								THEN original_payee_name || ', ' || original_first_name || ' ' || original_middle_name || ' ' || original_suffix
							WHEN original_middle_name = '' AND original_suffix != ''
								THEN original_payee_name || ', ' || original_first_name || ' ' || original_suffix								
							END,
		last_name = coalesce(original_payee_name,''),
		first_name = coalesce(original_first_name,''),
		middle_name = coalesce(original_middle_name,''),
		suffix = coalesce(original_suffix,'')
		
WHERE original_payee_type in ('Individual','Self (Candidate)')
AND (original_payee_name not like '%$250%'
OR original_first_name not like '%$250%');

UPDATE 
public.expenditure
SET
		payee_type = CASE 
						WHEN original_payee_name = 'XXXX' and original_first_name = 'BUSINESSES UNDER $250' then 'Business'
						WHEN original_payee_type not in ('Individual','Self (Candidate)') then original_payee_type
						else 'Individual (Group)' END,
 		payee_type_short = 'Indiv (Grp)',
		payee_name = CASE 
								WHEN original_payee_name = '$250.00 OR LESS FROM INDIVIDUALS' and original_first_name = '###' then '$250 OR LESS - Individual'
								WHEN original_payee_name = 'DURING THE REPORTING PERIOD < 250.01' and original_first_name = 'PAYEES WHO WERE PAID, EACH $250 OR LESS' then '$250 OR LESS - Individual'
								WHEN original_payee_name = 'FOR THE CALENDAR YEAR < 250' and original_first_name = 'INDIVIDUALS WHO HAVE CONTRIBUTED DURING THE REPORTING PERIOD, BUT EACH $250 OR LESS' then '$250 OR LESS - Individual'
								WHEN original_payee_name = 'FOR THE CALENDAR YEAR < 250.01' and original_first_name = 'INDIVIDUALS WHO HAVE CONTRIBUTED DURING THE REPORTING PERIOD, BUT EACH $250 OR LESS' then '$250 OR LESS - Individual'
								WHEN original_payee_name = 'LESS THAN 250' and original_first_name = 'OTHERS' then '$250 OR LESS - Individual'
								WHEN original_payee_name = 'OTHERS (NON-INDIVIDUALS) WHO HAVE CONTRIBUTED DURING PERIOD, BUT EACH $250 OR LESS FOR CALENDAR YEAR' and original_first_name = '' then '$250 OR LESS - Non-Individual'	
								WHEN original_payee_name = 'PAYEES WHO WERE PAID, EACH $250 OR LESS DURING THE REPORTING PERIOD' and original_first_name = '' then '$250 OR LESS - Non-Individual'
								WHEN original_payee_name = 'VFW POST 2503' and original_first_name = '' then original_payee_name	
								WHEN original_payee_name = 'XXX' and original_first_name = 'EXPENDITURES UNDER 250' then '$250 OR LESS - Individual'
								WHEN original_payee_name = 'XXXX' and original_first_name = 'EXPENDITURES UNDER $250' then '$250 OR LESS - Individual'
								WHEN original_payee_type = 'Individual' then '$250 OR LESS - Individual'
								WHEN original_payee_type != 'Individual' then '$250 OR LESS - Non-Individual'
								ELSE original_payee_name END,
		last_name = '',
		first_name = '',
		middle_name = '',
		suffix = '',	
		address_1 = '',
		address_2 = '',
		city = '',
		state = 'NE',
		zip = '00000'								
	
WHERE  (original_payee_name like '%$250%'
OR original_first_name like '%$250%');	

-- --INDIVIDUALS WITH $250
-- UPDATE 
-- public.expenditure
-- SET
-- 		payee_type = 'Individual (Group)',
--  		payee_type_short = 'Indiv (Grp)',
-- 		payee_name = '$250 OR LESS',
-- 		last_name = '',
-- 		first_name = '',
-- 		middle_name = '',
-- 		suffix = '',	
-- 		address_1 = '',
-- 		address_2 = '',
-- 		city = '',
-- 		state = 'NE',
-- 		zip = '00000'
		
		
-- WHERE original_payee_type in ('Individual','Self (Candidate)')
-- AND (original_payee_name like '%$250%'
-- OR original_first_name like '%$250%');

-- --NOT INDIVIDUALS WITH $250		
-- UPDATE 
-- 		public.expenditure
-- SET 
-- 		payee_type = original_payee_type,
-- 		payee_name = '$250 OR LESS',
-- 		last_name = '',
-- 		first_name = '',
-- 		middle_name = '',
-- 		suffix = '',
-- 		address_1 = '',
-- 		address_2 = '',
-- 		city = '',
-- 		state = '',
-- 		zip = '00000'
								
		
-- WHERE original_payee_type not in ('Individual','Self (Candidate)')
-- AND (original_payee_name like '%$250%'
-- OR original_first_name like '%$250%');

--NOT INDIVIDUALS NOT $250		
UPDATE
		public.expenditure
SET 
		payee_type = original_payee_type,
		payee_name = original_payee_name,
		last_name = '',
		first_name = '',
		middle_name = '',
		suffix = ''
					
WHERE original_payee_type not in ('Individual','Self (Candidate)')
AND NOT (original_payee_name like '%$250%'
OR original_first_name like '%$250%');
		

--payee TYPE SHORT	
UPDATE 	public.expenditure	
SET 
payee_type_short = 
			CASE 	original_payee_type 
				WHEN 'Political Party Committee'
					THEN 'Party Cmte'
				WHEN 'Self (Candidate)'
					THEN 'Self (Cand)'
				WHEN 'PAC-Independent'
					THEN 'PAC-Ind'
				WHEN ''
					THEN 'Unk'
				WHEN 'Business (For-Profit and Non-Profit entities)'
					THEN 'Biz (FP & NP)'
				WHEN 'PAC-Separate Segregated Political Fund'
					THEN 'PAC-SSPF'
				WHEN 'Federal PAC'
					THEN 'Fed PAC'
				WHEN 'Ballot Question Committee'
					then 'BQ Cmte'	
				WHEN 'Individual'
					THEN 'Indv'
				WHEN 'Candidate Committee'
					THEN 'Cand Cmte'
				ELSE '' END;
				
	
--INDIVIDUALS WITH $250
--OVERRIDE payee TYPE
-- UPDATE 
-- public.expenditure
-- SET
-- 		payee_type = 'Individual (Group)',
--  		payee_type_short = 'Indiv (Grp)'
						
-- WHERE original_payee_type = 'Individual'
-- AND (original_payee_name like '%$250%'
-- OR original_first_name like '%$250%');
$BODY$;
