Streaming-Media-check (forked and modified)
===========================================

This is a fork from dmartinez7500's 'Streaming-Media-Check' (https://github.com/dmartinez7500/Streaming-Media-check) - Ilhaan Rasheed

A Python script I'm putting together to check my media server for content available on Streaming services, and offer the choice to delete, in order to save space. - dmartinez7500

Recently added (dmartinez7500):
- Changed log directory to base path. this should make it non-OS dependent.

To-Do (dmartinez7500):
- Add option to check Amazon Instant Video as well as Netflix.
- Option to mark movies as 'Saved', even if they are available online. Thinking of using the Plex Collection feature to mark. Also would be nice to have the script update the XML to add the movie to the 'Saved' collection.
- Option to delete movies as they are found.
- Different modes. Scan and report only, or scan and delete.
- Ability to search for TV Shows as well. Not sure how to handle different seasons however.
- Ability to move movies to another location instead of deleting. Might be handy for when Netflix no longer has the movie.

Modifications to be made (ilhaan):
- Create two modes of operation: List Mode and Delete Mode. List Mode will list all movies that are available on any of the streaming services on to a log/text file. Delete Mode will delete the movie from the hard drive (how to handle video files in folders?)
- Allow user to select streaming services to compare against
- XML parsing currently done using MiniDOM. This is said to be slow and memory hungry. Try and change this to an ElementTree (xml.etree.ElementTree) implementation.
