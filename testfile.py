# Test file created to test new features, additions and modifications to movie_select_plex.py
import os, urllib, json, re

os.system("clear")

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
