"""
This script contains methods for getting data through API calls.
"""

import json
import requests
from fastapi import HTTPException
from decouple import config
import time


async def getBasicData(username: str) -> dict:
    start = time.time()
    print("getBasicData start")
    userData = json.loads(requests.get('https://www.reddit.com/user/{}/about.json'.format(username), headers={'User-agent': config('USER_AGENT')}).content)
    if "error" in userData:
        raise HTTPException(status_code=404, detail='User not found!')
    elif "message" in userData:
        raise HTTPException(status_code=429, detail='Too many requests are sent to Reddit!')
    elif "is_suspended" in userData["data"]:
        raise HTTPException(status_code=404, detail='User is suspended!')
    else:
        print("getBasicData ended at {}".format(time.time() - start))
        return userData

async def getNumSubmissions(username: str, type: str) -> int:
    start = time.time()
    print("getNumSubmissions start")
    submissionsData = json.loads(requests.get('https://api.pushshift.io/reddit/search/{}/?author={}&metadata=true&size=0'.format(type, username)).content)
    print("getNumSubmissions ended at {}".format(time.time() - start))    
    return submissionsData["metadata"]["total_results"]

# async def getCommentList(username: str):
#     start = time.time()
#     print("getNumSubmissions start")
#     commentList = json.loads(requests.get('https://api.pushshift.io/reddit/comment/search/?author={}&sort=desc&sort_type=created_utc'.format(username)).content)
#     print("getNumSubmissions ended at {}".format(time.time() - start))   
#     return commentList["data"]
