""" Correcting Spelling
    Problem
        How to do spelling correction?
    
    Definition
        Most of the text data is in the form of either customer reviews,
        blogs, or tweets, where there is a high chance of people using
        short words and making typo errors. This will help us in reducing
        multiple copies of words, which represents the same meaning. For
        example, “proccessing” and “processing” will be treated as different
        words even if they are used in the same sense.
    
    Note
        Abbreviations should be handled before this step, or else the corrector
        would fail at times. Say, for example, “ur” (actually means “your”) 
        would be corrected to “or.”
    
    Solution
        The simplest way to do this by using the TextBlob library.
    
    Author: Rezwanul Haque
    Date: 
    License: 
"""
# Import Standard Library

# Import Third Party Library
import pandas as pd
from textblob import TextBlob
from autocorrect import spell

# Import Local  Library


# Your code goes here
text: list = ['Introduction to NLP',
              'It is likely to be useful, to people',
              'Machine learning is the new electrcity',  # electrcity spell is wrong
              'python is the best tool!',
              'R is good langauage',  # langauage spell is wrong
              'I like this book',
              'I want more books like this']

# Converting list to dataframe
df = pd.DataFrame({'tweet': text})
# print(df)

# Output
#                                                tweet
# 0                        This is introduction to NLP
# 1               It is likely to be useful, to people
# 2            Machine learning is the new electrcity
# 3  There would be less hype around AI and more ac...
# 4                           python is the best tool!
# 5                                 R is good langauage
# 6                                   I like this book
# 7                        I want more books like this

# Execute below code on the text data
spell_corrected_df = df['tweet'].apply(lambda x: str(TextBlob(x).correct()))

# print(spell_corrected_df)

# Output
# 0                        Introduction to NLP
# 1       It is likely to be useful, to people
# 2    Machine learning is the new electricity
# 3                   patron is the best tool!
# 4                         R is good language
# 5                           I like this book
# 6                I want more books like this
# Name: tweet, dtype: object

# Note it corrected the spelling of electricity and language.

# or Use autocorrect library
print(spell(u'mussage'))
print(spell(u'sirvice'))

# Output
# message
# service
