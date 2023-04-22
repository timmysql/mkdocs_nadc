import requests
from rich import inspect, print 
from dataclasses import dataclass
from dataclasses_json import dataclass_json
import polars as pl
import json
from db_models import ScheduleA
from sqlmodel.sql.expression import Select, SelectOfScalar
from db_config import DbConfig

from sqlmodel import Field, Session, SQLModel, create_engine, select, or_, insert
engine = db_engine = DbConfig.get_central_engine()
    
SelectOfScalar.inherit_cache = True  # type: ignore
Select.inherit_cache = True  # type: ignore       


class InsertScheduleA:
    def __init__(self,dc_object):
        self.dc_object = dc_object
        # self.org_id = org_id
        pass
    def insert(self):
        try:
            with Session(engine) as session:
                schedule_a = ScheduleA(
                        count = self.dc_object.count
                        ,cycle = self.dc_object.cycle
                        ,committee_id = self.dc_object.committee_id
                        ,total = self.dc_object.total
                        ,state = self.dc_object.state
                        ,state_full = self.dc_object.state_full
                    
                )
                session.add(schedule_a)
                session.commit()
            #     # print(dir(results))
            #     filers = results.fetchall()
            #     # for filer in results:
            #     #     print(filer.org_id)
            # return filers
        except Exception as e:
            raise        
            # return None       


API_KEY = '3A1Dq0EgwLLL7zXVJPKlU2XUS5AXxknVacIkDrX3'



payload = {'api_key': API_KEY}

BASE_URL = 'https://api.open.fec.gov/v1/'
URL = BASE_URL + 'schedules/schedule_a/by_state/'


@dataclass_json
@dataclass
class DcScheduleA:
    count: int
    cycle: int
    committee_id: str
    total: float
    state: str
    state_full: str



def working_main():
    session = requests.Session()
    payload = {'api_key': API_KEY,'state':'NE','page':1,'per_page':50}      
    first_page = session.get(URL,params=payload).json()
    num_pages = first_page['pagination']['pages']    
    yield first_page
    
    
    

    for page in range(2, num_pages + 1):    
        # print(page)
        next_page = session.get(URL, params={'api_key': API_KEY,'state':'NE','page':page,'per_page':50}).json()
        # print(next_page['pagination'])        
        yield next_page

def working_main_conductor():
    for page in working_main():
        for x in page['results']:
            # print(x)
            z =json.dumps(x)
            y = DcScheduleA.from_json(z)            
            print(y)
            go_thing = InsertScheduleA(dc_object=y)
            go_thing.insert()
        
working_main_conductor()  