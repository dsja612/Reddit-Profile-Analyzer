"""
This script executes API calls and constructs data for the front-end.
"""

import time
from decouple import config
import asyncpraw
from . import api
from . import preprocess
from decouple import config
from fastapi import HTTPException
from datetime import datetime

async def main(username: str) -> dict: 

    reddit = asyncpraw.Reddit(client_id = config('CLIENT_ID'),
                     client_secret = config('CLIENT_SECRET'),
                     user_agent = config('USER_AGENT'))

    payload = {}
    
    try:
        # Get general information & check if username exists
        payload['basic_data'] = await api.getBasicData(username)

        ### ASYNCPRAW
        start = time.time()
        print("Starting PRAW query for /u/{}".format(username))
        user = await reddit.redditor(username)
        comments = user.comments.new(limit=int(config('COMMENTS_LIMIT')))

        # Get info from comments
        comment_list = []
        comment_sentiment = []
        top_subreddits = {}
        comment_freq_hr = dict.fromkeys(["00", "01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23"], 0)
        comment_freq_days = dict.fromkeys(["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"], 0)

        # What to process for each comment
        async for comment in comments:
            # Get freqdist of comments in subreddits
            comment_list.append(comment.body)
            key = comment.subreddit.display_name
            top_subreddits[key] = top_subreddits[key] + 1 if key in top_subreddits else 1

            # Get freqdist of hr (e.g 00, 12, 23) comments were made
            hr = str(datetime.utcfromtimestamp(comment.created_utc).strftime('%H'))
            comment_freq_hr[hr] = comment_freq_hr[hr] + 1

            # Get freqdist of day (e.g. Mon, Tue) comments were made 
            day = str(datetime.utcfromtimestamp(comment.created_utc).strftime('%a'))
            comment_freq_days[day] = comment_freq_days[day] + 1

            sentiment = await preprocess.sentiment_analyzer(comment.body)
            comment_sentiment.append(sentiment)

        end = time.time()
        print("PRAW query finished in {} seconds".format(end - start))

        await reddit.close()

        payload['comment_sentiment'] = comment_sentiment
        payload['comment_freq'] = {}
        payload['comment_freq']['hrs'] = {}
        payload['comment_freq']['days'] = {}
        payload['comment_freq']['hrs']['keys'] = []
        payload['comment_freq']['hrs']['values'] = []
        payload['comment_freq']['days']['keys'] = []
        payload['comment_freq']['days']['values'] = []
        
        if len(comment_list) != 0:
            # Get top words sorted in ascending order
            payload['top_words'] = await preprocess.preprocess_comments(comment_list)
            
            # Sort top subreddits commented on
            top_subreddits = await preprocess.dict_sort(top_subreddits)
            payload['top_subreddits'] = top_subreddits

            # Comment frequency data in ApexCharts format
            payload['comment_freq']['hrs']['keys'] = list(comment_freq_hr.keys())
            payload['comment_freq']['hrs']['values'] = list(comment_freq_hr.values())
            payload['comment_freq']['days']['keys'] = list(comment_freq_days.keys())
            payload['comment_freq']['days']['values'] = list(comment_freq_days.values())

        else:
            # Assign comment items as blank
            payload['top_words'] = {}
            payload['top_subreddits'] = {}
        

        # Get no. of comments
        payload['num_comments'] = await api.getNumSubmissions(username, 'comment')

        # Get no. of submissions
        payload['num_submissions'] = await api.getNumSubmissions(username, 'submission')

        return payload

    except Exception as err:
        raise err
