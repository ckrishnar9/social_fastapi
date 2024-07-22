from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from app.schemas import user as user_schemas
from app.crud import user as user_crud
from app.core import security
from app.db.session import get_db

router = APIRouter()

@router.post("/login", response_model=user_schemas.Token)
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    db_user = user_crud.authenticate_user(db, username=form_data.username, password=form_data.password)
    if not db_user:
        raise HTTPException(status_code=400, detail="Invalid Username and Password")
    access_token = security.create_access_token(data={"sub": db_user.username})
    return {"access_token": access_token, "token_type": "bearer"}

@router.post("/register", response_model=user_schemas.User)
def register(user: user_schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = user_crud.get_user_by_username(db, username=user.username)
    if db_user:
        raise HTTPException(status_code=400, detail="Username is already registered")
    return user_crud.create_user(db=db, user=user)