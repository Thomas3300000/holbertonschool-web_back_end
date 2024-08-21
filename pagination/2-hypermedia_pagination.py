#!/usr/bin/env python3
"""Implement a get_hyper method that takes the same arguments (and defaults)
as get_page and returns a dictionary containing the following
key-value pairs"""
import csv
import math
from typing import List


def index_range(page: int, page_size: int) -> tuple:
    """The function should return a tuple of size two containing a start index
    and an end index corresponding to the range of indexes to return in
    a list for those particular pagination parameters"""
    start = (page - 1) * page_size
    end = start + page_size
    return (start, end)


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

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Return the appropriate page of the dataset"""
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0
        start, end = index_range(page, page_size)
        data = self.dataset()
        if start >= len(data):
            return []
        return data[start:end]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> dict:
        """ Returns a dictionary containing the following key-value pairs:

        page_size: the length of the returned dataset page
        page: the current page number
        data: the dataset page (equivalent to return from previous task)
        next_page: number of the next page, None if no next page
        prev_page: number of the previous page, None if no previous page
        total_pages: the total number of pages in the dataset as an integer"""
        data = self.get_page(page, page_size)
        pages = len(self.dataset())
        total = math.ceil(pages / page_size)

        next = page + 1 if page < total else None
        prev = page - 1 if page > 1 else None

        return {
            "page_size": len(data),
            "page": page,
            "data": data,
            "next_page": next,
            "prev_page": prev,
            "total_pages": total
        }
