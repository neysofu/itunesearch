# -*- coding: utf-8 -*-
from .core import MalformedRequestError
from .media import Media

def list_results(response):
    r = []
    if 'errorMessage' in response:
        raise MalformedRequestError(response['errorMessage'])
    for result in response['results']:
        r.append(Media(result))
    return r
