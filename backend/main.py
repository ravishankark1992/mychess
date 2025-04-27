from fastapi import FastAPI, HTTPException
from backend.database import SessionLocal, engine
from backend.models import Base, User, Game
from backend.crud import create_user, authenticate_user, create_game

from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime
from backend.database import Base

class Game(Base):
    __tablename__ = "games"
    id = Column(Integer, primary_key=True, index=True)
    player = Column(String)         # Player name
    opponent = Column(String)       # Opponent (human or AI)
    result = Column(String)         # win/loss/draw
    moves = Column(String)          # PGN or moves
    created_at = Column(DateTime, default=datetime.utcnow)


Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.post("/login")
def login(username: str, password: str):
    user = authenticate_user(username, password)
    if not user:
        raise HTTPException(status_code=400, detail="Invalid credentials")
    return {"token": f"{user.username}-token"}

@app.post("/register")
def register(username: str, password: str):
    return create_user(username, password)

@app.post("/newgame")
def new_game():
    return create_game()

@app.get("/lessons")
def get_lessons():
    return [{"title": "Control Center"}, {"title": "Develop Pieces"}]
