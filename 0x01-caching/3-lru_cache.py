#!/usr/bin/python3
"""
returns the value of the key in the cache
"""

from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """ LRUCache defines:
      - constants of your caching system
      - where your data are stored (in a dictionary)
    """
    MAX_ITEMS = 4
    COUNT = 0

    def __init__(self):
        """
        Initiliaze
        """
        super().__init__()
        self.cache_data_dict = {}

    def put(self, key, item):
        """ Add an item in the cache
        """
        if key is not None and item is not None and key not in self.cache_data:
            if len(self.cache_data) >= self.MAX_ITEMS:
                if key in self.cache_data_dict:
                    self.cache_data_dict[key] = self.COUNT
                    # self.COUNT += 1
                if key not in self.cache_data_dict:
                    del self.cache_data[
                        min(self.cache_data, key=self.cache_data.get)]
                    del self.cache_data_dict[
                        min(self.cache_data_dict,
                            key=self.cache_data_dict.get)]
                    self.cache_data[key] = item
                    self.cache_data_dict[key] = self.COUNT
                    # self.COUNT += 1
                    print(f'DISCARD: {key}')
            self.cache_data[key] = item
            self.cache_data_dict[key] = self.COUNT
            self.COUNT += 1

    def get(self, key):
        """ Get an item by key
        """
        if key is not None:
            return self.cache_data.get(key)
        return None
