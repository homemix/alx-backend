#!/usr/bin/python3
"""
FIFO Cache module
"""

BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """ FIFOCache defines:
      - a FIFO cache system
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
        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            key = self.cache_data_queue.pop(0)
            self.cache_data.pop(key)
            print(f'DISCARD: {key}')

        if key is not None and item is not None:
            self.cache_data_queue.append(key)
            self.cache_data[key] = item

    def get(self, key):
        """
        Get an item by key
        """
        if key is not None:
            return self.cache_data.get(key)
        return None
