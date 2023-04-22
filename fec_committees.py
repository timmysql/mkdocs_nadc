import requests
from rich import inspect, print 
from dataclasses import dataclass
from dataclasses_json import dataclass_json
import polars as pl
import json
from db_models import FecCommittees
from sqlmodel.sql.expression import Select, SelectOfScalar
from db_config import DbConfig
from typing import Optional, List, Union
from dataclasses import dataclass, field, MISSING
from db_dal_classes import SelectOneFecCommittee, SelectFecCandidates
from sqlmodel import Field, Session, SQLModel, create_engine, select, or_, insert
engine = db_engine = DbConfig.get_central_engine()
    
SelectOfScalar.inherit_cache = True  # type: ignore
Select.inherit_cache = True  # type: ignore       


class InsertCommittee:
    def __init__(self,dc_object):
        self.dc_object = dc_object
        # self.org_id = org_id
        pass
    
    def check_insert(self):
        x = SelectOneFecCommittee(committee_id=self.dc_object.committee_id)
        result = x.select()
        if result:
            result = True
        else:
            result = False
        return result       
    
    def insert(self):
        if self.check_insert() == False:        
            try:
                with Session(engine) as session:
                    committee = FecCommittees(
                        affiliated_committee_name = self.dc_object.affiliated_committee_name,
                        candidate_ids = self.dc_object.candidate_ids,
                        committee_id = self.dc_object.committee_id,
                        committee_type = self.dc_object.committee_type,
                        committee_type_full = self.dc_object.committee_type_full,
                        cycles = self.dc_object.cycles,
                        designation = self.dc_object.designation,
                        designation_full = self.dc_object.designation_full,
                        filing_frequency = self.dc_object.filing_frequency,
                        first_f1_date = self.dc_object.first_f1_date,
                        first_file_date = self.dc_object.first_file_date,
                        last_f1_date = self.dc_object.last_f1_date,
                        last_file_date = self.dc_object.last_file_date,
                        name = self.dc_object.name,
                        organization_type = self.dc_object.organization_type,
                        organization_type_full = self.dc_object.organization_type_full,
                        party = self.dc_object.party,
                        party_full = self.dc_object.party_full,
                        sponsor_candidate_ids = self.dc_object.sponsor_candidate_ids,
                        sponsor_candidate_list = self.dc_object.sponsor_candidate_list,
                        state = self.dc_object.state,
                        treasurer_name = self.dc_object.treasurer_name                  
                    )
                    session.add(committee)
                    session.commit()

            except Exception as e:
                raise        
   


API_KEY = '3A1Dq0EgwLLL7zXVJPKlU2XUS5AXxknVacIkDrX3'



payload = {'api_key': API_KEY}

BASE_URL = 'https://api.open.fec.gov/v1/'
URL = BASE_URL + 'committees/'

state = 'NE'


@dataclass_json
@dataclass
class Committees:
    affiliated_committee_name: Optional[str] = field(default=None, init=False) 
    candidate_ids: List[str]
    committee_id: str
    committee_type: str
    committee_type_full: str
    cycles: List[int]
    designation: Optional[str]
    designation_full: Optional[str]
    filing_frequency: str
    first_f1_date: Optional[str]
    first_file_date: str
    last_f1_date: Optional[str]
    last_file_date: str
    name: str
    organization_type: Optional[str]
    organization_type_full: Optional[str]
    party: Optional[str] = field(default=None, init=False) 
    party_full: Optional[str] = field(default=None, init=False) 
    sponsor_candidate_ids: Optional[List[str]] = field(default=None, init=False)     
    sponsor_candidate_list: Optional[List[str]] = field(default=None, init=False)  
    state: str
    treasurer_name: Optional[str]
        
   

def state_main():
    session = requests.Session()
    payload = {'api_key': API_KEY,'state':state,'page':1,'per_page':50}      
    first_page = session.get(URL,params=payload).json()
    num_pages = first_page['pagination']['pages']    
    yield first_page
    
        
    for page in range(2, num_pages + 1):    
        # print(page)
        next_page = session.get(URL, params={'api_key': API_KEY,'state':state,'page':page,'per_page':50}).json()
        # print(next_page['pagination'])        
        yield next_page

def state_conductor():
    for page in state_main():
        for x in page['results']:
            # print(x)
            z =json.dumps(x)
            # print(z)
            # input('stop')
            y = Committees.from_json(z)            
            # print(y)
            go_thing = InsertCommittee(dc_object=y)
            go_thing.insert()
            
            
            
def candidate_main(candidate_id):
    session = requests.Session()
    payload = {'api_key': API_KEY,'candidate_id':candidate_id,'page':1,'per_page':50}      
    first_page = session.get(URL,params=payload).json()
    num_pages = first_page['pagination']['pages']    
    yield first_page
    
        
    for page in range(2, num_pages + 1):    
        # print(page)
        next_page = session.get(URL, params={'api_key': API_KEY,'state':state,'page':page,'per_page':50}).json()
        # print(next_page['pagination'])        
        yield next_page 
        
def candidate_conductor():
    x = SelectFecCandidates()
    candidates = x.all()
    for candidate in candidates:
        # page = candidate_main(candidate_id=candidate.candidate_id)    
        for page in candidate_main(candidate_id=candidate.candidate_id):
            for x in page['results']:
                # print(x)
                z =json.dumps(x)
                # print(z)
                # input('stop')
                y = Committees.from_json(z)            
                # print(y)
                go_thing = InsertCommittee(dc_object=y)
                go_thing.insert()                   
    
   
   
   
if __name__ == '__main__': 
    candidate_conductor()    
    
    state_conductor()
       
    # x = SelectFecCandidates()
    # candidates = x.all()
    # for candidate in candidates:
    #     working_candidates(candidate_id=candidate.candidate_id)
        # print(candidate.name, candidate.candidate_id)