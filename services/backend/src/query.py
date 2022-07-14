"""
This script executes API calls and constructs data for the front-end.
"""

from datetime import datetime
from string import punctuation

from decouple import config

from . import api
from . import preprocess


async def main(username: str): 

    payload = {}
    
    try:
        # Get general information
        payload['basic_data'] = await api.getBasicData(username)

        # Get no. of comments
        payload['num_comments'] = await api.getNumSubmissions(username, 'comment')

        # Get no. of submissions
        payload['num_submissions'] = await api.getNumSubmissions(username, 'submission')

        ### Comment text processing
        commentList = await api.getCommentList(username)

        # Get top words sorted in ascending order
        payload['top_words'] = await preprocess.preprocess_string([comment["body"] for comment in commentList])

        return payload

    except Exception as err:
        raise err
