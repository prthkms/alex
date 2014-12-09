import count
import web

def assign_handler(query, category):
	if(category == 'count lines'):
		count.lines(query)
	elif(category == 'count words'):
		count.words(query)
	elif(category == 'weather'):
		web.weather(query)
	elif(category == 'no match'):
		web.generic(query)