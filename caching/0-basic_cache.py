#!/usr/bin/env python3
""" BasicCache module """
BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """ Cacing Dictionary class """

    def put(self, key, item):
        ''' put: assign to the dictionary self.cache_data the item value. '''
        if key is None or item is None:
            return

        self.cache_data[key] = item
    def get(self, key):
        ''' get : return the value in self.cache_data linked to key '''
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
