#!/usr/bin/python3
"""
LIFO Cache module
"""

BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """ LIFOCache defines:
      - a LIFO cache system
      - a max_items constant
    """

    def __init__(self):
        """
        Initialize
        """
        super().__init__()
        self.cache_data_queue = []

    def put(self, key, item):
        """
        Add an item in the cache
        """
        if key is not None and item is not None and key not in self.cache_data:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                removed = self.cache_data_queue.pop()
                self.cache_data.pop(removed)
                print(f'DISCARD: {removed}')
            self.cache_data_queue.append(key)
            self.cache_data[key] = item

    def get(self, key):
        """
        Get an item by key
        """
        if key is not None:
            return self.cache_data.get(key)
        return None
