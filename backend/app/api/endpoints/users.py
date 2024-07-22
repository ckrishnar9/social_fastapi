from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas import user as user_schemas
from app.crud import user as user_crud
from app.db.session import get_db
from app.utils.dependencies import get_current_user

router = APIRouter()

@router.get("/", response_model=list[user_schemas.User])
def read_users(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    users = user_crud.get_users(db, skip=skip, limit=limit)
    return users

@router.get("/{user_id}", response_model=user_schemas.User)
def read_user(user_id: int, db: Session= Depends(get_db)):
    db_user = user_crud.get_user(db, user_id=user_id)
    if db_user in None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user
