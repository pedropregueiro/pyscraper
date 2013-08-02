
import sys
import urllib2
import re

# scrape a website given some params (URL, HTTP Headers, regex, etc.)
def scrape(params):
	try:
		url = params['url']
		content = _get_content(url, params)
	except KeyError as e:
		sys.exit("Missing argument '%s'!" % e[0])
	except:
		print "Unexpected error:", sys.exc_info()[0]
		raise
		sys.exit()

	save = raw_input('Do you want to save the HTML content to a file? [y/n] ')
	if save == 'y':
		_save_content(content)
	
	for key, regex in params['regexes'].iteritems():
		match = re.search(regex, content)
		if match:
			print "%s: %s" % (key, match.group(0))



# gets the HTML content of the URL with some optional params
def _get_content(url, params):
	request = urllib2.Request(url)

	# for POST requests
	if 'post_values' in params:
		data = urllib.urlencode(post_values)
		request.add_data(data)

	# for additional HTTP headers needed (user-agent, credentials, etc.)
	if 'headers' in params:
		for header, value in params['headers'].iteritems():
			request.add_header(header, value)

	response = urllib2.urlopen(request)
	
	# use info to check response's HTTP headers
	info = response.info()

	content = response.read()
	return content
	

# save the content to a file for future debug if necessary
def _save_content(content):
	filename = raw_input('Do you want to name the output file? [output.html] ')
	if not filename:
		filename = 'output.html'

	try:
		file = open(filename, 'w')
		file.write(content)
		file.close()
		print "File %s saved successfully!\n\n" % filename
	except:
		print "Unexpected error:", sys.exc_info()[0]
		raise
		sys.exit()



## TODO:
# . analyse response's content type to smartly save as .html, .xml or whatever
# . improve regex matching to allow multiple results (g)
# . improve display of results



