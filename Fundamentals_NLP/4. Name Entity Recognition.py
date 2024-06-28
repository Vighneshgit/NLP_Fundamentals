
#Named Entity Recognition is the process of identifying and categorizing key information (entities) in text.
# This imports the necessary NLTK modules and functions for Named Entity Recognition (NER),
# including ne_chunk for performing NER, word_tokenize for tokenizing words, and pos_tag for part-of-speech tagging.

from nltk import ne_chunk
from nltk.tokenize import word_tokenize
from nltk import pos_tag

text = "Barack Obama was born in Hawaii. He was elected president in 2008."

# word_tokenize(text): Tokenizes the input text into individual words and punctuation marks.
# Example:
# Input text: "Barack Obama was born in Hawaii. He was elected president in 2008."
# Output words: ['Barack', 'Obama', 'was', 'born',  '.']

# pos_tag(words): Assigns part-of-speech tags to each tokenized word.
# Example (for the tokenized words above):
# Output POS tags: [('Barack', 'NNP'), ('Obama', 'NNP'),  ('.', '.')]
# Each tuple pairs a word/token with its corresponding part-of-speech tag.


words = word_tokenize(text)
pos_tags = pos_tag(words)

# Named Entity Recognition
# ne_chunk(pos_tags): Applies Named Entity Recognition to the part-of-speech tagged words.
# Example (based on the POS tags above):
# Output named entities: Tree('S', [Tree('PERSON', [('Barack', 'NNP'), ('Obama', 'NNP')]), ('was', 'VBD'), ('born', 'VBN'), ('in', 'IN'),....
# ne_chunk organizes recognized entities into a nested tree structure (Tree objects) where entities like persons (PERSON) and
# geopolitical entities (GPE) are labeled accordingly.

named_entities = ne_chunk(pos_tags)
print("Named Entities:", named_entities)
