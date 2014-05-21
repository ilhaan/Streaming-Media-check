import urllib, os
from xml.dom import minidom

os.system("clear")

plex_url = 'http://localhost:32400/library/sections/2/all'
root_tree = minidom.parse(urllib.urlopen(plex_url))
part = root_tree.getElementsByTagName('Part')
for x in part:
  filepath = x.getAttribute('file')
  print filepath
