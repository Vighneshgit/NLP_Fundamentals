#Tokenization is the process of splitting text into individual words or sentences.
# his line imports two functions, word_tokenize and sent_tokenize, from the nltk.tokenize module.
# These functions are used for tokenizing text into words and sentences, respectively.

from nltk.tokenize import word_tokenize, sent_tokenize

text = "Hello, how are you? I hope you are doing well. NLP is fun!"

# Sentence Tokenization
# sent_tokenize(text): This function splits the input text into individual sentences based on punctuation marks
# (like periods, exclamation marks, and question marks).
# Example:
# Input text: "Hello, how are you? I hope you are doing well. NLP is fun!"
# Output sentences: ['Hello, how are you?', 'I hope you are doing well.', 'NLP is fun!']
# The sentences list contains each sentence as a separate string.

sentences = sent_tokenize(text)
print("Sentences:", sentences)



# word_tokenize(text): This function splits the input text into individual words and punctuation marks.
# Example:
# Input text: "Hello, how are you? I hope you are doing well. NLP is fun!"
# Output words: ['Hello', ',', 'how', 'are', 'you', '?', 'I', 'hope', 'you', 'are', 'doing', 'well', '.', 'NLP', 'is', 'fun', '!']
# The words list contains each word and punctuation mark as a separate string element.
# Word Tokenization
words = word_tokenize(text)
print("Words:", words)


