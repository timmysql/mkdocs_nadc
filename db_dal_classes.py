# from crypt import methods
import sqlmodel 
from typing import Optional
from sqlmodel import Field, Session, SQLModel, create_engine, select, or_
# import db_config as cfg
# import models as mdl
from db_models import PppData, Payee, Payor, Filer, ExpenditureFiler, Expenditure, ContributionFiler, Contribution, ErrorLog
from db_config import DbConfig
from sqlmodel.sql.expression import Select, SelectOfScalar
from rich import inspect
from datetime import date, timedelta 


engine = db_engine = DbConfig.get_central_engine()
    
SelectOfScalar.inherit_cache = True  # type: ignore
Select.inherit_cache = True  # type: ignore       


class SelectPayor:
    def __init__(self):
        # self.org_id = org_id
        pass
     
    # def __str__(self):
    #     filer = self.get()
    #     string = ''
    #     string += f"org_id: {filer.org_id}" + '\r\n'
    #     string += f"name: {filer.filer_name}"
    #     return string
        
    def all(self):
        try:
            with Session(engine) as session:
                statement = select(Payor).order_by(Payor.payor_name.asc())
                results = session.exec(statement)
                # print(dir(results))
                filers = results.fetchall()
                # for filer in results:
                #     print(filer.org_id)
            return filers
        except Exception as e:
            raise
        
    def sample(self):
        try:
            with Session(engine) as session:
                statement = select(Payor).limit(200).order_by(Payor.payor_name.asc())
                results = session.exec(statement)
                # print(dir(results))
                filers = results.fetchall()
                # for filer in results:
                #     print(filer.org_id)
            return filers
        except Exception as e:
            raise        
            # return None       


class SelectPayee:
    def __init__(self):
        # self.org_id = org_id
        pass
     
    # def __str__(self):
    #     filer = self.get()
    #     string = ''
    #     string += f"org_id: {filer.org_id}" + '\r\n'
    #     string += f"name: {filer.filer_name}"
    #     return string
        
    def all(self):
        try:
            with Session(engine) as session:
                statement = select(Payee).order_by(Payee.payee_name.asc())
                results = session.exec(statement)
                # print(dir(results))
                filers = results.fetchall()
                # for filer in results:
                #     print(filer.org_id)
            return filers
        except Exception as e:
            raise
        
    def sample(self):
        try:
            with Session(engine) as session:
                statement = select(Payee).limit(200).order_by(Payee.payee_name.asc())
                results = session.exec(statement)
                # print(dir(results))
                filers = results.fetchall()
                # for filer in results:
                #     print(filer.org_id)
            return filers
        except Exception as e:
            raise    
        
     



class SelectFiler:
    def __init__(self):
        # self.org_id = org_id
        pass
     
    def __str__(self):
        filer = self.get()
        string = ''
        string += f"org_id: {filer.org_id}" + '\r\n'
        string += f"name: {filer.filer_name}"
        return string
        
    def all(self):
        try:
            with Session(engine) as session:
                statement = select(Filer).order_by(Filer.filer_name.asc())
                results = session.exec(statement)
                # print(dir(results))
                filers = results.fetchall()
                # for filer in results:
                #     print(filer.org_id)
            return filers
        except Exception as e:
            raise
        
    def sample(self):
        try:
            with Session(engine) as session:
                statement = select(Filer).limit(200).order_by(Filer.filer_name.asc())
                results = session.exec(statement)
                # print(dir(results))
                filers = results.fetchall()
                # for filer in results:
                #     print(filer.org_id)
            return filers
        except Exception as e:
            raise        
            # return None       
    
    def select_group(self):
        governors_race = [7688,7707,7582,7695,7417,7579]
        try:
            with Session(engine) as session:
                statement = select(Filer).where(or_(
                                                           Filer.org_id == 7688,                
                                                           Filer.org_id == 7707,
                                                           Filer.org_id == 7582,
                                                           Filer.org_id == 7695,
                                                           Filer.org_id == 7417,
                                                           Filer.org_id == 7579
                                                           ))
                results = session.exec(statement)
                # print(dir(results))
                filers = results.fetchall()
                # for filer in results:
                #     print(filer.org_id)
            return filers
        except Exception as e:
            raise          
        

    
