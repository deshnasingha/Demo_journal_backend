
from fastapi import FastAPI
from backend.router import journal

app= FastAPI()

app.include_router(journal.router, prefix= "/journal", tags=["Journal"])


