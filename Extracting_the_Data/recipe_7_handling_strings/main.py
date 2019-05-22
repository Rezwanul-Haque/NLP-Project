# s.find(t) index of first instance of string t inside s (-1 if not found)
# s.rfind(t) index of last instance of string t inside s (-1 if not found)
# s.index(t) like s.find(t) except it raises ValueError if not found
# s.rindex(t) like s.rfind(t) except it raises ValueError if not found
#  s.join(text) combine the words of the text into a string
# using s as the glue
#  s.split(t) split s into a list wherever a t is found
# (whitespace by default)
# s.splitlines() split s into a list of strings, one per line
# s.lower() a lowercased version of the string s
# s.upper() an uppercased version of the string s
# s.title() a titlecased version of the string s
# s.strip() a copy of s without leading or trailing whitespace
# s.replace(t, u) replace instances of t with u inside s

## Replacing content
# Creating string
string_v1 = "I am exploring NLP"

# To extract particular character or range of characters from string
print(string_v1[0])
## Output
# I
# To extract exploring
print(string_v1[5:14])
## Output
# exploring


## Replace “exploring” with “learning” in the above string
# Creating string
string_v2 = string_v1.replace('exploring', 'learning')

print(string_v2)
## Output
# I am learning NLP

## Concatenating two strings
# Creating string
s1 = "nlp"
s2 = "machine learning"

s3 = s1 + s2

print(s3)
## Output
# 'nlpmachine learning'


## Searching for a substring in a string
# Creating string
var = "I am learning NLP"
f = "learn"

# Use the find function to fetch the starting index value of the substring in the whole string.
print(var.find(f))
## Output
# 5
