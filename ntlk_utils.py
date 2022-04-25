import nltk
nltk.download('punkt')
from nltk.stem.porter import PorterStemmer
stemmer = PorterStemmer()

# breaks sentences into words
def tokenize(sentence):
    return nltk.word_tokenize(sentence)

# stemming words ie cuts the words into smaller words
def stem(word):
    return stemmer.stem(word.lower())

def bag_of_words(tokenized_sentence,all_words):
    pass

a= "How do you live ?"
print(a)
a = tokenize(a)
print(a)