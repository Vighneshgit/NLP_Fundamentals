#pip install nltk
#DOWNLOAD THE DATASET
import nltk
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('maxent_ne_chunker')
nltk.download('words')
nltk.download('vader_lexicon')



# punkt:


# Punk Example to set identify and seperate the sentences
# Purpose: punkt is a tokenizer that splits text into sentences and words.
# Use Case: It’s used for sentence splitting and word tokenization, essential steps in text preprocessing.
from nltk.tokenize import word_tokenize, sent_tokenize
text = "Hello! How are you? I am fine."
print(sent_tokenize(text))  # Output: ['Hello!', 'How are you?', 'I am fine.']
print(word_tokenize(text))  # Output: ['Hello', '!', 'How', 'are', 'you', '?', 'I', 'am', 'fine', '.']



# averaged_perceptron_tagger:


# Purpose: This is a part-of-speech (POS) tagger.
# Use Case: It tags words in a sentence with their respective parts of speech (e.g., noun, verb, adjective).
from nltk import pos_tag
from nltk.tokenize import word_tokenize
words = word_tokenize("Natural language processing is fascinating.")
print(pos_tag(words))  # Output: [('Natural', 'JJ'), ('language', 'NN'), ('processing', 'NN'), ('is', 'VBZ'), ('fascinating', 'VBG'), ('.', '.')]


# maxent_ne_chunker:


# Purpose: This is used for Named Entity Recognition (NER).
# Use Case: It identifies named entities (e.g., person names, organizations, locations) in text.
from nltk import pos_tag, ne_chunk
from nltk.tokenize import word_tokenize
words = word_tokenize("Apple is looking at buying U.K. startup for $1 billion.")
pos_tags = pos_tag(words)
print(ne_chunk(pos_tags))  # Output: (S Apple/NNP is/VBZ looking/VBG at/IN buying/VBG U.K./NNP startup/NN for/IN $/$ 1/CD billion/CD ./.)


# words:

# Purpose: This dataset contains a list of English words.
# Use Case: It’s often used for spell checking, word validation, or other linguistic tasks.

from nltk.corpus import words
print(words.words()[:10])  # Output: ['A', 'a', 'aa', 'aal', 'aalii', 'aam', 'Aani', 'aardvark', 'aardwolf', 'Aaron']


# vader_lexicon:
#
# Purpose: VADER (Valence Aware Dictionary and sEntiment Reasoner) is a sentiment analysis tool.
# Use Case: It’s used for sentiment analysis, particularly in social media text where emojis, slang, and punctuation are important.

from nltk.sentiment.vader import SentimentIntensityAnalyzer
sid = SentimentIntensityAnalyzer()
text = "NLTK is a fantastic library!"
print(sid.polarity_scores(text))  # Output: {'neg': 0.0, 'neu': 0.245, 'pos': 0.755, 'compound': 0.7023}

