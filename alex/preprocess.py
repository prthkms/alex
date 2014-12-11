from __future__ import division
from nltk.tokenize import word_tokenize as wt
from nltk.stem import PorterStemmer
from collections import defaultdict
from math import log
import os


class QueryMatcher(object):
	"""This an implementation of tf-idf ranking 
	(term frequency - inverse document frequency) for information 
	retreival and text mining.
	1. Each sentence in 'corpus.txt' acts as a document, 
	and the processed words in each sentence act as terms.
	2. Frequently occuring stop words are removed. 
	3. Stemming is done on each word, i.e. reducing inflected or derived
	words to their word stem, base or root form.
	4. A new user query undergoes tf-idf ranking, and the highest
	ranked sentence(document) is picked up and mapped to a category. 
	"""
	
	def __init__(self):
		super(QueryMatcher, self).__init__()
		self.initialize()

	def calculate_inverse_docoument_frequencies(self):
		"""Q.calculate_inverse_docoument_frequencies() -- measures how much
		information the term provides, i.e. whether the term is common or
		rare across all documents.

		This is obtained by dividing the total number of documents 
		by the number of documents containing the term, 
		and then taking the logarithm of that quotient.
		"""
		for doc in self.processed_corpus:
			for word in doc:
				self.inverse_document_frequencies[word] += 1
		for key,value in self.inverse_document_frequencies.iteritems():
			idf = log((1.0 * len(self.corpus)) / value)
			self.inverse_document_frequencies[key] = idf

	def calculate_term_frequencies(self):
		"""Q.calculate_term_frequencies() -- calculate the number of times 
		each term t occurs in document d.
		"""
		for doc in self.processed_corpus:
			term_frequency_doc = defaultdict(int)
			for word in doc:
				term_frequency_doc[word] += 1
			
			for key,value in term_frequency_doc.iteritems():
				term_frequency_doc[key] = (1.0 * value) / len(doc)
			self.term_frequencies.append(term_frequency_doc)


	def initialize(self):

         	'''
		corpus : contains a list of sentences, each of which acts as 
		a document
		category : contains a category of each sentence in the corpus.
		stemmer : imported from the nltk library, used for reducing 
		words to their root form.
		'''

		self.stop_words = ['i', 'me', 'my', 'myself', 'we', 'our', 'ours', 
		'ourselves', 'you', 'your', 'yours', 'yourself', 'yourselves', 
		'he', 'him', 'his', 'himself', 'she', 'her', 'hers', 'herself', 
		'it', 'its', 'itself', 'they', 'them', 'their', 'theirs', 'themselves',
		'what', 'which', 'who', 'whom', 'this', 'that', 'these', 'those',
		'am', 'is', 'are', 'was', 'were', 'be', 'been', 'being', 'have', 'has',
		'had', 'having', 'do', 'does', 'did', 'doing', 'a', 'an', 'the', 'and',
		'but', 'if', 'or', 'because', 'as', 'until', 'while', 'of', 'at', 'by',
		'for', 'with', 'about', 'between', 'into','to', 'during', 'before', 
		'after', 'above', 'below', 'from', 'up', 'down', 'in', 'on', 'under', 
		'again', 'then', 'once', 'here', 'there', 'when', 'where', 'why', 'how',
		'all', 'any', 'both', 'each', 'few', 'more', 'most', 'other', 'some',
		'such', 'nor', 'only', 'own', 'same', 'so', 'than', 'too', 'very', 's',
		't', 'can', 'will', 'just', 'don', 'should', 'now']

		ALEX_DIR = os.path.join(os.path.expanduser('~'),'alex')
		#ALEX_DIR = '/home/pratheek/work/git_repos/alex/alex'
		#ALEX_DIR = '/home/chitra/aost/alex/alex'
		#ALEX_DIR = '/home/anushree/aost/alex/alex'
		self.category = open(os.path.join(ALEX_DIR,'category.txt'))
		self.corpus_list = self.corpus.readlines()
		self.category_list = self.category.readlines()
		self.corpus.seek(0)
		self.corpus = self.corpus.read()
		self.processed_corpus = []
		self.punctuation = [',', '.', '?', '!']
		self.stemmer = PorterStemmer()
		self.inverse_document_frequencies = defaultdict(float)
		self.term_frequencies = []

		#--------------------------------------
		self.process_corpus()
		self.calculate_inverse_docoument_frequencies()
		self.calculate_term_frequencies()



	def match_query_to_corpus(self):
		"""Q.match_query_to_corpus() -> index -- return the matched corpus 
		index of the user query 
		"""
		ranking = []
		for i,doc in enumerate(self.processed_corpus):
			rank = 0.0
			for word in self.processed_query:
				if word in doc:
					rank += self.term_frequencies[i][word] * self.inverse_document_frequencies[word]
			ranking.append((rank,i))
		matching_corpus_index = 0
		max_rank = 0
		for rank,index in ranking:
			if rank > max_rank:
				matching_corpus_index = index
				max_rank = rank
		return matching_corpus_index



	def process_corpus(self):
		"""Q.process_corpus() -- processes the queries defined by us, 
		by tokenizing, stemming, and removing stop words.
		"""
		for doc in self.corpus_list:
			doc = wt(doc)
			sentence = []
			for word in doc:
				if word not in self.stop_words and word not in self.punctuation:
					word = self.stemmer.stem(word)
					sentence.append(word)
			self.processed_corpus.append(sentence)


	def process_query(self):
		"""Q.process_query() -- processes the user query, 
		by tokenizing and stemming words.
		"""
		self.query = wt(self.query)
		self.processed_query = []
		for word in self.query:
			if word not in self.stop_words and word not in self.punctuation:
				self.processed_query.append(self.stemmer.stem(word))

	def query(self, query):
		"""Q.query(query string) -> category string -- return the matched 
		category for any user query
		"""
		self.query = query
		self.process_query()
		matching_corpus_index = self.match_query_to_corpus()
		return self.category_list[matching_corpus_index].strip()



	def calculate_inverse_docoument_frequencies(self):
		for doc in self.processed_corpus:
			for word in doc:
				self.inverse_document_frequencies[word] += 1
		for key,value in self.inverse_document_frequencies.iteritems():
			self.inverse_document_frequencies[key] = log((1.0*len(self.corpus))/value)

#To calculate term frequencies
	def calculate_term_frequencies(self):
		for doc in self.processed_corpus:
			term_frequency_doc = defaultdict(int)
			for word in doc:
				term_frequency_doc[word] += 1
			
			for key,value in term_frequency_doc.iteritems():
				term_frequency_doc[key] = (1.0*value)/len(doc)
			self.term_frequencies.append(term_frequency_doc)

#To match user query to corpus list and return queries with their ranking based on closest match 
	def match_query_to_corpus(self):
		ranking = []
		for i,doc in enumerate(self.processed_corpus):
			rank = 0.0
			for word in self.processed_query:
				if word in doc:
					rank += self.term_frequencies[i][word] * self.inverse_document_frequencies[word]
			ranking.append((rank,i))
		matching_corpus_index = 0
		max_rank = 0
		for rank,index in ranking:
			if rank > max_rank:
				matching_corpus_index = index
				max_rank = rank
		return matching_corpus_index

