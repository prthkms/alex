from preprocess import QueryMatcher
import support
import sys

if __name__ == '__main__':
	if(len(sys.argv) > 1):
		query_string = ' '.join(sys.argv[1:])
	else:
		print 'enter something'
		sys.exit()
	qm = QueryMatcher()
	category = qm.query(query_string)
	print category
	support.assign_handler(query_string, category)