from fastapi import APIRouter
from fastapi import FastAPI

from todos import todo_router

app = FastAPI()
router = APIRouter()


@app.get("/")
async def welcome() -> dict:
    return {"message": "Hello, World!"}


@router.get("/hello")
async def say_hello() -> dict:
    return {"message": "Hello"}


app.include_router(todo_router)
