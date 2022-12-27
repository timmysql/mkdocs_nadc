-- PROCEDURE: public.sp_load_payor()

-- DROP PROCEDURE public.sp_load_payor();

CREATE OR REPLACE PROCEDURE public.sp_load_payor(
	)
LANGUAGE 'sql'
AS $BODY$
insert into payor (
original_payor_type, original_payor_name, original_first_name, original_middle_name, 
original_suffix, payor_type, payor_type_short, 
payor_name, last_name, first_name, middle_name, suffix,
address_1, address_2, city, state, zip
)

SELECT  
		c.original_payor_type, c.original_payor_name, c.original_first_name, 
		c.original_middle_name, 
		c.original_suffix, c.payor_type, c.payor_type_short, 
		c.payor_name, c.last_name, c.first_name, c.middle_name, c.suffix,
		c.address_1, c.address_2, c.city, c.state, c.zip
-- employer, occupation 

FROM public.v_load_payor as c

LEFT JOIN payor as p
ON
		c.original_payor_type = p.original_payor_type
	and c.original_payor_name = p.original_payor_name
	and c.original_first_name = p.original_first_name
	and c.original_middle_name = p.original_middle_name
	and c.original_suffix = p.original_suffix
	
WHERE p.original_payor_name IS NULL
	;

update contribution
set payor_id = payor.id,
	payor_name = payor.payor_name
from payor
WHERE 
		contribution.original_payor_type = payor.original_payor_type
	and contribution.original_payor_name = payor.original_payor_name
	and contribution.original_first_name = payor.original_first_name
	and contribution.original_middle_name = payor.original_middle_name
	and contribution.original_suffix = payor.original_suffix;

update payor
set receipt_payor_count = x.payor_count
	,receipt_payor_total_amount = x. receipt_total
from 
(select 
		count(1) as payor_count, 
		sum(receipt_amount) as receipt_total
		, payor_id
from contribution
group by 
		payor_id) as x
		where payor.id = x.payor_id;
		
		
update payor
set markdown_file = replace(replace(
					translate(
					lower(payor_name)
						,'()-,.$/.\#','')
						,'''',''),' ','-');	
						
update payor
set city_state = CASE
	when city != '' AND state != '' then city || ', ' || state
	when city != '' AND state = '' then city 
	when city = '' AND state != '' then state 
	else '' end;
	
update payor
set payor_folder = case 
						when lower(left(payor_name,1)) = 'a' then 'payors_a'
						when lower(left(payor_name,1)) = 'b' then 'payors_b'
						when lower(left(payor_name,1)) = 'c' then 'payors_c'
						when lower(left(payor_name,1)) = 'd' then 'payors_d'
						when lower(left(payor_name,1)) = 'e' then 'payors_e'
						when lower(left(payor_name,1)) = 'f' then 'payors_f'
						when lower(left(payor_name,1)) = 'g' then 'payors_g'
						when lower(left(payor_name,1)) = 'h' then 'payors_h'
						when lower(left(payor_name,1)) = 'i' then 'payors_i'
						when lower(left(payor_name,1)) = 'j' then 'payors_j'
						when lower(left(payor_name,1)) = 'k' then 'payors_k'
						when lower(left(payor_name,1)) = 'l' then 'payors_l'
						when lower(left(payor_name,1)) = 'm' then 'payors_m'
						when lower(left(payor_name,1)) = 'n' then 'payors_n'
						when lower(left(payor_name,1)) = 'o' then 'payors_o'
						when lower(left(payor_name,1)) = 'p' then 'payors_p'
						when lower(left(payor_name,1)) = 'q' then 'payors_q'
						when lower(left(payor_name,1)) = 'r' then 'payors_r'
						when lower(left(payor_name,1)) = 's' then 'payors_s'
						when lower(left(payor_name,1)) = 't' then 'payors_t'
						when lower(left(payor_name,1)) = 'u' then 'payors_u'
						when lower(left(payor_name,1)) = 'v' then 'payors_v'
						when lower(left(payor_name,1)) = 'w' then 'payors_w'
						when lower(left(payor_name,1)) = 'x' then 'payors_x'
						when lower(left(payor_name,1)) = 'y' then 'payors_y'
						when lower(left(payor_name,1)) = 'z' then 'payors_z'
						else 'payors_other' end	;
	
	
	
update contribution
set payor_markdown_file = payor.markdown_file
from payor
where  contribution.payor_id = payor.id;

update contribution
set payor_folder = case 
						when lower(left(payor_name,1)) = 'a' then 'payors_a'
						when lower(left(payor_name,1)) = 'b' then 'payors_b'
						when lower(left(payor_name,1)) = 'c' then 'payors_c'
						when lower(left(payor_name,1)) = 'd' then 'payors_d'
						when lower(left(payor_name,1)) = 'e' then 'payors_e'
						when lower(left(payor_name,1)) = 'f' then 'payors_f'
						when lower(left(payor_name,1)) = 'g' then 'payors_g'
						when lower(left(payor_name,1)) = 'h' then 'payors_h'
						when lower(left(payor_name,1)) = 'i' then 'payors_i'
						when lower(left(payor_name,1)) = 'j' then 'payors_j'
						when lower(left(payor_name,1)) = 'k' then 'payors_k'
						when lower(left(payor_name,1)) = 'l' then 'payors_l'
						when lower(left(payor_name,1)) = 'm' then 'payors_m'
						when lower(left(payor_name,1)) = 'n' then 'payors_n'
						when lower(left(payor_name,1)) = 'o' then 'payors_o'
						when lower(left(payor_name,1)) = 'p' then 'payors_p'
						when lower(left(payor_name,1)) = 'q' then 'payors_q'
						when lower(left(payor_name,1)) = 'r' then 'payors_r'
						when lower(left(payor_name,1)) = 's' then 'payors_s'
						when lower(left(payor_name,1)) = 't' then 'payors_t'
						when lower(left(payor_name,1)) = 'u' then 'payors_u'
						when lower(left(payor_name,1)) = 'v' then 'payors_v'
						when lower(left(payor_name,1)) = 'w' then 'payors_w'
						when lower(left(payor_name,1)) = 'x' then 'payors_x'
						when lower(left(payor_name,1)) = 'y' then 'payors_y'
						when lower(left(payor_name,1)) = 'z' then 'payors_z'
						else 'payors_other' end
$BODY$;
