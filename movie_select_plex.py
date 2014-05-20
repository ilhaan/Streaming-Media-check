#Python Library Imports
# import stat, httplib, tools #this is the original import
import os, urllib, json, re, datetime, module_locater, logging
from xml.dom import minidom
#------------------
header = """
****************************************
*                                      *
*       Streaming Service Check        *
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


# Function to get movie's id from CanIStream.it
def get_movie_id(movie_name):
	movie_id_search_url = "http://www.canistream.it/services/search?movieName=%s" % movie_name
	url = urllib.urlopen(movie_id_search_url)
	json_data = url.read()
	url.close()
	data = json.loads(json_data)
	movie_id = data[0]["_id"]
	return movie_id

# Function to get streaming services movie is available on from CanIStream.it
def get_streaming_info(movie_id):
	movie_strinfo_url = "http://www.canistream.it/services/query?movieId=%s&attributes=1&mediaType=streaming" % movie_id
	url = urllib.urlopen(movie_strinfo_url)
	data = url.read()
	url.close()
	streaming_info = re.findall('friendlyName":"([^"]+)', data)
	return streaming_info

# Function to check of movie is available on Netflix Instant Streaming
def netflix_check(streaming_info):
	if 'Netflix Instant' in streaming_info:
		return True
	else:
		return False

# Function to check if movie is available on Hulu Plus
def hulu_check(streaming_info):
	if 'Hulu Plus' in streaming_info:
		return True
	else:
		return False

# Function to check if movie is available on Amazon Prime Instant Video
def amazon_check(streaming_info):
	if 'Amazon Prime' in streaming_info:
		return True
	else:
		return False

# Class that stores movie name and streaming services that movie is available on
class MovClass(object):
	def __init__(self, movie_name):
		self.movie_name = movie_name
		self.streaming_info = get_streaming_info(get_movie_id(movie_name))

movtest = MovClass("The Terminator")
if netflix_check(movtest.streaming_info):
	print "%s is available on Netflix" % movtest.movie_name
if hulu_check(movtest.streaming_info):
	print "%s is available on Hulu" % movtest.movie_name
if amazon_check(movtest.streaming_info):
	print "%s is available on Amazon Prime Instant Video" % movtest.movie_name


'''
#This function still needs to be modfied
def delete_movie(service_name):
		print "%s marked for deletion. Moving on to the next movie." % movie
		logger.info('%s is avalible on %s.' % (movie,service_name))
'''


'''
#These commands below still need to be modified
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
'''
