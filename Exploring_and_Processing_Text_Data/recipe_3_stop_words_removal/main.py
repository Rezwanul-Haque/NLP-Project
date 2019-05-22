""" Removing Stop Words
    Problem
        How to remove Stop Words?
    
    Definition
        A stop word is a commonly used word (such as “the”, “a”, “an”, “in”)
        that carry no meaning or less meaning compared to other keywords
    
    Solution
        The simplest way to do this by using the NLTK library, or you can build
        your own stop words file.
    
    Author: Rezwanul Haque
    Date: 
    License: 
"""
# Import Standard Library

# Import Third Party Library
import pandas as pd
import nltk
from nltk.corpus import stopwords

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
# remove stop words
stop = stopwords.words('english')

df['tweet'] = df['tweet'].apply(lambda x: ' '.join(x for x in x.split() if x.lower() not in stop))

print(df['tweet'])

# Output
# 0                                  introduction NLP
# 1                             likely useful, people
# 2                  Machine learning new electricity
# 3    would less hype around AI action going forward
# 4                                 python best tool!
# 5                                   R good language
# 6                                         like book
# 7                                   want books like
# Name: tweet, dtype: object