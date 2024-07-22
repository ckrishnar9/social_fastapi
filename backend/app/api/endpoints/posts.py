from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas import post as post_schemas
from app.schemas import user as user_schemas
from app.crud import post as post_crud
from app.db.session import get_db
from app.utils.dependencies import get_current_user

router = APIRouter()

@router.get("/", response_model=list[post_schemas.Post])
def read_posts(skip: int = 0, limit: int = 10, db: Session= Depends(get_db)):
    posts = post_crud.get_posts(db, skip=skip, limit=limit)
    return posts

@router.post("/", response_model=list[post_schemas.Post])
def create_post(post: post_schemas.PostCreate, db: Session = Depends(get_db), current_user: user_schemas.User = Depends(get_current_user)):
    return post_crud.create_post(db=db, post=post, user_id=current_user.id)


    