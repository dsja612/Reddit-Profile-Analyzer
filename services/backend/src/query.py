"""
This script executes API calls and constructs data for the front-end.
"""

from datetime import datetime
from string import punctuation

from decouple import config
import json
from . import api
from . import preprocess
import praw
from decouple import config
from fastapi import HTTPException

async def main(username: str): 

    reddit = praw.Reddit(client_id = config('CLIENT_ID'),
                     client_secret = config('CLIENT_SECRET'),
                     user_agent = config('USER_AGENT'))

    payload = {}
    
    try:
        # Get general information
        payload['basic_data'] = await api.getBasicData(username)

        # Get no. of comments
        payload['num_comments'] = await api.getNumSubmissions(username, 'comment')

        # Get no. of submissions
        payload['num_submissions'] = await api.getNumSubmissions(username, 'submission')

        ### PRAW
        comments = reddit.redditor(username).comments.new(limit=1000)

        # Get body of comments
        comment_list = []
        top_subreddits = {}
        for comment in comments:
            comment_list.append(comment.body)
            key = comment.subreddit.display_name
            top_subreddits[key] = top_subreddits[key] + 1 if key in top_subreddits else 1

        # Get top subreddits commented on
        payload['top_subreddits'] = top_subreddits

        # Get top words sorted in ascending order
        payload['top_words'] = await preprocess.preprocess_comments(comment_list)

        return payload

    except Exception as err:
        raise err