class SelectExpenditures:
       
    def __init__(self,amount=None):
        self.amount = amount
        # self.org_id = org_id
        # self.expenditure_id              
        pass
    
    def count_all(self):
        return len(self.all())
    
    def count_untweeted(self):
        return len(self.untweeted())
    
    def count_unbuilt(self):
        return len(self.unbuilt()) 
    
    def all_greater_than(self):
        with Session(engine) as session:
            statement = select(Expenditure).where(Expenditure.expenditure_amount >= self.amount).order_by(Expenditure.expenditure_amount.desc())
            results = session.exec(statement)
            expenditures = results.fetchall() 
            return expenditures     
    
    def all(self):
        with Session(engine) as session:
            statement = select(Expenditure).where(Expenditure.expenditure_id != 6760).order_by(Expenditure.expenditure_date.asc())
            results = session.exec(statement)
            expenditures = results.fetchall() 
            return expenditures   
        
    def last_1500(self):
        with Session(engine) as session:        
            statement = select(Expenditure).limit(1500).order_by(Expenditure.expenditure_date.desc())
            results = session.exec(statement)
            expenditures = results.fetchall() 
            return expenditures 
        
    def top_100_old(self):
        with Session(engine) as session:        
            statement = select(Expenditure).limit(200).order_by(Expenditure.expenditure_amount.desc())
            results = session.exec(statement)
            expenditures = results.fetchall() 
            return expenditures  
        
    def top_500(self):
        backdate = date.today() + timedelta(days=-90)
        # print(today)
        with Session(engine) as session:        
            statement = select(Expenditure).where(Expenditure.expenditure_date >= backdate).limit(500).order_by(Expenditure.expenditure_amount.desc())
            results = session.exec(statement)
            contributions = results.fetchall() 
            return contributions                              
    
    # def all(self):
    #     with Session(engine) as session:
    #         statement = select(Expenditure).where(Expenditure.expenditure_id != 6760).order_by(Expenditure.expenditure_date.asc())
    #         results = session.exec(statement)
    #         expenditures = results.fetchall() 
    #         return expenditures 
        
    # def tweeted(self):
    #     with Session(engine) as session:
    #         statement = select(Expenditure).where(Expenditure.tweet_sent == 1).where(Expenditure.expenditure_id != 6760).order_by(Expenditure.expenditure_date.asc())
    #         results = session.exec(statement)
    #         expenditures = results.fetchall() 
    #         return expenditures          
        
    # def untweeted(self):
    #     with Session(engine) as session:
    #         statement = select(Expenditure).where(Expenditure.tweet_sent == 0).where(Expenditure.expenditure_id != 6760).order_by(Expenditure.expenditure_date.asc())
    #         results = session.exec(statement)
    #         expenditures = results.fetchall() 
    #         return expenditures  
        
    # def unbuilt(self):
    #     with Session(engine) as session:    
    #         statement = select(Expenditure).where(Expenditure.tweet_message == None).where(Expenditure.expenditure_id != 6760).order_by(Expenditure.expenditure_date.asc())
    #         results = session.exec(statement)
    #         expenditures = results.fetchall() 
    #         return expenditures  

    def all_ids():
        with Session(engine) as session:
            statement = select(Expenditure.expenditure_id).where(Expenditure.expenditure_id != 6760)
            results = session.exec(statement)
            rtn_results = results.fetchall() 
        return rtn_results 

class SelectOrgExpenditures:
    def __init__(self,org_id):
        self.org_id = org_id
    
    def count_all(self):
        return len(self.all())
    
    def count_untweeted(self):
        return len(self.untweeted())
    
    def count_unbuilt(self):
        return len(self.unbuilt())    
    
    def last_tweeted(self):
        with Session(engine) as session:
            statement = select(Expenditure).where(Expenditure.org_id == self.org_id).where(Expenditure.tweet_id != None).order_by(Expenditure.tweet_dt.desc())
            results = session.exec(statement)
            rtn_results = results.first() 
        return rtn_results          
    
    def all(self):
        with Session(engine) as session:
            statement = select(Expenditure).where(Expenditure.org_id == self.org_id).order_by(Expenditure.expenditure_date.asc())
            results = session.exec(statement)
            expenditures = results.fetchall() 
            return expenditures 
        
    def tweeted(self):
        with Session(engine) as session:
            statement = select(Expenditure).where(Expenditure.tweet_sent == 1).where(Expenditure.org_id == self.org_id).order_by(Expenditure.expenditure_date.asc())
            results = session.exec(statement)
            expenditures = results.fetchall() 
            return expenditures          
        
    def untweeted(self):
        with Session(engine) as session:
            statement = select(Expenditure).where(Expenditure.tweet_sent == 0).where(Expenditure.org_id == self.org_id).where(Expenditure.expenditure_id != 6760).order_by(Expenditure.expenditure_date.asc())
            results = session.exec(statement)
            expenditures = results.fetchall() 
            return expenditures  
        
    def unbuilt(self):
        with Session(engine) as session:    
            statement = select(Expenditure).where(Expenditure.tweet_message == None).where(Expenditure.org_id == self.org_id).order_by(Expenditure.expenditure_date.asc())
            results = session.exec(statement)
            expenditures = results.fetchall() 
            return expenditures
        
        

