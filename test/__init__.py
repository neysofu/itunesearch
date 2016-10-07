import unittest
import itunesearch
import random

# Global variables
# ----------------

TRACK_QUERY = 'Rolling in the Deep'
COLLECTION_QUERY = '21'
AUTHOR_QUERY = 'Adele'


TRACK = itunesearch.search(TRACK_QUERY)[0]
COLLECTION = itunesearch.search(COLLECTION_QUERY)[0]
AUTHOR = itunesearch.search(AUTHOR_QUERY)[0]

class TestMedia(unittest.TestCase):
	
	def test_Track(self):
		TRACK.get_duration()
		TRACK.get_id()
		TRACK.get_name()
		TRACK.get_price()
		TRACK.grab_author()
		TRACK.grab_collection()
		TRACK.is_explicit()
		self.assertTrue(True)

	def test_search_song(self):
		test_track = itunesearch.search_song(TRACK_QUERY)[0]
		self.assertTrue(test_track.response == TRACK.response)

if __name__ == '__main__':
	unittest.main()
