import unittest
import itunesearch
import datetime
import random

TRACK_QUERY, COLLECTION_QUERY, AUTHOR_QUERY = random.choice([
	['When We Were Young', '25', 'Adele'],
	['On Top of the World', 'Night Visions', 'Imagine Dragons'],
	['Hymn for the Weekend', 'A Head Full of Dreams', 'Coldplay'] ])

TRACK = itunesearch.search_track(TRACK_QUERY)[0]
COLLECTION = itunesearch.search_collection(COLLECTION_QUERY)[0]
AUTHOR = itunesearch.search_author(AUTHOR_QUERY)[0]

# Test suits
# ----------

class TestTrack(unittest.TestCase):
	
	def test_get_artwork(self):
		n = random.randrange(30, 100)
		pattern = '{0}x{0}bb'.format(n)
		url = TRACK.get_artwork(resolution=n)
		self.assertIn(pattern, url)

	def test_get_country(self):
		self.assertIsInstance(TRACK.get_country(), str)

	def test_get_duration(self):
		self.assertIsInstance(TRACK.get_duration(), datetime.timedelta)
	
	def test_get_id(self):
		self.assertIsInstance(TRACK.get_id(), int)
	
	def test_get_name(self):
		self.assertEqual(TRACK.get_name(), TRACK_QUERY)
	
	def test_get_preview_url(self):
		self.assertIsInstance(TRACK.get_preview_url(), str)

	def test_get_price(self):
		self.assertIsInstance(TRACK.get_price()[0], float)
		self.assertIsInstance(TRACK.get_price()[1], str)

	def test_get_release_date(self):
		self.assertIsInstance(TRACK.get_release_date(), datetime.datetime)

	def test_get_track_number(self):
		self.assertIsInstance(TRACK.get_track_number()[0], int)
		self.assertIsInstance(TRACK.get_track_number()[1], int)

	def test_get_view_url(self):
		self.assertIsInstance(TRACK.get_view_url(), str)

	def test_grab_author(self):
		self.assertEqual(TRACK.grab_author(), AUTHOR)

	def test_grab_collection(self):
		self.assertEqual(TRACK.grab_collection(), COLLECTION)
		
	def test_is_explicit(self):
		self.assertIsInstance(TRACK.is_explicit(), bool)

class TestCollection(unittest.TestCase):

	def test_get_artwork(self):
		n = random.randrange(30, 100)
		pattern = '{0}x{0}bb'.format(n)
		url = COLLECTION.get_artwork(resolution=n)
		self.assertIn(pattern, url)
		
	def test_get_name(self):
		self.assertEqual(COLLECTION.get_name(), COLLECTION_QUERY)
	
class TestAuthor(unittest.TestCase):

	def test_get_id_get_view_url(self):
		self.assertIn(str(AUTHOR.get_id()), AUTHOR.get_view_url())
	
if __name__ == '__main__':
	unittest.main()
