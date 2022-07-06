from fastapi import FastAPI
import query

app = FastAPI()

@app.get("/users/basics/{username}")
async def basics(username: str):
    reddit = query.connectToReddit()
    return query.getBasics(reddit, username)

@app.get("/users/advanced/{username}")
async def advanced(username: str):
    reddit = query.connectToReddit()
    return query.getTextStatistics(query.getComments(reddit, username))