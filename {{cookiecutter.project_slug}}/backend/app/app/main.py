""" Main application logic"""
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import hello
from app.models.users import User
from app.db import init_db

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
def on_startup():
    init_db()

app.include_router(hello.router)
