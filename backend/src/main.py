from fastapi import FastAPI

import query

app = FastAPI()

@app.get("/users/{username}")
async def main(username: str):
    try:
        return await query.main(username)
    except Exception as err:
        raise err
