#!/usr/bin/env python3
""" LRUCache module """
from collections import OrderedDict
BaseCaching = __import__('base_caching').BaseCaching


class LRUCache(BaseCaching):
    ''' LRUCache Dictionary class '''
    def __init__(self):
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        ''' must discard the least recently used item (LRU algorithm) '''
        if key is None or item is None:
            return
        if key is self.cache_data:
            self.cache_data.move_to_end(key)  # func from imprt to mark it used
        elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:  # when full rm 1
            discard = next(iter(self.cache_data))
            del self.cache_data[discard]
            print(f"DISCARD: {discard}")
        self.cache_data[key] = item  # add new item to cache

    def get(self, key):
        ''' Must return the value in self.cache_data linked to key. '''
        if key is None or key not in self.cache_data:
            return
        self.cache_data.move_to_end(key)  # move key, mark it as recently used
        return self.cache_data[key]
