#!/usr/bin/python3
"""
Create a class FIFOCache that inherits
from BaseCaching and is a caching system
"""
BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """
    class FIFOCache that inherits from BaseCaching
    """
    def __init__(self):
        ''' Initialize class instance. '''
        super().__init__()
        self.keys = []
        self.last = ''

    def put(self, key, item):
        """
        assign to the dictionary self.cache_data the item value for the key key
        you must discard the first item put in cache (LIFO algorithm)
        """
        if key is not None and item is not None:
            self.cache_data[key] = item
            if key not in self.keys:
                self.keys.append(key)
            if len(self.keys) > BaseCaching.MAX_ITEMS:
                discard = self.keys.pop(BaseCaching.MAX_ITEMS - 1)
                del self.cache_data[self.last]
                print('DISCARD: {:s}'.format(self.last))
            self.last = key

    def get(self, key):
        """
         return the value in self.cache_data linked to key
        """
        if key is not None and key in self.cache_data:
            return self.cache_data[key]
        else:
            return None
