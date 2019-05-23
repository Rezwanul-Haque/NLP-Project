""" Exploring Text Data analysis
    Problem
        You want to explore and understand the text data.
    
    Definition
        
    Solution
        The simplest way to do this by using NLTK or the TextBlob library.
    
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
wt_sentences = webtext.sents('firefox.txt')
wt_words = webtext.words('firefox.txt')

# Check number of words in the data
# print(len(wt_sentences))

# Output
# 1142

# print(len(wt_words))

# Output
# 102457

# Compute the frequency of all words in the reviews
# Generating frequency for all the words:
frequency_dist = FreqDist(wt_words)

# print(frequency_dist)

sorted_frequency_dist = sorted(frequency_dist, key=frequency_dist.__getitem__,
                                               reverse=True)

# print(sorted_frequency_dist)

# Consider words with length greater than 3 and plot
large_words = dict([(key, value) for key, value in frequency_dist.items() if len(key) > 3])

frequency_dist = FreqDist(large_words)
# frequency_dist.plot(50, cumulative=False)  # Un-comment these to see the plot

# Output

# Build Wordcloud
wcloud = WordCloud().generate_from_frequencies(frequency_dist)

# Plotting the wordcloud
plt.imshow(wcloud, interpolation='bilinear')
plt.axis("off")
plt.show()

# Output