class SelectPayeeExpenditures:
    def __init__(self,payee_id):
        self.payee_id = payee_id
    
    def count_all(self):
        return len(self.all())
    

    def all(self):
        with Session(engine) as session:
            statement = select(Expenditure).where(Expenditure.payee_id == self.payee_id).order_by(Expenditure.expenditure_date.asc())
            results = session.exec(statement)
            expenditures = results.fetchall() 
            return expenditures

    def sample(self):
        with Session(engine) as session:
            statement = select(Expenditure).where(Expenditure.payee_id == self.payee_id).order_by(Expenditure.expenditure_date.asc())
            results = session.exec(statement)
            expenditures = results.fetchall() 
            return expenditures         
        
        
class SelectSingleExpenditure:
    
    def __init__(self, expenditure_id):
        self.expenditure_id = expenditure_id
        
    def __str__(self):
        exp = self.get_expenditure()
        string = ''
        string += f"filer_name: {exp.expenditure_id}" + '\r\n'        
        string += f"filer_name: {exp.filer_name}" + '\r\n'
        string += f"amt: {exp.expenditure_amount}" + '\r\n'
        string += f"payee: {exp.payee_name}" + '\r\n'
        string += f"exp_date: {exp.expenditure_date}"    
        return string
    
    def get(self):
        with Session(engine) as session:
            statement = select(Expenditure).where(Expenditure.expenditure_id == self.expenditure_id).where(Expenditure.expenditure_id != 6760)
            results = session.exec(statement)
            # print(dir(results))
            expenditure = results.first() 
            return expenditure 


class SelectPppData:
    def __init__(self):              
        pass
    
    def count_all(self):
        return len(self.all())    
    
    def all(self):
        with Session(engine) as session:
            statement = select(PppData).where(PppData.borrowerstate == 'NE').limit(1000)
            # statement = select(PppData).order_by(PppData.receipt_date.asc())
            results = session.exec(statement)
            contributions = results.fetchall() 
            return contributions
    
class SelectContributions:
    def __init__(self):              
        pass
    
    def count_all(self):
        return len(self.all())
    
    def count_untweeted(self):
        return len(self.untweeted())
    
    def count_unbuilt(self):
        return len(self.unbuilt()) 
    
    def all(self):
        with Session(engine) as session:
            statement = select(Contribution).order_by(Contribution.receipt_date.asc())
            results = session.exec(statement)
            contributions = results.fetchall() 
            return contributions

    def last_1500(self):
        with Session(engine) as session:        
            statement = select(Contribution).limit(1500).order_by(Contribution.receipt_date.desc())
            results = session.exec(statement)
            contributions = results.fetchall() 
            return contributions 
        
    # def top_100_old(self):
    #     with Session(engine) as session:        
    #         statement = select(Contribution).limit(200).order_by(Contribution.receipt_amount.desc())
    #         results = session.exec(statement)
    #         contributions = results.fetchall() 
    #         return contributions 
        
    def top_500(self):
        backdate = date.today() + timedelta(days=-90)
        # print(today)
        with Session(engine) as session:        
            statement = select(Contribution).where(Contribution.receipt_date >= backdate).limit(500).order_by(Contribution.receipt_amount.desc())
            results = session.exec(statement)
            contributions = results.fetchall() 
            return contributions         
                                                    
            
    def first_tweeted(self):
        with Session(engine) as session:
            statement = (select(Contribution) 
                .where(Contribution.tweet_sent == 1) 
                .where(Contribution.tweet_id !="1506004750164185090") 
                .where(Contribution.tweet_id !="1506004903574966272") 
                .where(Contribution.tweet_id !="1506005056985853957") 
                .where(Contribution.tweet_id !="1506005210023731201") 
                .where(Contribution.tweet_id !="1506005362637369347") 
                .order_by(Contribution.tweet_id.asc())
            )                                                                                                        
            results = session.exec(statement)
            contributions = results.first() 
            return contributions         
                
                
        
        
    def unbuilt(self):
        with Session(engine) as session:    
            statement = select(Contribution).where(Contribution.tweet_message == None).order_by(Contribution.receipt_date.asc())
            results = session.exec(statement)
            contributions = results.fetchall() 
            return contributions
          
    def all_ids():
        with Session(engine) as session:
            statement = select(Contribution.receipt_id)
            results = session.exec(statement)
            rtn_results = results.fetchall() 
        return rtn_results                
    
