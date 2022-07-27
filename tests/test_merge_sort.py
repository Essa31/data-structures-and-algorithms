import pytest
from sorting.merge.merge_sort import *


def test_empty_array():
    """
    this function test an empty array ( the length of the array equals zero )
    """
    actual = merge_sort([])
    expected = 'EMPTY ARRAY'
    assert actual == expected


def test_len_equal_one():
    """
    this function test an array of length equal one
    """
    actual = merge_sort([1])
    expected = [1]
    assert actual == expected


def test_random_array():
    """
    this function test an array of random array
    """
    actual = merge_sort([8, 4, 23, 42, 16, 15])
    expected = [4, 8, 15, 16, 23, 42]
    assert actual == expected


def test_reverse_sorted_array():
    """
    this function test reverse sorted array
    """
    actual = merge_sort([20, 18, 12, 8, 5, -2])
    expected = [-2, 5, 8, 12, 18, 20]
    assert actual == expected


def test_few_uniques_array():
    """
    this function test an array of uniques number
    """
    actual = merge_sort([5, 12, 7, 5, 5, 7])
    expected = [5, 5, 5, 7, 7, 12]
    assert actual == expected


def test_nearly_sorted_array():
    """
    this function test an array of nearly sorted array
    """
    actual = merge_sort([2, 3, 5, 7, 13, 11])
    expected = [2, 3, 5, 7, 11, 13]
    assert actual == expected