#!/usr/bin/python3
""" BasicCache module """
BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """ BasicCaching defines:
    constants of your caching system
    where your data are stored (in a dictionary) """
    def __init__(self):
        ''' Initialize '''
        self.cache_data = {}

    def put(self, key, item):
        if key is None or item is None:
            return
        self.cache_data[key] = item

    def get(self, key):
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
