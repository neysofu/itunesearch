# -*- coding: utf-8 -*-
from . import content

# Errors
# ------

class MalformedRequestError(Exception):
	pass

class DefectiveResponseError(Exception):
	pass

# Helpers
# -------

def wrapper_class(response):
	# Nothing can describe the feelings `wrapperType` and `kind` cause
	wrap = 'wrapperType'
	if wrap in response:
		return {
			'track' : content.Track,
			'collection' : content.Collection,
			'artist' : content.Author
		}[response[wrap]](response)
	else: # ... you are pretty much fucked
		pass

def list_results(response):
	msg = 'errorMessage'
	if msg in response:
		raise MalformedRequestError(response[msg])
	return [wrapper_class(r) for r in response['results']]
