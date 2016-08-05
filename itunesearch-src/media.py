# -*- coding: utf-8 -*-
from datetime import timedelta
from . import core


class Media:

    def __init__(self, json_data):
        self.json = json_data
        self.type = self.json.get('wrapperType', self.json.get('kind', None))

    def __getitem__(self, item):
        return self.json.get(item, None)

    def get_album(self):
        return core.Application.lookup(self.get_album_id())

    def get_album_explicitness(self):
        return self['collectionExplicitness']

    def get_album_id(self):
        return self['collectionId']

    def get_album_name(self, explicit=True):
        if explicit:
            return self['collectionName']
        else:
            return self['collectionCensoredName']

    def get_album_price(self):
        return '{0} {1}'.format(self['collectionPrice'], self['currency'])

    def get_album_url(self):
        return self['collectionViewUrl']

    def get_artist(self):
        return core.Application.lookup(self.get_artist_id())

    def get_artist_name(self):
        return self['artistName']

    def get_artist_type(self):
        return self['artistType']

    def get_artist_url(self):
        return self['artistViewUrl']

    def get_genre_id(self):
        return self['primaryGenreId']

    def get_genre_name(self):
        return self['primaryGenreName']

    def get_track_duration(self):
        msecs = self['trackTimeMillis']
        if msecs:
            secs = round(msecs / 1000)
            return timedelta(seconds=secs)
        else:
            return msecs

    def get_track_explicitness(self):
        return self['trackExplicitness']

    def get_track_name(self, explicit=True):
        if explicit:
            return self['trackName']
        else:
            return self['trackCensoredName']

    def get_track_number(self):
        return self.json['trackCount']

    def get_track_preview_url(self):
        return self['previewUrl']

    def get_track_price(self):
        return '{0} {1}'.format(self['trackPrice'], self['currency'])

    def get_track_url(self):
        return self['trackViewUrl']

    def get_artwork(self, size=2048):
        px = '{0}x{0}'.format(size)
        return (self['artworkUrl30']).replace('30x30', px)

    def get_content_advisory_rating(self):
        return self['contentAdvisoryRating']

    def get_country(self):
        return self['country']

    def get_disc_number(self):
        return self['discCount']

    def get_release_date(self):
        return self['releaseDate']

    def get_artist_id(self, idtype='itunes'):
        return {
            'itunes' : self['artistId'],
            'amg' : self['amgArtistId']
        }.get(idtype.lower(), None)
