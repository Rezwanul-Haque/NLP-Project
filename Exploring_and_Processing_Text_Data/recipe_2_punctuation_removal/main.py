""" Removing Punctuation
    Problem
        How to remove punctuation from the text data?
    
    Solution
        The simplest way to do this is by using the regex and replace() 
        function in Python.
    
    Author: Rezwanul Haque
    Date: 
    License: MIT
"""
# Import Standard Library
import re
import string

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

# Execute below function on the text data
# Using string library
s = "I. like. This book!"
s1 = s.translate(s.maketrans('', '', string.punctuation))
# print(s1)

# Using For loop
s2 = "I. like. This book!"
for c in string.punctuation:
    s2 = s2.replace(c, '')
# print(s2)

# Using re library
regex = r'[^\w\s]'
s3 = re.sub(regex, '', s)
# print(s3)

# Output
# I like This book

df['tweet'] = df['tweet'].str.replace(regex, '')
# print(df['tweet'])

df['tweet'] = df['tweet'].str.translate(str.maketrans('', '', string.punctuation))
# print(df['tweet'])

# Output 
# 0                          This is introduction to NLP
# 1                  It is likely to be useful to people
# 2              Machine learning is the new electricity
# 3    There would be less hype around AI and more ac...
# 4                              python is the best tool
# 5                                   R is good language
# 6                                     I like this book
# 7                          I want more books like this
# Name: tweet, dtype: object