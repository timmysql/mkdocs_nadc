-- PROCEDURE: public.sp_load_filer()

-- DROP PROCEDURE public.sp_load_filer();

CREATE OR REPLACE PROCEDURE public.sp_load_filer(
	)
LANGUAGE 'sql'
AS $BODY$
--insert
--expenditurefiler		
		insert into expenditurefiler
		(org_id, filer_type, filer_type_short, filer_name, expenditure_count, expenditure_total_amount)
		SELECT org_id, filer_type, filer_type_short, filer_name, expenditure_count, expenditure_total_amount		
		FROM public.v_expenditure_filer
		where org_id not in (select distinct org_id from expenditurefiler);
		
--insert		
--contributionfiler
		insert into contributionfiler
		(org_id, filer_type, filer_type_short, filer_name, receipt_count, receipt_total_amount)
		SELECT org_id, filer_type, filer_type_short, filer_name, receipt_count, receipt_total_amount
		FROM public.v_contribution_filer
		where org_id not in (select distinct org_id from contributionfiler);
		
--insert		
--filer from v_expenditures
		insert into filer
		(org_id, filer_type, filer_type_short, filer_name, expenditure_count, expenditure_total_amount)
		SELECT org_id, filer_type, filer_type_short, filer_name, expenditure_count, expenditure_total_amount		
		FROM public.v_expenditure_filer
		where org_id not in (select distinct org_id from filer);
		
--insert		
--filer from v_contributions
		insert into filer
		(org_id, filer_type, filer_type_short, filer_name, receipt_count, receipt_total_amount)
		SELECT org_id, filer_type, filer_type_short, filer_name, receipt_count, receipt_total_amount
		FROM public.v_contribution_filer
		where org_id not in (select distinct org_id from filer);

--update
--expenditurefiler
		update expenditurefiler
		set 
				filer_name = src.filer_name
				,filer_type = src.filer_type
				,filer_type_short = src.filer_type_short
				,expenditure_count = coalesce(src.expenditure_count,0)
				,expenditure_total_amount = coalesce(src.expenditure_total_amount,0)
		-- select * 
		from 
		-- 		filers,
				v_expenditure_filer as src
		where 
				expenditurefiler.org_id = src.org_id
		AND (expenditurefiler.filer_type <> src.filer_type
			 or expenditurefiler.filer_type_short <> src.filer_type_short
			 or expenditurefiler.filer_name <> src.filer_name
			 or coalesce(expenditurefiler.expenditure_count,0) <>  coalesce(src.expenditure_count,0)
			 or coalesce(expenditurefiler.expenditure_total_amount,0) <>  coalesce(src.expenditure_total_amount,0)
			 );
--update
--contributionfiler
		update contributionfiler
		set 
				filer_name = src.filer_name
				,filer_type = src.filer_type
				,filer_type_short = src.filer_type_short
				,receipt_count = coalesce(src.receipt_count,0)
				,receipt_total_amount = coalesce(src.receipt_total_amount,0)
		-- select * 
		from 
		-- 		filers,
				v_contribution_filer as src
		where 
				contributionfiler.org_id = src.org_id
		AND (contributionfiler.filer_type <> src.filer_type
			 or contributionfiler.filer_type_short <> src.filer_type_short
			 or contributionfiler.filer_name <> src.filer_name
			 or coalesce(contributionfiler.receipt_count,0) <>  coalesce(src.receipt_count,0)
			 or coalesce(contributionfiler.receipt_total_amount,0) <>  coalesce(src.receipt_total_amount,0)
			 );

--update		
--filer from v_expenditure_filer
		update filer
		set 
				filer_name = src.filer_name
				,filer_type = src.filer_type
				,filer_type_short = src.filer_type_short
				,expenditure_count = coalesce(src.expenditure_count,0)
				,expenditure_total_amount = coalesce(src.expenditure_total_amount,0)								
		-- select * 
		from 
		-- 		filers,
				v_expenditure_filer as src
		where 
				filer.org_id = src.org_id
		AND (filer.filer_type <> src.filer_type
		     or filer.filer_type_short <> src.filer_type_short
			 or filer.filer_name <> src.filer_name
			 or coalesce(filer.expenditure_count,0) <>  coalesce(src.expenditure_count,0)
			 or coalesce(filer.expenditure_total_amount,0) <>  coalesce(src.expenditure_total_amount,0)			 

			 );

--update		
--filer from v_contribution_filer
		update filer
		set 
				filer_name = src.filer_name
				,filer_type = src.filer_type
				,filer_type_short = src.filer_type_short
				,receipt_count = coalesce(src.receipt_count,0)
				,receipt_total_amount = coalesce(src.receipt_total_amount,0)
		-- select * 
		from 
		-- 		filers,
				v_contribution_filer as src
		where 
				filer.org_id = src.org_id
		AND (filer.filer_type <> src.filer_type
			 or filer.filer_name <> src.filer_name
			 or filer.filer_type_short <> src.filer_type_short
			 or coalesce(filer.receipt_count,0) <>  coalesce(src.receipt_count,0)
			 or coalesce(filer.receipt_total_amount,0) <>  coalesce(src.receipt_total_amount,0)
			 );
			 
--update nulls to zero

--filer
		update filer 
		set expenditure_count = 0
		where expenditure_count is null;
		
		update filer 
		set expenditure_total_amount = 0
		where expenditure_total_amount is null;	
		
		update filer 
		set receipt_count = 0
		where receipt_count is null;
		
		update filer 
		set receipt_total_amount = 0
		where receipt_total_amount is null;		
		
--expenditure filer
		update expenditurefiler 
		set expenditure_count = 0
		where expenditure_count is null;
		
		update expenditurefiler 
		set expenditure_total_amount = 0
		where expenditure_total_amount is null;	

--contribution filer

		update contributionfiler 
		set receipt_count = 0
		where receipt_count is null;
		
		update contributionfiler 
		set receipt_total_amount = 0
		where receipt_total_amount is null;
		
		
update filer
set markdown_file = replace(
					translate(
					replace(lower(filer_name),' ','_')
						,'(),-.$/.\#','')
						,'''','');	
						
						
update contribution
set filer_markdown_file = filer.markdown_file
from filer
where  contribution.org_id = filer.org_id;	

update expenditure
set filer_markdown_file = filer.markdown_file
from filer
where expenditure.org_id = filer.org_id;
$BODY$;
