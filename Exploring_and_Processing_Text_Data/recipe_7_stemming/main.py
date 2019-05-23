""" Stemming
    Problem
        the ways to Stemming words
    
    Definition
        Stemming is a process of extracting a root word. For
        example, “fish,” “fishes,” and “fishing” are stemmed into fish.
    
    Solution
        The simplest way to do this by using NLTK or a TextBlob library.
    
    Author: Rezwanul Haque
    Date: 
    License: MIT
"""
# Import Standard Library

# Import Third Party Library
import pandas as pd
from textblob import TextBlob
from nltk.stem import PorterStemmer

# Import Local  Library


# Your code goes here
text: list = ['I like fishing',
              'I eat fish',
              'There are many fishes in pound']

# Converting list to dataframe
df = pd.DataFrame({'tweet': text})
# print(df)

# Output
#                             tweet
# 0                  I like fishing
# 1                      I eat fish
# 2  There are many fishes in pound

# Execute below commands on the text data
stemmer = PorterStemmer()

stemmed_df = df['tweet'][:5].apply(lambda x: " ".join([stemmer.stem(word) for word in x.split()]))

print(stemmed_df)

# Output
# 0                     I like fish
# 1                      I eat fish
# 2    there are mani fish in pound
# Name: tweet, dtype: object

# Note 'fishing', 'fishes', 'fish' have been stemmed to fish.
