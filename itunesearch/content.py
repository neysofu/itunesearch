# -*- coding: utf-8 -*-
import itunesearch.core as itc
from itunesearch import traits


# Subclasses
# ----------

class Track(
		itc.Item,
		traits.Music,
		traits.Streamable,
		traits.Purchasable ):

	def __init__(self, response):
		super().__init__(response, 'track')

	def get_country(self):
		return self['country']

	def get_track_number(self):
		return self['discNumber'], self['trackNumber']

	def grab_collection(self):
		return itc.lookup(self['collectionId'])
	
class Collection(
		itc.Item,
		traits.Music,
		traits.Purchasable ):
	
	def __init__(self, response):
		super().__init__(response, 'collection')

	def get_country(self):
		return self['country']

class Author(
		itc.Item,
		traits.Music ):
		
	def __init__(self, response):
		super().__init__(response, 'artist')

class Audiobook(itc.Item):

	def __init__(self, response):
		super().__init__(self, response, 'track')

	def get_description(self):
		return self['description']

	def grab_author(self):
		return itc.lookup(self['artistId'])

