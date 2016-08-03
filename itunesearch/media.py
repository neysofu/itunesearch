# -*- coding: utf-8 -*-
from datetime import timedelta
from .core import MediaItem, Request, Application


class Song(MediaItem):

    STREAMABLE = True

    def get_album(self):
        return MediaItem(Application.lookup(self.get_album_id()))

    def get_album_explicitness(self):
        return self.json['collectionExplicitness']

    def get_album_id(self):
        return self.json['collectionId']

    def get_album_name(self, explicit=True):
        if explicit:
            return self.json['collectionName']
        else:
            return self.json['collectionCensoredName']

    def get_album_price(self):
        return str(self.json['collectionPrice']) + ' ' + self.json['currency']

    def get_album_url(self):
        return self.json['collectionViewUrl']

    def get_artist(self):
        return MediaItem(Application.lookup(self.get_artist_id()))

    def get_artist_id(self):
        return self.json['artistId']

    def get_artist_name(self):
        return self.json['artistName']

    def get_artist_url(self):
        return self.json['artistViewUrl']

    def get_genre_id(self):
        return self.json['primaryGenreId']

    def get_genre_name(self):
        return self.json['primaryGenreName']

    def get_track_duration(self):
        secs = round(self.json['trackTimeMillis'] / 1000)
        return timedelta(seconds=secs)

    def get_track_explicitness(self):
        return self.json['trackExplicitness']

    def get_track_name(self, explicit=True):
        if explicit:
            return self.json['trackName']
        else:
            return self.data['trackCensoredName']

    def get_track_number(self):
        return self.json['trackCount']

    def get_track_preview_url(self):
        return self.json['previewUrl']

    def get_track_price(self):
        return str(self.json['trackPrice']) + ' ' + self.json['currency']

    def get_track_url(self):
        return self.json['trackViewUrl']

    def get_artwork(self, size=2048):
        resolution = '{0}x{0}'.format(size)
        return (self.json['artworkUrl30']).replace('30x30', resolution)

    def get_content_advisory_rating(self):
        return self.json['contentAdvisoryRating']

    def get_country(self):
        return self.json['country']

    def get_disc_number(self):
        return self.json['discCount']

    def get_release_date(self):
        return self.json['releaseDate']


class Artist(MediaItem):

    STREAMABLE = False

    def get_artist_id(self, idtype='itunes'):
        iid = self.json['artistId']
        aid = self.json.get('amgArtistId', None)
        return id_handler(iid, aid, idtype)

    def get_artist_name(self):
        return self.json['artistName']

    def get_artist_type(self):
        return self.json['artistType']

    def get_artist_url(self):
        return self.json['artistViewUrl']

    def get_genre_id(self, idtype='itunes'):
        return self.json['primaryGenreId']

    def get_genre_name(self):
        return self.json['primaryGenreName']

CLASSIFIER = {
    None : MediaItem,
    'song' : Song,
    'artist' : Artist}
