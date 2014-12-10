import json
import requests

# example queries:
# duckduckgo.py mahatma gnadhi
# duckduckgo.py friends characters

def parse_result(result):
	if(result['Type'] == 'D'):
		print """There is more than one answer for this. Try making your query more specific.
For example, if you want to learn about apple the company and not apple the fruit, try something \
like apple inc or apple computers.  
		"""
	
	elif(result['Type'] == 'A'):
		print result['AbstractText']
		print '\nResults from DuckDuckGo'
	
	elif(result['Type'] == 'C'):
		for entry in result['RelatedTopics']:
			print entry['Text']
			print "\n"
	else:
		print "I do not know how to process this query at the moment"

def query(string):
	url = "https://api.duckduckgo.com/?q="
	formating = "&format=json"
	query_string = url+'+'.join(string)+formating
	try:
		result = json.loads(requests.get(query_string).text)
	except:
		print "I'm sorry. Something went wrong. May be we could try again later."
		return
	parse_result(result)

if __name__ == '__main__':
	import sys
	if(len(sys.argv) > 1):
		query(sys.argv[1:])