from nltk.tokenize import word_tokenize as wt
from nltk.stem import PorterStemmer
from collections import defaultdict
from math import log
import os

class QueryMatcher(object):
	"""docstring for QueryMatcher"""
	
	def __init__(self):
		super(QueryMatcher, self).__init__()
		self.initialize()

	def initialize(self):
                #list of stopwords
		self.stop_words = ['i', 'me', 'my', 'myself', 'we', 'our', 'ours', 'ourselves', 'you', 'your', 'yours', 'yourself',
		'yourselves', 'he', 'him', 'his', 'himself', 'she', 'her', 'hers', 'herself', 'it', 'its',
		'itself', 'they', 'them', 'their', 'theirs', 'themselves', 'what', 'which', 'who', 'whom',
		'this', 'that', 'these', 'those', 'am', 'is', 'are', 'was', 'were', 'be', 'been', 'being',
		'have', 'has', 'had', 'having', 'do', 'does', 'did', 'doing', 'a', 'an', 'the', 'and', 'but',
		'if', 'or', 'because', 'as', 'until', 'while', 'of', 'at', 'by', 'for', 'with', 'about',
		'between', 'into','to', 'during', 'before', 'after', 'above', 'below', 'from', 'up', 'down',
		'in', 'on', 'under', 'again', 'then', 'once', 'here', 'there', 'when', 'where', 'why', 'how',
		'all', 'any', 'both', 'each', 'few', 'more', 'most', 'other', 'some', 'such', 'nor',  'only',
		'own', 'same', 'so', 'than', 'too', 'very', 's', 't', 'can', 'will', 'just', 'don', 'should',
		'now']
                #Obtain current path
		ALEX_DIR = os.path.join(os.path.expanduser('~'),'alex')
		#ALEX_DIR = '/home/pratheek/work/git_repos/alex/alex'
		self.corpus = open(os.path.join(ALEX_DIR,'corpus.txt'))
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

#function to perform stemming operation on corpus words,create sentences of stemmed words and append them to a processed corpus list
	def process_corpus(self):
		for doc in self.corpus_list:
			doc = wt(doc)
			sentence = []
			for word in doc:
				if word not in self.stop_words and word not in self.punctuation:
					word = self.stemmer.stem(word)
					sentence.append(word)
			self.processed_corpus.append(sentence)

#function to perform stemming operation on user query words, and append them to a processed query list
	def process_query(self):
		self.query = wt(self.query)
		self.processed_query = []
		for word in self.query:
			if word not in self.stop_words and word not in self.punctuation:
				self.processed_query.append(self.stemmer.stem(word))
#function to match user query to corpus and return category
	def query(self, query):
		self.query = query
		self.process_query()
		matching_corpus_index = self.match_query_to_corpus()
		return self.category_list[matching_corpus_index].strip()

#function to calculate inverse document frequencies
	def calculate_inverse_docoument_frequencies(self):
		for doc in self.processed_corpus:
			for word in doc:
				self.inverse_document_frequencies[word] += 1
		for key,value in self.inverse_document_frequencies.iteritems():
			self.inverse_document_frequencies[key] = log((1.0*len(self.corpus))/value)

#function to calculate term frequencies
	def calculate_term_frequencies(self):
		for doc in self.processed_corpus:
			term_frequency_doc = defaultdict(int)
			for word in doc:
				term_frequency_doc[word] += 1
			
			for key,value in term_frequency_doc.iteritems():
				term_frequency_doc[key] = (1.0*value)/len(doc)
			self.term_frequencies.append(term_frequency_doc)

#function to match user query to corpus list and return queries with their ranking based on closest match 
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
