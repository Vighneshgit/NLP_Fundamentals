#Sentiment analysis is the process of determining the sentiment or emotion expressed in a text.
# This line imports SentimentIntensityAnalyzer from NLTK('s sentiment module. '
# SentimentIntensityAnalyzer is a pre-built tool in NLTK that helps analyze and quantify the sentiment expressed in a piece of text.)

from nltk.sentiment import SentimentIntensityAnalyzer

text = "I love this product! It's amazing."

# Creates an instance of SentimentIntensityAnalyzer. This initializes the sentiment analyzer object that will be used to analyze the sentiment of the text.
sia = SentimentIntensityAnalyzer()

# sia.polarity_scores(text): Analyzes the sentiment of the input text and returns a dictionary of sentiment scores.
# Example:
# Input text: "I love this product! It's amazing."
# Output sentiment scores: {'neg': 0.0, 'neu': 0.297, 'pos': 0.703, 'compound': 0.7351}
sentiment = sia.polarity_scores(text)
print("Sentiment:", sentiment)
