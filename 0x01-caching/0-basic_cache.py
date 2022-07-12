#!/usr/bin/python3
"""
BaseCaching module
"""
BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """
    BasicCache module
    """

    def __init__(self):
        """
        Initialize
        """
        super().__init__()

    def put(self, key, item):
        """ Add an item in the cache
        """
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """
        Get an item by key
        """
        if key is not None and key in self.cache_data:
            return self.cache_data.get(key)
