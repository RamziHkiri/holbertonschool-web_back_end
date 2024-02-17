#!/usr/bin/python3
"""
Create a class LRUCache that inherits from BaseCaching and is a caching system
"""
BaseCaching = __import__('base_caching').BaseCaching


class LRUCache(BaseCaching):
    """
    class LRUCache that inherits from BaseCaching
    """

    def __init__(self):
        """initilize instance"""
        super().__init__()
        self.preorities = {}
        self.preority = 0
        self.minKey = ''

    def put(self, key, item):
        """you must discard the least recently used item (LRU algorithm)"""
        if key is not None and item is not None:
            self.preority += 1
            self.cache_data[key] = item
            self.preorities[key] = self.preority

            if len(self.preorities) > BaseCaching.MAX_ITEMS:
                self.minKey = min(self.preorities,
                                  key=lambda k: self.preorities[k])
                del self.cache_data[self.minKey]
                del self.preorities[self.minKey]
                print('DISCARD: {:s}'.format(self.minKey))
                print(self.preorities)

    def get(self, key):
        """
         return the value in self.cache_data linked to key
        """
        if key is not None and key in self.cache_data:
            self.preority += 1
            self.preorities[key] = self.preority
            return self.cache_data[key]
        else:
            return None
