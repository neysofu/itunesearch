# -*- coding: utf-8 -*-
from itunesearch.GenericItem import GenericItem


class Artist(GenericItem):

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
