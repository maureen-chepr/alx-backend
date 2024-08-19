#!/usr/bin/env python3
"""Function that returns a tuple."""

from typing import Tuple

def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Return a tuple of size two containing a start index
    and an end index corresponding to the range of indexes
    to return in a list for those particular pagination parameters.
    """
    rtTuple = (page - 1) * page_size, page * page_size
    return (rtTuple)