class SelectSingleContribution:
    def __init__(self, receipt_id):
        self.receipt_id = receipt_id
    
    def __str__(self):
        con = self.get()
        string = ''
        string += f"contr_id: {con.receipt_id}" + '\r\n'        
        string += f"filer_name: {con.filer_name}" + '\r\n'
        string += f"org_id: {con.org_id}" + '\r\n'
        string += f"amt: {con.receipt_amount}" + '\r\n'
        string += f"payor: {con.payor_name}" + '\r\n'
        string += f"rcp_date: {con.receipt_date}"    
        return string
    
    def get(self):
        with Session(engine) as session:
            statement = select(Contribution).where(Contribution.receipt_id== self.receipt_id)
            results = session.exec(statement)
            # print(dir(results))
            expenditure = results.first() 
            return expenditure     
  
class SelectSingleContribtionTweetText:
    def __init__(self, tweet_text):
        self.tweet_text = tweet_text
    
    def __str__(self):
        con = self.get()
        string = ''
        string += f"contr_id: {con.receipt_id}" + '\r\n'        
        string += f"filer_name: {con.filer_name}" + '\r\n'
        string += f"org_id: {con.org_id}" + '\r\n'
        string += f"amt: {con.receipt_amount}" + '\r\n'
        string += f"payor: {con.payor_name}" + '\r\n'
        string += f"rcp_date: {con.receipt_date}"    
        return string
    
    def get(self):
        with Session(engine) as session:
            statement = select(Contribution).filter(self.tweet_text in Contribution.tweet_message)
            results = session.exec(statement)
            # print(dir(results))
            expenditure = results.first() 
            return expenditure       
  
  
  
class SelectOrgContributions:
    def __init__(self, org_id):              
        self.org_id = org_id
    
    def count_all(self):
        return len(self.all())
    
    def count_untweeted(self):
        return len(self.untweeted())
    
    def count_unbuilt(self):
        return len(self.unbuilt()) 
    
    def last_tweeted(self):
        with Session(engine) as session:
            statement = select(Contribution).where(Contribution.org_id == self.org_id).where(Contribution.tweet_id != None).order_by(Contribution.tweet_dt.desc())
            results = session.exec(statement)
            rtn_results = results.first() 
        return rtn_results
    
    def last_status_id(self):
        with Session(engine) as session:
            statement = select(Contribution).where(Contribution.org_id == self.org_id).where(Contribution.tweet_id != None).order_by(Contribution.tweet_id.desc())
            results = session.exec(statement)
            rtn_results = results.first() 
        return rtn_results  
    
    def first_status_id(self):
        with Session(engine) as session:
            statement = select(Contribution).where(Contribution.org_id == self.org_id).where(Contribution.tweet_id != None).order_by(Contribution.tweet_id.asc())
            results = session.exec(statement)
            rtn_results = results.first() 
        return rtn_results          
    
    def all(self):
        with Session(engine) as session:
            statement = select(Contribution).where(Contribution.org_id == self.org_id).order_by(Contribution.receipt_date.asc())
            results = session.exec(statement)
            contributions = results.fetchall() 
            return contributions
        
    def untweeted(self):
        with Session(engine) as session:
            statement = select(Contribution).where(Contribution.tweet_sent == 0).where(Contribution.org_id == self.org_id).order_by(Contribution.receipt_date.asc())
            results = session.exec(statement)
            contributions = results.fetchall() 
            return contributions   
        
    def unbuilt(self):
        with Session(engine) as session:    
            statement = select(Contribution).where(Contribution.tweet_message == None).where(Contribution.org_id == self.org_id).order_by(Contribution.receipt_date.asc())
            results = session.exec(statement)
            contributions = results.fetchall() 
            return contributions

  
class SelectPayorContributions:
    def __init__(self, payor_id):              
        self.payor_id = payor_id
    
    def count_all(self):
        return len(self.all())       
    
    def all(self):
        with Session(engine) as session:
            statement = select(Contribution).where(Contribution.payor_id == self.payor_id).order_by(Contribution.receipt_date.asc())
            results = session.exec(statement)
            contributions = results.fetchall() 
            return contributions

    def sample(self):
        with Session(engine) as session:
            statement = select(Contribution).where(Contribution.payor_id == self.payor_id).limit(50).order_by(Contribution.receipt_date.asc())
            results = session.exec(statement)
            contributions = results.fetchall() 
            return contributions          
  
