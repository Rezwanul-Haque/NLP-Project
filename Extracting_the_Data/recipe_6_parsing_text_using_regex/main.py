# • re.I: This flag is used for ignoring casing.
# • re.L: This flag is used to find a local dependent.
# • re.M: This flag is useful if you want to find patterns throughout multiple lines.
# • re.S: This flag is used to find dot matches.
# • re.U: This flag is used to work for unicode data.
# • re.X: This flag is used for writing regex in a more readable format.

# Regular expressions’ functionality:
# • Find the single occurrence of character a and b:
# Regex: [ab]
# • Find characters except for a and b:
# Regex: [^ab]
# • Find the character range of a to z:
# Regex: [a-z]
# • Find a range except to z:
# Regex: [^a-z]
# • Find all the characters a to z as well as A to Z:
# Regex: [a-zA-Z]
# • Any single character:
# Regex:
# • Any whitespace character:
# Regex: \s
# • Any non-whitespace character:
# Regex: \S
# • Any digit:
# Regex: \d
# • Any non-digit:
# Regex: \D
# • Any non-words:
# Regex: \W
# • Any words:
# Regex: \w
# • Either match a or b:
# Regex: (a|b)
# • The occurrence of a is either zero or one:
    # • Matches zero or one occurrence but not more than one occurrence
    # Regex: a? ; ?
    # • The occurrence of a is zero times or more than that:
    # Regex: a* ; * matches zero or more than that
    # • The occurrence of a is one time or more than that:
    # Regex: a+ ; + matches occurrences one or more that one time
# • Exactly match three occurrences of a:
# Regex: a{3}
# • Match simultaneous occurrences of a with 3 or more than 3:
# Regex: a{3,}
# • Match simultaneous occurrences of a between 3 to 6:
# Regex: a{3,6}
# • Starting of the string:
# Regex: ^
# • Ending of the string:
# Regex: $
# • Match word boundary:
# Regex: \b
# • Non-word boundary:
# Regex: \B

# • re.match(): This checks for a match of the string only
# at the beginning of the string. So, if it finds the pattern
# at the beginning of the input string, then it returns the
# matched pattern; otherwise; it returns a noun.
# • re.search(): This checks for a match of the string
# anywhere in the string. It finds all the occurrences of
# the pattern in the given input string or data.

# Tokenizing
# Import regex library
import re

# run the split query
re.split('\s+', 'I like this book.')

# Extracing email IDs
## Read/create the document or sentences
doc = "For more details please mail us at: xyz@abc.com, pqr@mno.com"

# Execute the re.findall function
addresses = re.findall(r'[\w\.-]+@[\w\.-]+', doc)
# for address in addresses:
#     print(address)

## Output
# xyz@abc.com
# pqr@mno.com

## Replacing email IDs
## Read/create the document or sentences
doc = "For more details please mail us at xyz@abc.com"

# Execute the re.sub function
new_email_address = re.sub(r'([\w\.-]+)@([\w\.-]+)', r'pqr@mno.com', doc)

# print(new_email_address)

## Output
# For more details please mail us at pqr@mno.com

# 1. Extract data from the ebook and perform regex
import re
import requests

# url you want to extract
url = 'https://www.gutenberg.org/files/2638/2638-0.txt'

# function to extract
def get_book(url):
    # Sends a http request to get the text from project Gutenberg
    raw = requests.get(url).text
    # Disscards the metadata from the beginning of the book
    start = re.search(r'\*\*\* START OF THIS PROJECT GUTENBERG EBOOK .* \*\*\*', raw).end()
    # Discards the metadata from the end of the book
    stop = re.search(r'II', raw).start()
    # Keeps the relevent text
    text = raw[start:stop]

    return text

# Processing
def preprocess(sentence):
    return re.sub('[^A-Za-z0-9.]+', ' ', sentence).lower()

# Calling the above function
book = get_book(url)
processed_book = preprocess(book)

# print(processed_book)

## Output
# produced by martin adamson david widger with corrections by andrew sly the 
# idiot by fyodor dostoyevsky translated by eva martin part i i.
# ...

# 2. Perform some exploratory data analysis on this data using regex
# Count number of times "the" is appeared in the book
string = r'the'
string_length = len(re.findall(string, processed_book))
print(string_length)

## Output
# 302

## Replace "i" with "I"
change_string_from = r'\si\s'
change_string_to = r" I "
processed_book = re.sub(change_string_from, change_string_to, processed_book)

# print(processed_book)

## Output
"""
...
of course I can t argue the matter because I know only my own case but my doctor 
...
"""

# find all occurance of text in the format "abc--xyz"
re.findall(r'[a-zA-Z0-9]*--[a-zA-Z0-9]*', book)

## Output
# ['ironical--it',
# 'malicious--smile',
# 'fur--or',
# ...]



