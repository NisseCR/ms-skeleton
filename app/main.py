from fastapi import Depends, FastAPI

from .dependencies import get_token_header
from .routers import packages

app = FastAPI()
app.include_router(packages.router)


@app.get("/")
async def root():
    return {"message": "I'm a data-reader!"}