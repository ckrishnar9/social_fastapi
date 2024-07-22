from fastapi import FastAPI
from app.api.endpoints import auth, users, posts, comments

app = FastAPI()

app.include_router(auth.router, prefix="/auth", tags=["auth"])
app.include_router(users.router, prefix="/users", tags=["users"])
app.include_router(posts.router, prefix="/posts", tags=["posts"])
app.include_router(comments.router, prefix="/comments", tags=["comments"])

@app.get("/")
def read_root():
    return {"Hello": "Krishna!"}
