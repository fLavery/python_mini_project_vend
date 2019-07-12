import re 
import collections

text = open('book.txt').read().lower()
words = re.findall('\w+', text)
print(collections.Counter(words).most_common(10))

# finds the most common 10 words from a file