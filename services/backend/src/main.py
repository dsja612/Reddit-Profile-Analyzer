from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from . import query

app = FastAPI()

@app.get("/users/{username}")
async def main(username: str):
    try:
        return await query.main(username)
    except Exception as err:
        raise err
