import urllib.request as urllib2
from bs4 import BeautifulSoup

# Fetch the html file
url = 'https://en.wikipedia.org/wiki/Natural_language_processing'
response = urllib2.urlopen(url)

html_doc = response.read()

# Parsing
soup = BeautifulSoup(html_doc, 'html.parser')

# Formatting the parsed html file
strhtml = soup.prettify()

# Print few line
# print(strhtml[:1000])

print(soup.title)
print(soup.title.string)
print(soup.a.string)
print(soup.b.string)

# Extracting all the instances of a tag
for x in soup.find_all('a'):
    print(x.string)

# Extracting all text of a particular tag
for x in soup.find_all('p'):
    print(x.text)