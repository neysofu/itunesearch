# -*- coding: utf-8 -*-
import requests
import functools
from . import util

# Global variables
# ----------------

HOSTNAME = 'http://itunes.apple.com/'

SEARCH_HOSTNAME = HOSTNAME + 'search'
LOOKUP_HOSTNAME = HOSTNAME + 'lookup'

# Public API
# ----------

def search(term, country=None, media=None, entity=None, attribute=None,
		   limit=None, lang=None, explicit=None):
    '''
    Sends a ``GET`` request to the iTunes Search API with the selected
	parameters and returns an object wrapper to the JSON response.

    :param term:
       The text string you want to search for; e.g., ``'jack johnson'``.
	:param country:
        The ``ISO 3166-1 alpha-2`` country code of the store you want to
		search for; e.g., ``'FR'``.
    :param media:
	    The media type you want to search for, e.g., ``'movie'``.
	:param entity:
		The type of results you want returned, relative to the specified media
		type, e.g., ``'movieArtist'`` for a ``'movie'`` media type search.
    :param attribute:
        The attribute you want to search for in the stores, relative to the
		specified media type; e.g., specify ``entity='allArtist'``
		and ``attribute='allArtistTerm'`` if you want to search for an artist
		by name.
    :param limit:
        The number of search results you want the iTunes Store to return, e.g.,
		``25``.
    :param lang:
        The language, English or Japanese, you want to use when returning
		search results, e.g. ``'ja_jp'``. Specify the language using the
		five-letter codename.
    :param explicit:
        A boolean flag indicating whether or not you want to include explicit
		content in your search results, e.g., ``True``.
    '''
    parameters = {k:v for (k,v) in locals().items() if v != None}
    if not('explicit'):
        parameters['explicit'] = 'no'
    response = requests.get(SEARCH_HOSTNAME, parameters).json()
    return util.list_results(response)

def lookup(itunes_id):
	response = requests.get(LOOKUP_HOSTNAME, {'id':itunes_id}).json()
	return util.list_results(response)[0]

search_author = functools.partial(search, entity='allArtist')
search_collection = functools.partial(search, entity='album')
search_track = functools.partial(search, entity='allTrack')
