"""
This script contains methods for getting data through API calls.
"""

import requests
import json

def getNumSubmissions(username: str, type: str):
    userInfo = json.loads(requests.get('https://api.pushshift.io/reddit/search/{}/?author={}&metadata=true&size=0'.format(type, username)).content)
    return userInfo["metadata"]["total_results"]

def getCommentList(username: str):
    commentList = json.loads(requests.get('https://api.pushshift.io/reddit/comment/search/?author={}&sort=desc&sort_type=created_utc'.format(username)).content)
    return commentList["data"]