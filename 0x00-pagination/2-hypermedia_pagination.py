#!/usr/bin/env python3
"""
:returns a list of indexes for the given page and page size
"""

import csv
from typing import List, Dict

index_range = __import__('0-simple_helper_function').index_range


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        """
        Return a page of the dictionary of the dataset
        :param page:
        :param page_size:
        :return:
        """
        assert type(page) is int and page > 0
        assert type(page_size) is int and page_size > 0
        start, end = index_range(page, page_size)
        try:
            return {
                'page_size': page_size,
                'page': page,
                'data': self.dataset()[start:end],
                'next_page': page + 1
                if page < len(self.dataset()) // page_size + 1 else None,
                'prev_page': page - 1 if page > 1 else None,
                'total_pages': len(self.dataset()) // page_size + 1
            }
        except IndexError:
            return {
                'page_size': page_size,
                'page': page,
                'data': [],
                'next_page': None,
                'prev_page': None,
                'total_pages': 0
            }
