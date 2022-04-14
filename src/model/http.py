from pydantic import BaseModel

class Team(BaseModel):
    name: str
    abbrev: str
    winMultiplier: float
    elo: str

class MatchesResponse(BaseModel):
    date: str
    event: str
    team1: Team
    team2: Team

class AppInfo(BaseModel):
    appName: str
    status: str