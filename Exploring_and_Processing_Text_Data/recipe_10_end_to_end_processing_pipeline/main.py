""" Building a Text Preprocessing Pipeline
    Problem
        end-to-end text preprocessing pipeline. Whenever
        you want to do preprocessing for any NLP application,
        you can directly plug in data to this pipeline function
        and get the required clean text data as the output.
    
    Definition
        
    Solution
        The simplest way to do this by creating the custom function with all
        the techniques shown in the other recipes.
    
    Author: Rezwanul Haque
    Date: 
    License: MIT
"""
# Import Standard Library
import string

# Import Third Party Library
# import nltk
from nltk.corpus import webtext
# nltk.download('webtext')  # if not downloaded these corpus
from nltk.probability import FreqDist
from nltk.corpus import stopwords
from wordcloud import WordCloud
import matplotlib.pyplot as plt

# Import Local  Library


# Your code goes here

# Wrapper function for text data preprocessing
def processRow(row):
    # Import Standard Library
    import re

    # Import Third Party Library
    import nltk
    from textblob import TextBlob
    from textblob import Word
    from nltk.corpus import stopwords
    from nltk.stem import PorterStemmer
    from nltk.tokenize import word_tokenize
    from nltk.util import ngrams
    from wordcloud import WordCloud, STOPWORDS

    # Import Local  Library

    # Your code goes here
    tweet = row

    # Lower case
    tweet.lower()

    # Removes unicode strings like "\u002c" and "x96" 
    tweet = re.sub(r'(\\u[0-9A-Fa-f]+)', r'', tweet)       
    tweet = re.sub(r'[^\x00-\x7f]', r'', tweet)

    # Convert any url to URL
    tweet = re.sub('((www\.[^\s]+)|(https?://[^\s]+))', 'URL', tweet)

    # Convert any @Username to "AT_USER"
    tweet = re.sub('@[^\s]+', 'AT_USER', tweet)

    # Remove additional white spaces
    tweet = re.sub('[\s]+', ' ', tweet)
    tweet = re.sub('[\n]+', ' ', tweet)

    # Remove not alphanumeric symbols white spaces
    tweet = re.sub(r'[^\w]', ' ', tweet)

    # Removes hastag in front of a word """
    tweet = re.sub(r'#([^\s]+)', r'\1', tweet)

    # Replace #word with word
    tweet = re.sub(r'#([^\s]+)', r'\1', tweet)

    # Remove :( or :)
    tweet = tweet.replace(':)', '')
    tweet = tweet.replace(':(', '')

    # Remove numbers
    tweet = ''.join([i for i in tweet if not i.isdigit()]) 

    # Remove multiple exclamation
    tweet = re.sub(r"(\!)\1+", ' ', tweet)

    # Remove multiple question marks
    tweet = re.sub(r"(\?)\1+", ' ', tweet)

    # Remove multistop
    tweet = re.sub(r"(\.)\1+", ' ', tweet)

    # lemma
    from textblob import Word
    tweet =" ".join([Word(word).lemmatize() for word in tweet.split()])

    # stemmer
    #st = PorterStemmer()
    #tweet=" ".join([st.stem(word) for word in tweet.split()])
    
    # Removes emoticons from text 
    tweet = re.sub(':\)|;\)|:-\)|\(-:|:-D|=D|:P|xD|X-p|\^\^|:-*|\^\.\^|\^\-\^|\^\_\^|\,-\)|\)-:|:\'\(|:\(|:-\(|:\S|T\.T|\.\_\.|:<|:-\S|:-<|\*\-\*|:O|=O|=\-O|O\.o|XO|O\_O|:-\@|=/|:/|X\-\(|>\.<|>=\(|D:', '', tweet)

    # trim
    tweet = tweet.strip('\'"')

    row = tweet

    return row

# Sample data for testing the processRow functions  
tweet_sample = "How to take control of your #debt https://personal.vanguard.com/us/insights/saving-investing/debt-management.#Best advice for #family #financial #success (@PrepareToWin)"
    
# Call the function with your data
preprocessed_text = processRow(tweet_sample)

print(preprocessed_text)

# Output
# How to take control of your debt URL advice for family financial success 
# AT_USER