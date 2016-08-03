# -*- coding: utf-8 -*-
import .GenericItem
import .Artist
import .Song


CLASSIFIER = {
    None : GenericItem,
    'song' : Song,
    'artist' : Artist}
