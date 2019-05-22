""" Converting Text Data to Lowercase
    Problem
        How to lowercase the text data?
    
    Solution
        The simplest way to do this is by using the default lower() function in
        Python.
        The lower() method converts all uppercase characters in a string into
        lowercase characters and returns them.
    
    Author: Rezwanul Haque
    Date: 
    License: 
"""
# Import Standard Library

# Import Third Party Library
import pandas as pd

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

# convert list to pandas data frame
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


# Execute .lower() function on the text data
# x = "String"
# x2 = x.lower()
# print(x2)
df['tweet'] = df['tweet'].apply(lambda x: ' '.join(x.lower() for x in x.split()))
# print(df['tweet'])

# Output
# 0                          this is introduction to nlp
# 1                 it is likely to be useful, to people
# 2              machine learning is the new electricity
# 3    there would be less hype around ai and more ac...
# 4                             python is the best tool!
# 5                                   r is good language
# 6                                     i like this book
# 7                          i want more books like this
# Name: tweet, dtype: object