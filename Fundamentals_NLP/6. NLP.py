#Merged together
import nltk
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk import pos_tag, ne_chunk
from nltk.sentiment import SentimentIntensityAnalyzer

# Download required NLTK data
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('maxent_ne_chunker')
nltk.download('words')
nltk.download('vader_lexicon')

# Sample text
text = "Barack Obama was born in Hawaii. He was elected president in 2008. I love this product! It's amazing."

# Sentence Tokenization
sentences = sent_tokenize(text)
print("Sentences:", sentences)

# Word Tokenization
words = word_tokenize(text)
print("Words:", words)

# POS Tagging
pos_tags = pos_tag(words)
print("POS Tags:", pos_tags)

# Named Entity Recognition
named_entities = ne_chunk(pos_tags)
print("Named Entities:", named_entities)

# Sentiment Analysis
sia = SentimentIntensityAnalyzer()
sentiment = sia.polarity_scores(text)
print("Sentiment:", sentiment)
