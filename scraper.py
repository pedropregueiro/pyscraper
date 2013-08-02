
import sys
import urllib2
import re

# dictionary of python's possible regex flags
REGEX_FLAGS = {
	'i'	:	re.IGNORECASE, 	# re.I
	's'	:	re.DOTALL, 		# re.S
	'l'	:	re.LOCALE, 		# re.L
	'm'	:	re.MULTILINE,	# re.M
	'x'	:	re.VERBOSE, 	# re.X
}

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
	
	for field, re_hash in params['extract'].iteritems():
		results = _extract_field(field, re_hash, content)
		for r in results:
			print "result: |%s|" % r			


# extract part of content that matches the given regex
def _extract_field(field, re_hash, content):
	regex = re_hash['regex']

	re_flags = 0
	if 'flags' in re_hash:
		flags = re_hash['flags']
		for flag in flags:
			if flag in REGEX_FLAGS:
				re_flags = re_flags | REGEX_FLAGS[flag]

	try:
		pattern = re.compile(regex, re_flags)
		if 'flags' in re_hash and re.search('g', re_hash['flags']) is not None:
			match = re.findall(pattern, content)
		else:
			match = [ re.search(pattern, content).group(1) ]
	except:
		return []

	return match



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


