""" Lemmatizing
    Problem
        the ways to lemmatizing a word.
    
    Definition
        Lemmatization is a process of extracting a root word
        by considering the vocabulary. For example, “good,”
        “better,” or “best” is lemmatized into "good".
    
    Note
        The part of speech of a word is determined in lemmatization. It will
        return the dictionary form of a word, which must be a valid word while
        stemming just extracts the root word.
    
    Example
        • Lemmatization handles matching “car” to “cars” along
          with matching “car” to “automobile.”
        • Stemming handles matching “car” to “cars.”
        Lemmatization can get better results.
        • The stemmed form of "leafs" is "leaf".
        • The stemmed form of "leaves" is "leav".
        • The lemmatized form of "leafs" is "leaf".
        • The lemmatized form of "leaves" is "leaf".
    
    Solution
        The simplest way to do this is by using NLTK or the TextBlob library.
    
    Author: Rezwanul Haque
    Date: 
    License: MIT
"""
# Import Standard Library

# Import Third Party Library
import pandas as pd
from textblob import Word

# Import Local  Library


# Your code goes here
text: list = ['I like fishing',
              'I eat fish',
              'There are many fishes in pound',
              'leaves and leaf']

# Converting list to dataframe
df = pd.DataFrame({'tweet': text})
# print(df)

# Output
#                             tweet
# 0                  I like fishing
# 1                      I eat fish
# 2  There are many fishes in pound
# 3                 leaves and leaf

# Execute below commands on the text data
lemmatize_df = df['tweet'].apply(lambda x: " ".join([Word(word).lemmatize() for word in x.split()]))

print(lemmatize_df)

# Output
# 0                  I like fishing
# 1                      I eat fish
# 2    There are many fish in pound
# 3                   leaf and leaf
# Name: tweet, dtype: object

# Observe
#     "fish" and "fishes" are lemmatized to "fish" and, as
#     explained, "leaves" and "leaf" are lemmatized to "leaf"