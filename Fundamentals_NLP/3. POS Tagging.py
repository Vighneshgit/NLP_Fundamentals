#Part-of-Speech (POS) tagging is the process of marking up a word in a text as corresponding to a particular part of speech.
# This imports the necessary functions for tokenization (word_tokenize) and part-of-speech tagging (pos_tag) from NLTK (Natural Language Toolkit).
# POS tagging assigns a specific part-of-speech tag to each word in the input text.
# python

from nltk.tokenize import word_tokenize
from nltk import pos_tag

text = "Hello, how are you? I hope you are doing well. NLP is fun!"
words = word_tokenize(text)

# POS Tagging
pos_tags = pos_tag(words)
print("POS Tags:", pos_tags)
