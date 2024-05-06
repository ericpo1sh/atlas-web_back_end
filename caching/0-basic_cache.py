#!/usr/bin/python3
""" BasicCache module """
BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """ constants of your caching system where your data are stored"""

    def put(self, key, item):
        ''' put '''
        if key is None or item is None:
            return
        self.cache_data[key] = item

    def get(self, key):
        ''' get '''
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