class SelectContributionFilers:
    def __init__(self):
        pass
    
    def count(self):
        return len(self.all())
    
    def all(self):
        with Session(engine) as session:
            statement = select(ContributionFiler).order_by(ContributionFiler.receipt_count.desc())
            results = session.exec(statement)
            # print(dir(results))
            filers = results.fetchall()
            # for filer in results:
            #     print(filer.org_id)
            return filers   
        
    def unbuilt(self):
        with Session(engine) as session:
            statement = select(ContributionFiler).where(ContributionFiler.tweet_header_text == None)
            results = session.exec(statement)
            # print(dir(results))
            filers = results.fetchall()
            # for filer in results:
            #     print(filer.org_id)
            return filers           

    def untweeted(self):
        with Session(engine) as session:
            statement = select(ContributionFiler).where(ContributionFiler.tweet_header_id == None)
            results = session.exec(statement)            
            filers = results.fetchall()    
            return filers          
        
        
class SelectExpenditureFilers:
    def __init__(self):
        pass
    
    def count(self):                        
        return len(self.all())
    
    def all(self):
        with Session(engine) as session:
            statement = select(ExpenditureFiler)
            results = session.exec(statement)
            filers = results.fetchall()
            return filers 
        
    # def all_test(self):
    #     with Session(engine) as session:
    #         statement = select(ExpenditureFiler).where(ExpenditureFiler.org_id == 7626)
    #         results = session.exec(statement)
    #         filers = results.fetchall()
    #         return filers      
        
    def all_test(self):
        with Session(engine) as session:
            statement = select(ExpenditureFiler).where(or_(
                                                           ExpenditureFiler.org_id == 7397,                
                                                           ExpenditureFiler.org_id == 7417,
                                                           ExpenditureFiler.org_id == 7582,
                                                           ExpenditureFiler.org_id == 7688,
                                                           ExpenditureFiler.org_id == 7626,
                                                           ExpenditureFiler.org_id == 7491,
                                                           ExpenditureFiler.org_id == 7579,
                                                           ExpenditureFiler.org_id == 7339,
                                                           ExpenditureFiler.org_id == 7680,                                                         
                                                           ExpenditureFiler.org_id == 7347,
                                                           ExpenditureFiler.org_id == 7694,
                                                           ExpenditureFiler.org_id == 7432
                                                           )
                                                       )
            results = session.exec(statement)
            filers = results.fetchall()
            return filers                 
        
    def unbuilt(self):
        with Session(engine) as session:
            statement = select(ExpenditureFiler).where(ExpenditureFiler.tweet_header_text == None)
            results = session.exec(statement)
            filers = results.fetchall()
            return filers 

    def untweeted(self):
        with Session(engine) as session:
            statement = select(ExpenditureFiler).where(ExpenditureFiler.tweet_header_id == None)
            results = session.exec(statement)
            filers = results.fetchall()
            return filers    
        
    def untweeted(self):
        with Session(engine) as session:
            statement = select(ExpenditureFiler).where(ExpenditureFiler.tweet_header_id == None)
            results = session.exec(statement)
            filers = results.fetchall()
            return filers                                  
           
    
class SelectContributionFiler:
    def __init__(self, org_id):
        self.org_id = org_id
     
    def __str__(self):
        filer = self.get()
        string = ''
        string += f"org_id: {filer.org_id}" + '\r\n'
        string += f"name: {filer.filer_name}"
        return string
        
    def get(self):
        try:
            with Session(engine) as session:
                statement = select(ContributionFiler).where(ContributionFiler.org_id == self.org_id)
                results = session.exec(statement)
                # print(dir(results))
                filer = results.one()
                # for filer in results:
                #     print(filer.org_id)
                return filer
        except: 
            return None     

class SelectExpenditureFiler:
    def __init__(self, org_id):
        self.org_id = org_id
     
    def __str__(self):
        filer = self.get()
        string = ''
        string += f"org_id: {filer.org_id}" + '\r\n'
        string += f"name: {filer.filer_name}"
        return string
        
    def get(self):
        try:
            with Session(engine) as session:
                statement = select(ExpenditureFiler).where(ExpenditureFiler.org_id == self.org_id)
                results = session.exec(statement)
                # print(dir(results))
                filer = results.one()
                # for filer in results:
                #     print(filer.org_id)
                return filer
        except: 
            return None    
    

    
      
def main():
    today = date.today() + timedelta(days=-90)
    print(today)
    x = SelectPppData()
    y = x.all()
    for i in y:
        print(i)



      
if __name__ == "__main__":
    main()
    
