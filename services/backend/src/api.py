"""
This script contains methods for getting data through API calls.
"""

import json
import requests
from fastapi import HTTPException
import praw
from decouple import config


async def getBasicData(username: str):
    userData = json.loads(requests.get('https://www.reddit.com/user/{}/about.json'.format(username), headers={'User-agent': config('USER_AGENT')}).content)
    if "error" in userData:
        raise HTTPException(status_code=404, detail='User not found!')
    return userData

async def getNumSubmissions(username: str, type: str):
    submissionsData = json.loads(requests.get('https://api.pushshift.io/reddit/search/{}/?author={}&metadata=true&size=0'.format(type, username)).content)
    return submissionsData["metadata"]["total_results"]

async def getCommentList(username: str):
    commentList = json.loads(requests.get('https://api.pushshift.io/reddit/comment/search/?author={}&sort=desc&sort_type=created_utc'.format(username)).content)
    return commentList["data"]
