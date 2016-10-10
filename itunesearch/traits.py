# -*- coding: utf-8 -*-
import datetime
import itunesearch.core as itc

# Traits
# ------

class Streamable:

	def get_duration(self):
		return datetime.timedelta(milliseconds=self['trackTimeMillis'])

class Purchasable:

	def get_artwork(self, resolution):
		return self['artworkUrl60'].replace(
			'60x60bb',
			'{0}x{0}bb'.format(resolution) )

	def get_preview_url(self):
		return self['previewUrl']

	def get_price(self):
		return self['{0}Price'.format(self.entity)], self['currency']

	def get_release_date(self):
		return datetime.datetime.strptime(
			self['releaseDate'],
			'%Y-%m-%dT%H:%M:%SZ' )

	def grab_author(self):
		return itc.lookup(self['artistId'])

	def is_explicit(self): 
		return 'not' not in self['{0}Explicitness'.format(self.entity)]
