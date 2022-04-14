import string
import sys
from os import path
from fastapi import FastAPI
from typing import List

sys.path.append(path.abspath('.'))

from src.data.schedule_with_rating import get_schedule_with_rating
from src.model.http import AppInfo, MatchesResponse

app = FastAPI()

@app.get('/', response_model=AppInfo)
def home():
    return { 
        'appName': 'League of Legends betting API', 
        'status': 'OK' 
    }

@app.get('/matches', response_model=List[MatchesResponse])
def read_root(startDate, endDate, league):
    data = get_schedule_with_rating('EU', startDate, endDate, league)
    return data