# -*- coding: utf-8 -*-
import media.GenericItem

class GenericItem:

    def __init__(self, json_data):
        self.json = json_data

    def get_type(self):
        return self.json.get('kind', self.json.get('wrapperType', None))
