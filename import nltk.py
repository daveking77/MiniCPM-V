import nltk
from nltk.tokenize import word_tokenize, sent_tokenize
import pandas as pd

# Load the text document
with open('example.txt', 'r') as f:
    text = f.read()

# Tokenize the text into words and sentences
words = word_tokenize(text)
sentences = sent_tokenize(text)

# Create a Pandas DataFrame to store the parsed data
data = pd.DataFrame({
    'Words': words,
    'Sentences': sentences
})

# Print the parsed data
print(data)
