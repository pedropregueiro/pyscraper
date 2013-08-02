
import scraper

html_params = { 
	'url' 		:	"http://www.google.com",
	'headers' 	:	{ 
						'User-Agent' : 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)' 
					},
	'extract' 	: 	{
						'title' : {
							'regex' : '<title>(.+?)</title>',
							'flags' : 'is'
						} 
					},
}

print "Scraping HTML...\n"
scraper.scrape(html_params)


xml_params = { 
	'url' 		:	"http://www.w3schools.com/xml/cd_catalog.xml",
	'headers' 	:	{ 
						'User-Agent' : 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)' 
					},
	'extract' 	: 	{
						'title' : {
							'regex' : '<title>(.+?)</title>',
							'flags' : 'isg'
						}
					},
}

print "\n\nScraping XML...\n"
scraper.scrape(xml_params)