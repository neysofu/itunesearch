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

class TestTrack(unittest.TestCase):
	
	def test_get_artwork(self):
		self.assertIn('256x256', TRACK.get_artwork())

	def test_get_duration(self):
		self.assertEqual(TRACK.get_duration(True), '0:04:55')
	
	def test_get_id(self):
		self.assertEqual(TRACK.get_id(), 1051394215)
	
	def test_get_name(self):
		self.assertEqual(TRACK.get_name(), TRACK_QUERY)
		
	def test_get_price(self):
		self.assertEqual(TRACK.get_price(), (1.29, 'USD'))
		
	def test_grab_author(self):
		self.assertIsInstance(TRACK.grab_author(), itunesearch.Author)

	def test_grab_collection(self):
		self.assertIsInstance(TRACK.grab_collection(), itunesearch.Collection)
		
	def test_is_explicit(self):
		self.assertFalse(TRACK.is_explicit())

class TestCollection(unittest.TestCase):

	def test_get_artwork(self):
		self.assertIn('256x256', COLLECTION.get_artwork())
		
	def test_get_name(self):
		self.assertEqual(COLLECTION.get_name(), COLLECTION_QUERY)
	
class TestAuthor(unittest.TestCase):

	def test_get_id_get_view_url(self):
		self.assertIn(str(AUTHOR.get_id()), AUTHOR.get_view_url())
	
if __name__ == '__main__':
	unittest.main()
