#!/usr/bin/env python3
""" LRUCache Module """

from collections import OrderedDict
from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """
    A data structure that implements a Least Recently Used (LRU)
    mechanism for storing and retrieving items from a cache (dictionary)
    """
    def __init__(self):
        """Initializes the cache instance."""
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """Adds an item to the cache."""
        if key is not None and item is not None:
            if key not in self.cache_data:
                if len(self.cache_data) + 1 > self.MAX_ITEMS:
                    lru_key = self.cache_data.popitem(last=True)[0]
                    print("DISCARD:", lru_key)
            self.cache_data[key] = item
            self.cache_data.move_to_end(key, last=False)
        else:
            self.cache_data[key] = item

    def get(self, key):
        """Retrieves an item from the cache"""
        if key is not None and key in self.cache_data:
            self.cache_data.move_to_end(key, last=False)
        return self.cache_data.get(key)
