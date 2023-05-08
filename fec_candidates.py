import os
import requests
from dotenv import load_dotenv
from rich import inspect, print
from dataclasses import dataclass
from dataclasses_json import dataclass_json
import polars as pl
import json
from db_models import FecCandidates
from sqlmodel.sql.expression import Select, SelectOfScalar
from db_config import DbConfig
from typing import Optional, List, Union
from dataclasses import dataclass, field, MISSING
from db_dal_classes import SelectOneFecCandidate

from sqlmodel import Field, Session, SQLModel, create_engine, select, or_, insert
engine = db_engine = DbConfig.get_central_engine()

SelectOfScalar.inherit_cache = True  # type: ignore
Select.inherit_cache = True  # type: ignore


class InsertCandidate:
    def __init__(self,dc_object):
        self.dc_object = dc_object
        # self.org_id = org_id
        pass

    def check_insert(self):
        x = SelectOneFecCandidate(candidate_id=self.dc_object.candidate_id)
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
                    candidate = FecCandidates(
                            active_through = self.dc_object.active_through
                            ,candidate_id = self.dc_object.candidate_id
                            ,candidate_inactive = self.dc_object.candidate_inactive
                            ,candidate_status = self.dc_object.candidate_status
                            ,cycles = self.dc_object.cycles
                            ,district = self.dc_object.district
                            ,district_number = self.dc_object.district_number
                            ,election_districts = self.dc_object.election_districts
                            ,election_years = self.dc_object.election_years
                            ,federal_funds_flag = self.dc_object.federal_funds_flag
                            ,first_file_date = self.dc_object.first_file_date
                            ,flags = self.dc_object.flags
                            ,has_raised_funds = self.dc_object.has_raised_funds
                            ,inactive_election_years = self.dc_object.inactive_election_years
                            ,incumbent_challenge = self.dc_object.incumbent_challenge
                            ,incumbent_challenge_full = self.dc_object.incumbent_challenge_full
                            ,last_f2_date = self.dc_object.last_f2_date
                            ,last_file_date = self.dc_object.last_file_date
                            ,load_date = self.dc_object.load_date
                            ,name = self.dc_object.name
                            ,office = self.dc_object.office
                            ,office_full = self.dc_object.office_full
                            ,party = self.dc_object.party
                            ,party_full = self.dc_object.party_full
                            ,state = self.dc_object.state
                    )
                    session.add(candidate)
                    session.commit()

            except Exception as e:
                raise

load_dotenv()
API_KEY = os.getenv("API_KEY")

payload = {'api_key': API_KEY}

BASE_URL = 'https://api.open.fec.gov/v1/'
URL = BASE_URL + 'candidates/search/'

state = 'NE'

@dataclass_json
@dataclass
class Candidate:
    active_through: int
    candidate_id: str
    candidate_inactive: bool
    candidate_status: str
    cycles: List[int]
    district: Optional[str]
    district_number: Optional[int]
    election_districts: Optional[List[str]] = field(default=None, init=False)
    election_years: List[int]
    federal_funds_flag: bool
    first_file_date: Optional[str] = field(default=None, init=False)
    flags: Optional[List[int]] = field(default=None, init=False)
    has_raised_funds: bool
    inactive_election_years: Optional[List[int]] = field(default=None, init=False)
    incumbent_challenge: Optional[str]
    incumbent_challenge_full: Optional[str]
    last_f2_date: Optional[str] = field(default=None, init=False)
    last_file_date: Optional[str] = field(default=None, init=False)
    load_date: Optional[str] = field(default=None, init=False)
    name: str
    office:str
    office_full: str
    party: Optional[str]
    party_full: Optional[str]
    state: str



def working_main():
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

def working_main_conductor():
    for page in working_main():
        for x in page['results']:
            inspect(x)
            input('x')
            z =json.dumps(x)
            # print(z)
            # input('stop')
            y = Candidate.from_json(z)
            print(y)
            go_thing = InsertCandidate(dc_object=y)
            go_thing.insert()

working_main_conductor()
