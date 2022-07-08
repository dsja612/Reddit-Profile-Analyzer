from fastapi import FastAPI
import query
from fastapi import HTTPException

app = FastAPI()

@app.get("/users/{username}")
def main(username: str):
    #try:
    return query.main(username)
    #except:
        #raise HTTPException(status_code=404, detail="User doesn't exist!")