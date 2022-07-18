"""
This script contains useful methods for pre-processing text.
"""

import nltk
from nltk.tokenize import RegexpTokenizer
from nltk.stem import WordNetLemmatizer,PorterStemmer
import re
lemmatizer = WordNetLemmatizer()
stemmer = PorterStemmer() 

async def preprocess_comments(sentences: list[str]):
    """ Processes a list of sentences into a dict of word:freq pairs.

    Parameters
    ----------
    sentences : list[str]
        List of sentences.
    
    Returns
    -------
    freqDist
        A dict of word:freq pairs.
    """

    sentences = str(sentences)
    sentences = sentences.lower()
    sentences = sentences.replace('{html}',"") 
    cleanr = re.compile('<.*?>')
    cleantext = re.sub(cleanr, '', sentences)
    rem_url = re.sub(r'http\S+', '', cleantext)
    rem_num = re.sub('[0-9]+', '', rem_url)
    tokenizer = RegexpTokenizer(r'\w+')
    tokens = tokenizer.tokenize(rem_num)  
    filtered_words = [w for w in tokens if len(w) > 2 if not w in nltk.corpus.stopwords.words('english')]
    # stem_words=[stemmer.stem(w) for w in filtered_words]
    # lemma_words=[lemmatizer.lemmatize(w) for w in stem_words]
    freq_dist = nltk.FreqDist(filtered_words)
    freq_dist = await dict_sort(freq_dist)
    return freq_dist

async def dict_sort(dict):
    return {k: v for k, v in sorted(dict.items(), key=lambda x: x[1], reverse=True)}