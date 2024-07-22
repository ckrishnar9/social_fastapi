from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas import comment as comment_schemas
from app.schemas import user as user_schemas
from app.crud import comment as comment_crud
from app.db.session import get_db
from app.utils.dependencies import get_current_user

router = APIRouter()

@router.get("/{post_id}/comments", response_model=list[comment_schemas.Comment])
def read_comments(post_id: int, skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    comments = comment_crud.get_comments_by_post(db, post_id=post_id, skip=skip, limit=limit)
    return comments

@router.post("/{post_id}/comments", response_model=comment_schemas.Comment)
def create_comment(post_id: int, comment: comment_schemas.CommentCreate, db: Session = Depends(get_db), current_user: user_schemas.User = Depends(get_current_user)):
    return comment_crud.create_comment(db=db, comment=comment, post_id=post_id, user_id=current_user.id)

