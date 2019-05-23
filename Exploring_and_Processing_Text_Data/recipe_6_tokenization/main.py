""" Tokenizing Text
    Problem
        the ways to tokenize text
    
    Definition
        Tokenization refers to splitting text into minimal meaningful units
    
    Solution
        The simplest way to do this is by using the TextBlob library.
    
    Author: Rezwanul Haque
    Date: 
    License: MIT
"""
# Import Standard Library

# Import Third Party Library
import pandas as pd
from textblob import TextBlob
import nltk

# Import Local  Library


# Your code goes here
text: list = ['This is introduction to NLP',
              'It is likely to be useful, to people',
              'Machine learning is the new electricity',
              'There would be less hype around AI and more action going forward',
              'python is the best tool!',
              'R is good language',
              'I like this book',
              'I want more books like this']

# Converting list to dataframe
df = pd.DataFrame({'tweet': text})
# print(df)

# Output
#                                                tweet
# 0                        This is introduction to NLP
# 1               It is likely to be useful, to people
# 2            Machine learning is the new electricity
# 3  There would be less hype around AI and more ac...
# 4                           python is the best tool!
# 5                                 R is good language
# 6                                   I like this book
# 7                        I want more books like this

# Execute below commands on the text data
string_tokenize_textblob = TextBlob(df['tweet'][3]).words

print(string_tokenize_textblob)

# Output
# ['There', 'would', 'be', 'less', 'hype', 'around', 'AI',
#  'and', 'more', 'action', 'going', 'forward']

# Create data 
mystring = "My favorite animal is cat"

string_tokenize_nltk = nltk.word_tokenize(mystring)

print(string_tokenize_nltk)

# Output
# ['My', 'favorite', 'animal', 'is', 'cat']

# Using split function from python
string_tokenize_split = mystring.split()

print(string_tokenize_split)

# Output
# ['My', 'favorite', 'animal', 'is', 'cat']