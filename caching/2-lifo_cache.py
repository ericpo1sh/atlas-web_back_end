#!/usr/bin/env python3
""" BasicCache module """
BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    ''' LIFOCaching Dictionary class '''

    def __init__(self):
        super().__init__()

    def put(self, key, item):
        ''' assign dictionary self.cache_data the item value for the key. '''
        if key is None or item is None:
            return
        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            discard, _ = self.cache_data.popitem()
            print(f"DISCARD: {discard}")
        self.cache_data[key] = item

    def get(self, key):
        ''' Must return the value in self.cache_data linked to key. '''
        if key is None or key not in self.cache_data:
            return
        return self.cache_data[key]
