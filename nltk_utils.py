import numpy as np 
import nltk
#nltk.download('punkt')
from nltk.stem.porter import PorterStemmer

stemmer = PorterStemmer()

def tokenize(sentence):
	return nltk.word_tokenize(sentence)

def stem(word):
	return stemmer.stem(word.lower())

def bag_of_words(tokenized_sentence, all_words):
	tokenized_sentence = [stem(w) for w in tokenized_sentence]
	bag = np.zeros(len(all_words), dtype=np.float32)
	
	for ind,w in enumerate(all_words):
		if w in tokenized_sentence:
			bag[ind] = 1.0
	return bag


"""
a = "How long does shipping take?"
print(a)

t_a = tokenize(a)
print(t_a)

words = ['Organize', 'organizes', 'organizing']
stemmed_words = [stem(w) for w in words]
print(stemmed_words)

print("!!!compleated!!!")

sentence = ["hello", "how", "are", "you"]
words = ["hi", "hello", "I", "you", "bye", "thank", "cool"]

bog = bag_of_words(sentence, words)

print(bog)

"""


