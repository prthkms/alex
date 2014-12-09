from preprocess import QueryMatcher
import support
import sys

if __name__ == '__main__':
	if(len(sys.argv) > 1):
		query_string = ' '.join(sys.argv[1:])
	else:
		query_string = "give me the word count in query.txt"
	qm = QueryMatcher()
	category = qm.query(query_string)
	print category
	support.assign_handler(query_string, category)