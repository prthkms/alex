from preprocess import QueryMatcher
import support
import sys

if __name__ == '__main__':
	if(len(sys.argv) > 1):
		query_string = ' '.join(sys.argv[1:])
	else:
		print 'Please enter your query followed by alex.'
		sys.exit()
	qm = QueryMatcher()
	category = qm.query(query_string)
	support.assign_handler(query_string, category)