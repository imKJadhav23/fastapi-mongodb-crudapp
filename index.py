from fastapi import FastAPI
from pydantic import BaseModel
from routes.student import student_router


app=FastAPI()


app.include_router(student_router)