from pydantic import BaseModel,field_validator
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
    @field_validator("*", mode="before")
    def empty_to_none(cls, v):
        if v in ("", " ", None):
            return None
        return v

    class Config:
        from_attributes = True


class PLAYER_DETAILED_INSERT(BaseModel):
    name: str
    country: Optional[str] = None
    role: Optional[str]=None
    batting_style: Optional[str]=None
    bowling_style: Optional[str]=None


    matches: Optional[int]=0
    runs: Optional[int]=0

    average: Optional[float]=0
    wickets: Optional[int]=0
    strike_rate: Optional[float]=0
    economy: Optional[float]=0

    best_score: Optional[str]=None
    is_active: Optional[bool] = True
    join_date: Optional[date]=None


class PLAYER_DETAILED_UPDATE(BaseModel):
    name: str
    country: Optional[str]=None     

    role: Optional[str]=None
    batting_style: Optional[str]=None
    bowling_style: Optional[str]=None

    matches: Optional[int]
    runs: Optional[int]

    average: Optional[float]
    wickets: Optional[int]
    strike_rate: Optional[float]
    economy: Optional[float]

    best_score: Optional[str]
    is_active: Optional[bool]=None
    join_date: Optional[date]= None

    # String Validate
    @field_validator(
        "name","country","role","batting_style","bowling_style","best_score",
        mode="before"
    )
    # String Validation
    def clean_strings(cls,v):
        if v in (""," "):
            return None
        return v
    # numeric validataion
    @field_validator( "matches", "runs", "average", "wickets",
        "strike_rate", "economy",
        mode = "before")
    def clean_num(cls,v):
        if v in (""," ",None):
            return None
        return v
    @field_validator("join_date", mode="before")
    def data_clean(cls , v):
        if v in (""," ",None):
            return None

        return v
    


class PLAYER_DETAILED(CRICKET_RECORD):
    pass




# Ml Model schema 
class ML_MODEL(BaseModel):
    matches: int
    runs: int
    average: float
    wickets: int


# JWT
from pydantic import BaseModel

class RegisterSchema(BaseModel):
    username: str
    password: str
    role: str

class LoginSchema(BaseModel):
    username: str
    password: str