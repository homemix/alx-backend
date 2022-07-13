#!/usr/bin/python3
"""
returns the value of the key in the cache in MRU cache
"""

BaseCaching = __import__('base_caching').BaseCaching


class MRUCache(BaseCaching):
    """
    returns the value of the key in the cache in MRU cache
    """

    MAX_ITEMS = 4
    COUNT = 0

    def __init__(self):
        super().__init__()
        self.cache_data_list = []

    def put(self, key, item):
        if key is not None and item is not None and key not in self.cache_data:
            if len(self.cache_data) >= self.MAX_ITEMS:
                del_key = self.cache_data_list.pop()
                del self.cache_data[del_key]
                print("DISCARD: {}".format(del_key))
            if key in self.cache_data:
                self.cache_data_list.remove(key)
            self.cache_data[key] = item
            self.cache_data_list.append(key)

    def get(self, key):
        if key in self.cache_data_list:
            self.cache_data_list.remove(key)
            self.cache_data_list.append(key)
            return self.cache_data.get(key)
        return None

    def print_cache(self):
        print("Current cache:")
        for key in sorted(self.cache_data.keys()):
            print("{}: {}".format(key, self.cache_data.get(key)))
