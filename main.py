from fastapi import FastAPI, Depends,HTTPException
from sqlalchemy.orm import Session
from typing import List
from db import SessionLocal
from models import Cricketer
from schemas import CRICKET_RECORD,PLAYER_DETAILED,PLAYER_DETAILED_INSERT,PLAYER_DETAILED_UPDATE


from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],      # sab origins allow
    allow_credentials=True,
    allow_methods=["*"],      # GET, POST, PUT, DELETE
    allow_headers=["*"],
)




def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
# all player data
@app.get("/players", response_model=List[CRICKET_RECORD])
def get_all_players(db: Session = Depends(get_db)):
    return db.query(Cricketer).all()


# Single player name

@app.get("/players/name/{player_name}", response_model=PLAYER_DETAILED)
def get_player_by_name(player_name: str, db: Session = Depends(get_db)):
    player = (db.query(Cricketer).filter(Cricketer.name == player_name).first()
    )

    if not player:
        raise HTTPException(
            status_code=404,
            detail=f"Player with name '{player_name}' not found"
        )

    return player



# Update player detailed 
@app.put("/players/name/{player_name}", response_model=PLAYER_DETAILED)
def update_player_by_name(
    player_name: str,
    player: PLAYER_DETAILED_UPDATE,
    db: Session = Depends(get_db)
):
    db_player = db.query(Cricketer).filter(
        Cricketer.name == player_name
    ).first()

    if not db_player:
        raise HTTPException(status_code=404, detail="Player not found")

    if player.country is not None:
        db_player.country = player.country

    if player.role is not None:
        db_player.role = player.role

    if player.batting_style is not None:
        db_player.batting_style = player.batting_style

    if player.bowling_style is not None:
        db_player.bowling_style = player.bowling_style

    if player.matches is not None:
        db_player.matches = player.matches

    if player.runs is not None:
        db_player.runs = player.runs

    if player.average is not None:
        db_player.average = player.average

    if player.wickets is not None:
        db_player.wickets = player.wickets

    if player.strike_rate is not None:
        db_player.strike_rate = player.strike_rate

    if player.economy is not None:
        db_player.economy = player.economy

    if player.best_score is not None:
        db_player.best_score = player.best_score

    if player.is_active is not None:
        db_player.is_active = player.is_active

    if player.join_date is not None:
        db_player.join_date = player.join_date

    db.commit()
    db.refresh(db_player)

    return db_player



# player ka name se delete 
@app.delete("/players/{id}")
def delete_player(id: str, db: Session = Depends(get_db)):
    player = db.query(Cricketer).filter(Cricketer.id == id).first()

    if not player:
        raise HTTPException(status_code=404,detail="Player not found")

    db.delete(player)
    db.commit()
    return {"message": "Player deleted successfully"}



# post
# Create new player
@app.post("/players/insert", response_model=PLAYER_DETAILED)
def create_player(
    player: PLAYER_DETAILED_INSERT,
    db: Session = Depends(get_db)
):
    existing_player = db.query(Cricketer).filter(
        Cricketer.name == player.name
    ).first()

    if existing_player:
        raise HTTPException(
            status_code=400,
            detail="Player already exists"
        )

    new_player = Cricketer(
        name=player.name,
        country=player.country,
        role=player.role,
        batting_style=player.batting_style,
        bowling_style=player.bowling_style,
        matches=player.matches,
        runs=player.runs,
        average=player.average,
        wickets=player.wickets,
        strike_rate=player.strike_rate,
        economy=player.economy,
        best_score=player.best_score,
        is_active=player.is_active,
        join_date=player.join_date
    )

    db.add(new_player)
    db.commit()
    db.refresh(new_player)

    return new_player
