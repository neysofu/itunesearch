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

	def get_duration(self, readable=False):
		duration = timedelta(milliseconds=self['trackTimeMillis'])
		return str(duration) if readable else duration

	def is_explicit(self):
		return self['trackExplicitness'] == 'explicit'

	def get_id(self):
		return self['trackId']

	def get_name(self, censored=False):
		return self['trackNameCensored'] if censored else self['trackName']

	def get_price(self):
		return self['trackPrice'], self['currency']

	def grab_author(self):
		return core.lookup(self['artistId'])

	def grab_collection(self):
		return core.lookup(self['collectionId'])

class Collection(Item):
	pass

class Author(Item):
		
	def get_name(self):
		return self['artistName']

	def get_id(self):
		return self['artistId']

	def get_store_url(self):
		return self['artistLinkUrl']
