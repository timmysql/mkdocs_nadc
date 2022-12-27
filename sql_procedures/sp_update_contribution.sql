-- PROCEDURE: public.sp_update_contribution()

-- DROP PROCEDURE public.sp_update_contribution();

CREATE OR REPLACE PROCEDURE public.sp_update_contribution(
	)
LANGUAGE 'sql'
AS $BODY$
--INDIVIDUALS NOT $250
UPDATE 		
		public.contribution
SET 
		payor_type = original_payor_type,
-- 		payor_type_short = 'Indv',
		payor_name = CASE 
							WHEN original_middle_name = '' AND original_suffix = ''
								THEN original_payor_name || ', ' || original_first_name
							WHEN original_middle_name != '' AND original_suffix = ''
								THEN original_payor_name || ', ' || original_first_name || ' ' || original_middle_name
							WHEN original_middle_name != '' AND original_suffix != ''
								THEN original_payor_name || ', ' || original_first_name || ' ' || original_middle_name || ' ' || original_suffix
							WHEN original_middle_name = '' AND original_suffix != ''
								THEN original_payor_name || ', ' || original_first_name || ' ' || original_suffix								
							END,
		last_name = coalesce(original_payor_name,''),
		first_name = coalesce(original_first_name,''),
		middle_name = coalesce(original_middle_name,''),
		suffix = coalesce(original_suffix,'')
		
WHERE original_payor_type in ('Individual','Self (Candidate)')
AND (original_payor_name not like '%$250%'
OR original_first_name not like '%$250%');

UPDATE 
public.contribution
SET
		payor_type = CASE 
						WHEN original_payor_name = 'XXXX' and original_first_name = 'BUSINESSES UNDER $250' then 'Business'
						WHEN original_payor_type not in ('Individual','Self (Candidate)') then original_payor_type
						else 'Individual (Group)' END,
 		payor_type_short = 'Indiv (Grp)',
		payor_name = CASE 
								WHEN original_payor_name = '$250.00 OR LESS FROM INDIVIDUALS' and original_first_name = '###' then '$250 OR LESS - Individual'
								WHEN original_payor_name = '$250 OR LESS' and original_first_name = 'OTHERS' then '$250 OR LESS - Individual'
								WHEN original_payor_name = 'FOR THE CALENDAR YEAR' and original_first_name = 'INDIVIDUALS WHO HAVE CONTRIBUTED DURING THE REPORTING PERIOD, BUT EACH $250 OR LESS' then '$250 OR LESS - Individual'
								WHEN original_payor_name = 'FOR THE CALENDAR YEAR < 250' and original_first_name = 'INDIVIDUALS WHO HAVE CONTRIBUTED DURING THE REPORTING PERIOD, BUT EACH $250 OR LESS' then '$250 OR LESS - Individual'
								WHEN original_payor_name = 'FOR THE CALENDAR YEAR < 250.01' and original_first_name = 'INDIVIDUALS WHO HAVE CONTRIBUTED DURING THE REPORTING PERIOD, BUT EACH $250 OR LESS' then '$250 OR LESS - Individual'
								
								WHEN original_payor_name = 'LESS THAN 250' and original_first_name = 'OTHERS' then '$250 OR LESS - Individual'	
								WHEN original_payor_name = 'OTHERS (NON-INDIVIDUALS) WHO HAVE CONTRIBUTED DURING PERIOD, BUT EACH $250 OR LESS FOR CALENDAR YEAR' and original_first_name = '' then '$250 OR LESS - Non-Individual'	
								WHEN original_payor_name = 'PAYEES WHO WERE PAID, EACH $250 OR LESS DURING THE REPORTING PERIOD' and original_first_name = '' then '$250 OR LESS - Non-Individual'	
								WHEN original_payor_name = 'TRANSCANADA USA SERVICES, INC. PAC  FEC#C00525055' and original_first_name = '' then original_payor_name
								WHEN original_payor_name = 'UNDER 250' and original_first_name = 'BUSINESSES' then '$250 OR LESS - Non-Individual'	
								WHEN original_payor_name = 'UNDER 250' and original_first_name = 'INDIVIDUALS' then '$250 OR LESS - Individual'	
								
								
								
								WHEN original_payor_name = 'VARIOUS' and original_first_name = 'VARIOUS CONTRIBUTIONS UNDER $250' then '$250 OR LESS - Individual'	
								WHEN original_payor_name = 'XXXX' and original_first_name = 'INDIVIDUALS UNDER $250' then '$250 OR LESS - Individual'
								WHEN original_payor_name = 'XXXX' and original_first_name = 'BUSINESSES UNDER $250' then '$250 OR LESS - Non-Individual'	
								WHEN original_payor_type = 'Individual' then '$250 OR LESS - Individual'
								WHEN original_payor_type != 'Individual' then '$250 OR LESS - Non-Individual'
								ELSE original_payor_name END,
		last_name = '',
		first_name = '',
		middle_name = '',
		suffix = '',	
		address_1 = '',
		address_2 = '',
		city = '',
		state = 'NE',
		zip = '00000'								
	
WHERE  (original_payor_name like '%$250%'
OR original_first_name like '%$250%');	

-- --INDIVIDUALS WITH $250
-- UPDATE 
-- public.contribution
-- SET
-- 		payor_type = 'Individual (Group)',
--  		payor_type_short = 'Indiv (Grp)',
-- 		payor_name = '$250 OR LESS - Individual',
-- 		last_name = '',
-- 		first_name = '',
-- 		middle_name = '',
-- 		suffix = '',	
-- 		address_1 = '',
-- 		address_2 = '',
-- 		city = '',
-- 		state = 'NE',
-- 		zip = '00000'
		
		
-- WHERE original_payor_type in ('Individual','Self (Candidate)')
-- AND (original_payor_name like '%$250%'
-- OR original_first_name like '%$250%');

--NOT INDIVIDUALS WITH $250		
-- UPDATE 
-- 		public.contribution
-- SET 
-- 		payor_type = original_payor_type,
-- 		payor_name = '$250 OR LESS - Non-Individual',
-- 		last_name = '',
-- 		first_name = '',
-- 		middle_name = '',
-- 		suffix = '',
-- 		address_1 = '',
-- 		address_2 = '',
-- 		city = '',
-- 		state = '',
-- 		zip = '00000'
								
		
-- WHERE original_payor_type not in ('Individual','Self (Candidate)')
-- AND (original_payor_name like '%$250%'
-- OR original_first_name like '%$250%');

--NOT INDIVIDUALS NOT $250		
UPDATE
		public.contribution
SET 
		payor_type = original_payor_type,
		payor_name = original_payor_name,
		last_name = '',
		first_name = '',
		middle_name = '',
		suffix = ''
					
WHERE original_payor_type not in ('Individual','Self (Candidate)')
AND NOT (original_payor_name like '%$250%'
OR original_first_name like '%$250%');
		

--PAYOR TYPE SHORT	
UPDATE 	public.contribution	
SET 
payor_type_short = 
			CASE 	original_payor_type 
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
					THEN 'Indiv'
				WHEN 'Candidate Committee'
					THEN 'Cand Cmte'
				ELSE '' END;
				
	
--INDIVIDUALS WITH $250
--OVERRIDE PAYOR TYPE
-- UPDATE 
-- public.contribution
-- SET
-- 		payor_type = 'Individual (Group)',
--  		payor_type_short = 'Indiv (Grp)'
						
-- WHERE original_payor_type in ('Individual','Self (Candidate)')
-- AND (original_payor_name like '%$250%'
-- OR original_first_name like '%$250%');
$BODY$;
