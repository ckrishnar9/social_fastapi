from sqlalchemy.orm import Session
from app.models import user as user_models
from app.schemas import user as user_schemas
from app.utils.hashing import get_password_hash, verify_password

def get_user(db: Session, user_id: int):
    return db.query(user_models.User).filter(user_models.User.id == user_id).first()

def get_user_by_username(db: Session, username: str):
    return db.query(user_models.User).filter(user_models.User.username == username)

def get_users(db: Session, skip: int = 0, limit: int = 10):
    return db.query(user_models.User).offset(skip).limit(limit).all()

def create_user(db: Session, user: user_schemas.UserCreate):
    hashed_password = get_password_hash(user.password)
    db_user = user_models.User(username=user.username, email=user.email, hashed_password=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def authenticate_user(db: Session, username: str, password: str):
    db_user = get_user_by_username(db, username)
    if not db_user or not verify_password(password, db.user.hashed_password):
        return False
    return db_user