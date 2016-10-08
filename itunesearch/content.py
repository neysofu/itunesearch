# -*- coding: utf-8 -*-
from datetime import timedelta
from . import core
from . import util

class Item:

	def __init__(self, response):
		self.response = response

	def __getitem__(self, item):
		try:
			return self.response[item]
		except IndexError:
			raise util.DefectiveResponseError

# Subclasses
# ----------

class Track(Item):

	def __init__(self, response):
		Item.__init__(self, response)

	def get_artwork(self, resolution=256):
		return self['artworkUrl60'].replace('60x60', '{0}x{0}'.format(resolution))
	
	def get_duration(self, readable=False):
		duration = timedelta(seconds=self['trackTimeMillis']//1000)
		return str(duration) if readable else duration

	def get_id(self):
		return self['trackId']

	def get_name(self, censored=False):
		return self['trackNameCensored'] if censored else self['trackName']

	def get_price(self):
		return self['trackPrice'], self['currency']

	def get_track_number(self):
		return self['trackNumber']

	def grab_author(self):
		return core.lookup(self['artistId'])

	def grab_collection(self):
		return core.lookup(self['collectionId'])
	
	def is_explicit(self):
		return 'not' not in self['trackExplicitness']

class Collection(Item):
	
	def __init__(self, response):
		Item.__init__(self, response)

	def get_artwork(self, resolution=256):
		return self['artworkUrl60'].replace('60x60', '{0}x{0}'.format(resolution))

	def get_description(self):
		return self['description']

	def get_name(self, censored=False):
		return self['collectionNameCensored'] if censored else self['collectionName']

	def get_preview_url(self):
		return self['previewUrl']

	def get_price(self):
		return self['collectionPrice'] + self['currency']

	def get_size(self):
		return self['trackCount']

	def get_view_url(self):
		return self['collectionViewUrl']
	
	def grab_author(self):
		return core.lookup(self['artistId'])

	def is_explicit(self):
		return 'not' not in self['collectionExplicitness']

class Author(Item):
		
	def __init__(self, response):
		Item.__init__(self, response)
	
	def get_name(self):
		return self['artistName']

	def get_id(self):
		return self['artistId']

	def get_view_url(self):
		return self['artistLinkUrl']

class Audiobook(Item):

	def __init__(self, response):
		Item.__init__(self, response)

	def get_artwork(self, resolution=256):
		return self['artworkUrl60'].replace('60x60', '{0}x{0}'.format(resolution))
	
	def get_description(self):
		return self['description']

	def get_preview_url(self):
		return self['previewUrl']

	def get_price(self):
		return self['collectionPrice'] + self['currency']

	def grab_author(self):
		return core.lookup(self['artistId'])

