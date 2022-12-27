-- PROCEDURE: public.sp_update_filer_type_short()

-- DROP PROCEDURE public.sp_update_filer_type_short();

CREATE OR REPLACE PROCEDURE public.sp_update_filer_type_short(
	)
LANGUAGE 'sql'
AS $BODY$
-- stuff goes here

UPDATE contribution
SET
		filer_type_short = 
                        CASE    filer_type
                                WHEN 'Political Party Committee'
                                        THEN 'Party Cmte'
                                WHEN 'Self (Candidate)'
                                        THEN 'Self (Cand)'
                                WHEN 'PAC-Independent'
                                        THEN 'PAC-Ind'
                                WHEN ''
                                        THEN 'Unk'
                                WHEN 'Business (For-Profit and Non-Profit entities)'
                                        THEN 'Bus (FP & NP)'
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
								WHEN 'Nebraska Business Supplemental Filer'
										THEN 'Neb Bus Sup Filer'										
                                ELSE '' END;

							
							
							
UPDATE expenditure
SET
		filer_type_short = 
                        CASE    filer_type
                                WHEN 'Political Party Committee'
                                        THEN 'Party Cmte'
                                WHEN 'Self (Candidate)'
                                        THEN 'Self (Cand)'
                                WHEN 'PAC-Independent'
                                        THEN 'PAC-Ind'
                                WHEN ''
                                        THEN 'Unk'
                                WHEN 'Business (For-Profit and Non-Profit entities)'
                                        THEN 'Bus (FP & NP)'
                                WHEN 'PAC-Separate Segregated Political Fund'
                                        THEN 'PAC-SSPF'
                                WHEN 'Federal PAC'
                                        THEN 'Fed PAC'
                                WHEN 'Ballot Question Committee'
                                        then 'BQ Comm'
                                WHEN 'Individual'
                                        THEN 'Indiv'
                                WHEN 'Candidate Committee'
                                        THEN 'Cand Cmte'
								WHEN 'Nebraska Business Supplemental Filer'
										THEN 'Neb Bus Sup Filer'
                                ELSE '' END
$BODY$;
