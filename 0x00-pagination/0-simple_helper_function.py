#!/usr/bin/env python3
"""
Write a function named index_range that takes
two integer arguments page and page_size
"""


def index_range(page, page_size):
    """
    Return the index range for the given page and page size
    """
    return (page - 1) * page_size, page * page_size
