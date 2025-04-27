from backend.database import SessionLocal
from backend.models import User, Game

db = SessionLocal()

def create_user(username: str, password: str):
    user = User(username=username, password=password)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

def authenticate_user(username: str, password: str):
    return db.query(User).filter(User.username == username, User.password == password).first()

def create_game():
    game = Game(fen="start")
    db.add(game)
    db.commit()
    db.refresh(game)
    return game

def save_game(player: str, opponent: str, result: str, moves: str):
    game = Game(player=player, opponent=opponent, result=result, moves=moves)
    db.add(game)
    db.commit()
    db.refresh(game)
    return game

def get_games(player: str):
    return db.query(Game).filter(Game.player == player).order_by(Game.created_at.desc()).all()