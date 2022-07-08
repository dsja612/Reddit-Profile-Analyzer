"""
This script executes API calls and constructs data for the front-end.
"""

import json
import requests
from datetime import datetime
from string import punctuation
import api
from decouple import config
import preprocess

def main(username: str): 

    payload = {}

    # Get general information
    userInfo = json.loads(requests.get('https://www.reddit.com/user/{}/about.json'.format(username)).content)
    payload['basic_data'] = userInfo['data']

    # Get no. of comments
    payload['num_comments'] = api.getNumSubmissions(username, 'comment')

    # Get no. of submissions
    payload['num_submissions'] = api.getNumSubmissions(username, 'submission')

    ### Comment text processing
    commentList = api.getCommentList(username)

    # Get top words sorted in ascending order
    payload['top_words'] = preprocess.preprocess_string([comment["body"] for comment in commentList])

    return payload



# def getBasics(reddit, username):
#     user = reddit.redditor(username)
#     comment_karma = user.comment_karma
#     link_karma = user.link_karma
#     creation_time = user.created_utc
#     obj = {
#         "username": username,
#         "comment_karma": comment_karma,
#         "link_karma": link_karma,
#         "creation_time": datetime.fromtimestamp(creation_time)
#     }
#     return obj

# def getComments(reddit, username):
#     user = reddit.redditor(username)
#     comments = []
#     for comment in user.comments.new(limit=None):
#         comments.append(comment.body)
#     return comments[0:500]

# def getTextStatistics(comments):
#     stopwords = nltk.corpus.stopwords.words('english')
#     allWords = []
#     for comment in comments:
#         comment = comment.split(" ")
#         for word in comment:
#             allWords.append(word)
#     return preprocess.preprocess_string(allWords)