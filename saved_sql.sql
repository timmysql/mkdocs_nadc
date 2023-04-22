	select 
			contributor_last_name, contributor_first_name, contributor_city, contributor_state
			,contributor_name
			--, image_number, filer_number, link_id, pdf_url
			--,sub_id, transaction_id
			,sum(contribution_receipt_amount::money)
	FROM public.fec_schedule_a
	group by 
				contributor_last_name, contributor_first_name, contributor_city, contributor_state
			,contributor_name
	order by sum(contribution_receipt_amount::money) desc