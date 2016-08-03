# -*- coding: utf-8 -*-
import requests
import functools
import itunesearch.errors
from .media import CLASSIFIER


class Request:

    def __init__(self, url, parameters):
        self.url = url
        self.params = parameters
        self.response = self.get_response()

    def get_response(self):
        return requests.get(self.url, self.params).json()

    def is_erraneus(self):
        return 'errorMessage' in self.response

    def error_pipeline(self):
        if self.is_erraneus():
            raise MalformedRequestError(self.response['errorMessage'])

    def list_results(self):
        self.error_pipeline()
        for result in self.response['results']:
            classtype = result.get('kind', result.get('wrapperType', None))
            yield CLASSIFIER(classtype)(result)


class Application:

    HOSTNAME = 'http://itunes.apple.com/'

    SEARCH_HOSTNAME = HOSTNAME + 'search'
    LOOKUP_HOSTNAME = HOSTNAME + 'lookup'

    def search(term, country=None, media=None, entity=None, attribute=None,
               limit=None, lang=None, explicit=None):
        '''
        Sends a ``GET`` request to the iTunes Search API with the
        selected parameters and performs.

        :param term:
            The text string you want to search for, e.g., ``'jack johnson'``.
        :param country:
            The ``ISO 3166-1-alpha-2`` country code for the store you want
            to search, e.g., ``'FR'``.
        :param media:
            The media type you want to search for, e.g., ``'movie'``.
        :param entity:
            The type of results you want returned, relative to the specified
            media type, e.g., ``'movieArtist'`` for a ``'movie'`` media type
            search.
        :param attribute:
            The attribute you want to search for in the stores, relative to
            the specified media type; e.g., specify
            ``entity='allArtist'`` and ``attribute='allArtistTerm'``
            if you want to search for an artist by name.
        :param limit:
            The number of search results you want the iTunes Store to return,
            e.g., ``25``.
        :param lang:
            The language, English or Japanese, you want to use when returning
            search results, e.g. ``'ja_jp'``. Specify the language using the
            five-letter codename.
        :param explicit:
            A boolean flag indicating whether or not you want to include
            explicit content in your search results, e.g., ``True``.
        '''
        parameters = {k:v for (k,v) in locals().items() if v != None}
        if not('explicit'):
            parameters['explicit'] = 'no'
        return Request(Application.SEARCH_HOSTNAME, parameters)

    def lookup(itunes_id):
        return Request(Application.LOOKUP_HOSTNAME, {'id':itunes_id})

    #search_artist = functools.partial(self.search, entity='allArtist')
    #search_song = functools.partial(self.search, entity='song')
