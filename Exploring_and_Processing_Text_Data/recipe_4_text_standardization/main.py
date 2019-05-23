""" Standardizing Text
    Problem
        How to standardize the text?
    
    Definition
        Most of the text data is in the form of either
        customer reviews, blogs, or tweets, where there
        is a high chance of people using short words and
        abbreviations to represent the same meaning.
    
    Solution
        custom dictionary to look for short words and
        abbreviations.
    
    Author: Rezwanul Haque
    Date: 
    License: 
"""
# Import Standard Library
import re

# Import Third Party Library

# Import Local  Library


# Your code goes here
lookup_dict = {'nlp': 'natural language processing', 'ur': 'your',
               'wbu': 'What about you'}


# Creating a custom function for text standardization
def text_std(input_text):
    words = input_text.split()
    new_words = []
    for word in words:
        regex = r'[^\w\s]'
        word = re.sub(regex, '', word)
        if word.lower() in lookup_dict:
            word = lookup_dict[word.lower()]
            new_words.append(word)
            new_text = " ".join(new_words)
    
    return new_text


# Run the text_std function
std_text = text_std("I like nlp it's ur choice")
print(std_text)

# Output
# natural language processing your
