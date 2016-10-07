import unittest
import itunesearch
import random

TRACK_QUERY = 'Hello'
COLLECTION_QUERY = '25'
AUTHOR_QUERY = 'Adele'

TRACK = itunesearch.search_track(TRACK_QUERY)[0]
COLLECTION = itunesearch.search_collection(COLLECTION_QUERY)[0]
AUTHOR = itunesearch.search_author(AUTHOR_QUERY)[0]

# Test suit
# ---------

class TestMedia(unittest.TestCase):
	
	def test_Track(self):
		self.assertTrue('256x256' in TRACK.get_artwork())
		self.assertTrue(TRACK.get_duration(True) == '0:04:55')
		self.assertTrue(TRACK.get_id() == 1051394215)
		self.assertTrue(TRACK.get_name() == TRACK_QUERY)
		self.assertTrue(TRACK.get_price() != None)
		self.assertTrue(TRACK.grab_author().response == AUTHOR.response)
		self.assertTrue(TRACK.grab_collection().response == COLLECTION.response)
		self.assertTrue(not(TRACK.is_explicit()))

	def test_Collection(self):
		COLLECTION.response
		self.assertTrue(True)
	
	def test_search_song(self):
		test_track = itunesearch.search_track(TRACK_QUERY)[0]
		self.assertTrue(test_track.response == TRACK.response)

if __name__ == '__main__':
	unittest.main()
