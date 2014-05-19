#Python Library Imports
import os, sys, sre, json, urllib, shutil, logging, stat, datetime, httplib, module_locater, tools
from xml.dom import minidom
#------------------
header = """
****************************************
*                                      *
*     Streaming Service Check          *
*                                      *
****************************************
\n"""

#Script Directory setup
myDateTime = datetime.datetime.now().strftime("%y-%m-%d-%H-%M")
Scriptdir = module_locater.module_path()
logdir = Scriptdir + '\\logs\\'
logfile = logdir + 'Streamingcheck-' + myDateTime + '.log'

#Log Handler Setup
logger = logging.getLogger('Netflix_check')
hdlr = logging.FileHandler(logfile)
formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
hdlr.setFormatter(formatter)
logger.addHandler(hdlr)
logger.setLevel(logging.INFO)

def movie_data(title):
	global movie1
	global movie
	movie1 = (title)
	movie_paren = movie1.replace('(', '').replace(')', '')
	movie = movie_paren
	movie_url = "http://www.canistream.it/services/search?movieName=%s" % movie
	try:
		url = urllib.urlopen(movie_url)
	except UnicodeError:
		print 'Non-ASCII Characters in title. Skipping.'
		logger.info('Non-ASCII Characters in title of %s' % movie)
		return False
	HTMLsource1 = url.read()
	url.close()
	data_j = json.loads(HTMLsource1)
	try:
		ID = data_j[0]['_id']
	except IndexError:
		print 'Invalid characters in title. Skipping.'
		logger.info('Invalid Search Characters in title of %s' % movie)
		return False
	movie_url2 = "http://www.canistream.it/services/query?movieId=%s&attributes=1&mediaType=streaming" % ID
	url = urllib.urlopen(movie_url2)
	global HTMLsource2
	HTMLsource2 = url.read()
	url.close()
	Netflix()
	Amazon_Prime()
	Hulu_Plus()

def Netflix():
	service = sre.findall('friendlyName":"([^"]+)', HTMLsource2)
	if 'Netflix Instant' in service:
		return True
	else:
		return False

def Amazon_Prime():
	service = sre.findall('friendlyName":"([^"]+)', HTMLsource2)
	if "Amazon Prime" in service:
		return True
	else:
		return False

def Hulu_Plus():
	service = sre.findall('friendlyName":"([^"]+)', HTMLsource2)
	if "Hulu Plus" in service:
		return True
	else:
		return False

def delete_movie(service_name):
		print "%s marked for deletion. Moving on to the next movie." % movie
		logger.info('%s is avalible on %s.' % (movie,service_name))

'''
def pushover():
	if 1 in to_delete:
		conn = httplib.HTTPSConnection("api.pushover.net:443")
		conn.request("POST", "/1/messages.json",
		urllib.urlencode({
		"token": "afTHBbHyLBSUFTNNPhBV9oDtBpqCUJ",
		"user": "uU95W9hYqeW3b24uyPaT1skT1SG35N",
		"message": "Netflix/Plex Scan has been run, and found new items to delete. Check the log for new movies to remove from Plex. ",
		}), { "Content-type": "application/x-www-form-urlencoded" })
		conn.getresponse()
	else:
		conn = httplib.HTTPSConnection("api.pushover.net:443")
		conn.request("POST", "/1/messages.json",
		urllib.urlencode({
		"token": "afTHBbHyLBSUFTNNPhBV9oDtBpqCUJ",
		"user": "uU95W9hYqeW3b24uyPaT1skT1SG35N",
		"message": "Netflix/Plex Scan has been run, but found no new movies to delete.",
		}), { "Content-type": "application/x-www-form-urlencoded" })
		conn.getresponse()
'''

plex_url = 'http://localhost:32400/library/sections/2/all'
root_tree = minidom.parse(urllib.urlopen(plex_url))
video = root_tree.getElementsByTagName('Video')
for t in video:
	title = t.getAttribute('title')
	movie_data(title)
	if Netflix() is True:
		#to_delete = '1'
		service_name = "Netflix"
		delete_movie(service_name)
	elif Amazon_Prime() is True:
		service_name = "Amazon Prime Instant Video"
		delete_movie(service_name)
	elif Hulu_Plus() is True:
		service_name = "Hulu"
		delete_movie(service_name)
	else:
		os.system('clear')
		print header
		print "%s is not available on Netflix, Amazon Prime Instant Video or Hulu Plus. Moving on to next movie." % movie
		continue
#pushover()
