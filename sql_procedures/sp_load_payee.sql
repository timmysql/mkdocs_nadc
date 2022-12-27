-- PROCEDURE: public.sp_load_payee()

-- DROP PROCEDURE public.sp_load_payee();

CREATE OR REPLACE PROCEDURE public.sp_load_payee(
	)
LANGUAGE 'sql'
AS $BODY$
insert into payee (
original_payee_type, original_payee_name, original_first_name, original_middle_name, 
original_suffix, payee_type, payee_type_short, 
payee_name, last_name, first_name, middle_name, suffix,
address_1, address_2, city, state, zip
)
SELECT distinct
		c.original_payee_type, c.original_payee_name, c.original_first_name, 
		c.original_middle_name, 
		c.original_suffix, c.payee_type, c.payee_type_short, 
		c.payee_name, c.last_name, c.first_name, c.middle_name, c.suffix,
		c.address_1, c.address_2, c.city, c.state, c.zip
-- employer, occupation 

FROM public.v_load_payee as c
LEFT JOIN payee as p
ON
		c.original_payee_type = p.original_payee_type
	and c.original_payee_name = p.original_payee_name
	and c.original_first_name = p.original_first_name
	and c.original_middle_name = p.original_middle_name
	and c.original_suffix = p.original_suffix
	
WHERE p.original_payee_name IS NULL
	;

update expenditure
set payee_id = payee.id,
	payee_name = payee.payee_name
from payee
WHERE 
		expenditure.original_payee_type = payee.original_payee_type
	and expenditure.original_payee_name = payee.original_payee_name
	and expenditure.original_first_name = payee.original_first_name
	and expenditure.original_middle_name = payee.original_middle_name
	and expenditure.original_suffix = payee.original_suffix;
	
	
update payee
set expenditure_payee_count = x.payee_count
	,expenditure_payee_total_amount = x. expenditure_total
from 
(select 
		count(1) as payee_count, 
		sum(expenditure_amount) as expenditure_total
		, payee_id
from expenditure
group by 
		payee_id) as x
		where payee.id = x.payee_id;	
		
		

update payee
set markdown_file = replace(replace(
					translate(
					lower(payee_name)
						,'()-,.$/.\#','')
						,'''',''),' ','-');	

update payee
set city_state = CASE
	when city != '' AND state != '' then city || ', ' || state
	when city != '' AND state = '' then city 
	when city = '' AND state != '' then state 
	else '' end;

update payee
set payee_folder = case 
						when lower(left(payee_name,1)) = 'a' then 'payees_a'
						when lower(left(payee_name,1)) = 'b' then 'payees_b'
						when lower(left(payee_name,1)) = 'c' then 'payees_c'
						when lower(left(payee_name,1)) = 'd' then 'payees_d'
						when lower(left(payee_name,1)) = 'e' then 'payees_e'
						when lower(left(payee_name,1)) = 'f' then 'payees_f'
						when lower(left(payee_name,1)) = 'g' then 'payees_g'
						when lower(left(payee_name,1)) = 'h' then 'payees_h'
						when lower(left(payee_name,1)) = 'i' then 'payees_i'
						when lower(left(payee_name,1)) = 'j' then 'payees_j'
						when lower(left(payee_name,1)) = 'k' then 'payees_k'
						when lower(left(payee_name,1)) = 'l' then 'payees_l'
						when lower(left(payee_name,1)) = 'm' then 'payees_m'
						when lower(left(payee_name,1)) = 'n' then 'payees_n'
						when lower(left(payee_name,1)) = 'o' then 'payees_o'
						when lower(left(payee_name,1)) = 'p' then 'payees_p'
						when lower(left(payee_name,1)) = 'q' then 'payees_q'
						when lower(left(payee_name,1)) = 'r' then 'payees_r'
						when lower(left(payee_name,1)) = 's' then 'payees_s'
						when lower(left(payee_name,1)) = 't' then 'payees_t'
						when lower(left(payee_name,1)) = 'u' then 'payees_u'
						when lower(left(payee_name,1)) = 'v' then 'payees_v'
						when lower(left(payee_name,1)) = 'w' then 'payees_w'
						when lower(left(payee_name,1)) = 'x' then 'payees_x'
						when lower(left(payee_name,1)) = 'y' then 'payees_y'
						when lower(left(payee_name,1)) = 'z' then 'payees_z'
						else 'payees_other' end;

update expenditure
set payee_markdown_file = payee.markdown_file
from payee
where expenditure.payee_id = payee.id;

update expenditure
set payee_folder = case 
						when lower(left(payee_name,1)) = 'a' then 'payees_a'
						when lower(left(payee_name,1)) = 'b' then 'payees_b'
						when lower(left(payee_name,1)) = 'c' then 'payees_c'
						when lower(left(payee_name,1)) = 'd' then 'payees_d'
						when lower(left(payee_name,1)) = 'e' then 'payees_e'
						when lower(left(payee_name,1)) = 'f' then 'payees_f'
						when lower(left(payee_name,1)) = 'g' then 'payees_g'
						when lower(left(payee_name,1)) = 'h' then 'payees_h'
						when lower(left(payee_name,1)) = 'i' then 'payees_i'
						when lower(left(payee_name,1)) = 'j' then 'payees_j'
						when lower(left(payee_name,1)) = 'k' then 'payees_k'
						when lower(left(payee_name,1)) = 'l' then 'payees_l'
						when lower(left(payee_name,1)) = 'm' then 'payees_m'
						when lower(left(payee_name,1)) = 'n' then 'payees_n'
						when lower(left(payee_name,1)) = 'o' then 'payees_o'
						when lower(left(payee_name,1)) = 'p' then 'payees_p'
						when lower(left(payee_name,1)) = 'q' then 'payees_q'
						when lower(left(payee_name,1)) = 'r' then 'payees_r'
						when lower(left(payee_name,1)) = 's' then 'payees_s'
						when lower(left(payee_name,1)) = 't' then 'payees_t'
						when lower(left(payee_name,1)) = 'u' then 'payees_u'
						when lower(left(payee_name,1)) = 'v' then 'payees_v'
						when lower(left(payee_name,1)) = 'w' then 'payees_w'
						when lower(left(payee_name,1)) = 'x' then 'payees_x'
						when lower(left(payee_name,1)) = 'y' then 'payees_y'
						when lower(left(payee_name,1)) = 'z' then 'payees_z'
						else 'payees_other' end
$BODY$;
