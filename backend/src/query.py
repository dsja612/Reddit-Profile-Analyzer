from decouple import config
import praw
import json
from datetime import datetime
from string import punctuation
import nltk
import preprocess
# import nltk
# import pandas as pd
# from nltk.sentiment.vader import SentimentIntensityAnalyzer as SIA
# from nltk.tokenize import word_tokenize, RegexpTokenizer
# from nltk.corpus import stopwords

def connectToReddit():
    reddit = praw.Reddit(
        client_id = config('CLIENT_ID'),
        client_secret = config('CLIENT_SECRET'),
        user_agent = config('USER_AGENT')
    )
    return reddit

def getBasics(reddit, username):
    user = reddit.redditor(username)
    comment_karma = user.comment_karma
    link_karma = user.link_karma
    creation_time = user.created_utc
    obj = {
        "username": username,
        "comment_karma": comment_karma,
        "link_karma": link_karma,
        "creation_time": datetime.fromtimestamp(creation_time)
    }
    return obj

def getComments(reddit, username):
    user = reddit.redditor(username)
    comments = []
    for comment in user.comments.new(limit=None):
        comments.append(comment.body)
    return comments[0:500]

def getTextStatistics(comments):
    stopwords = nltk.corpus.stopwords.words('english')
    allWords = []
    for comment in comments:
        comment = comment.split(" ")
        for word in comment:
            allWords.append(word)
    return preprocess.preprocess_string(allWords)
