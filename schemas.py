from pydantic import BaseModel
from typing import Optional
from datetime import date


class CRICKET_RECORD(BaseModel):
    id: int

    name: Optional[str]
    country: Optional[str]
    role: Optional[str]
    batting_style: Optional[str]
    bowling_style: Optional[str]

    matches: Optional[int]
    runs: Optional[int]

    average: Optional[float]
    wickets: Optional[int]
    strike_rate: Optional[float]
    economy: Optional[float]

    best_score: Optional[str]
    is_active: Optional[bool] = True
    join_date: Optional[date]

    class Config:
        from_attributes = True


class PLAYER_DETAILED_INSERT(BaseModel):
    name: str
    country: str
    role: str
    batting_style: str
    bowling_style: str

    matches: Optional[int]
    runs: Optional[int]

    average: Optional[float]
    wickets: Optional[int]
    strike_rate: Optional[float]
    economy: Optional[float]

    best_score: Optional[str]
    is_active: Optional[bool] = True
    join_date: Optional[date]


class PLAYER_DETAILED_UPDATE(BaseModel):
    name: Optional[str]
    country: Optional[str]
    role: Optional[str]
    batting_style: Optional[str]
    bowling_style: Optional[str]

    matches: Optional[int]
    runs: Optional[int]

    average: Optional[float]
    wickets: Optional[int]
    strike_rate: Optional[float]
    economy: Optional[float]

    best_score: Optional[str]
    is_active: Optional[bool]
    join_date: Optional[date]


class PLAYER_DETAILED(CRICKET_RECORD):
    pass




# Ml Model schema 
class ML_MODEL(BaseModel):
    matches: int
    runs: int
    average: float
    wickets: int
