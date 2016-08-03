# -*- coding: utf-8 -*-


class MalformedRequestError(Exception):
    pass


class UnavailableInformationError(Exception):
    '''
    This error is raised whenever the user accesses undefined properties
    of ``Item`` objects.
    '''
    pass
