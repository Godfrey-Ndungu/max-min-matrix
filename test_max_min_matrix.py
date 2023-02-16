from max_min_matrix import find_max_in_row_min_in_col
import pytest

def test_find_max_in_row_min_in_col_1():
    matrix = [[5,16,20],[9,11,18],[15,16,17]]
    assert find_max_in_row_min_in_col(matrix) == [17]

def test_find_max_in_row_min_in_col_2():
    matrix = [[100,60,20, 50],[70,80,10,90],[10,50,44,30]]
    assert find_max_in_row_min_in_col(matrix) == [50]

