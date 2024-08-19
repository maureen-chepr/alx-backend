#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
from typing import List, Dict


class Server:
    """Server class to paginate a database of popular baby names."""

    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset"""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0"""
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = 0, page_size: int = 10) -> Dict:
        """Get a page of the dataset with deletion-resilient pagination"""
        dataset = self.indexed_dataset()

        # Check if index is valid
        if not (isinstance(index, int) and index >= 0):
            raise AssertionError("Index must be a non-negative integer")
        if not (isinstance(page_size, int) and page_size > 0):
            raise AssertionError("Page size must be a positive integer")
        if index >= len(dataset):
            raise AssertionError("Index out of range")

        rows = []
        current_index = index

        while len(rows) < page_size:
            if current_index in dataset:
                rows.append(dataset[current_index])
            current_index += 1
            if current_index >= len(dataset):
                break

        return {
            "index": index,
            "data": rows,
            "page_size": len(rows),
            "next_index": current_index if len(rows) == page_size else None
            }
