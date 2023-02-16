from typing import List

def find_max_in_row_min_in_col(matrix: List[List[int]]) -> List[int]:
    """
    Returns a list of numbers that are the maximum value in its row but the minimum in its column.
    
    Args:
    - matrix: A M X N matrix where each element is an integer
    
    Returns:
    - A list of integers that are the maximum value in its row but the minimum in its column
    
    Example:
    >>> matrix = [[5,16,20],[9,11,18],[15,16,17]]
    >>> find_max_in_row_min_in_col(matrix)
    [17]
    >>> matrix = [[100,60,20, 50],[70,80,10,90],[10,50,44,30]]
    >>> find_max_in_row_min_in_col(matrix)
    [50]
    """
    max_in_rows = [max(row) for row in matrix] # List of max values in each row
    min_in_cols = [min(col) for col in zip(*matrix)] # List of min values in each column

    matching_vals = []
    for row_idx, row in enumerate(matrix):
        matching_vals.extend(
            val
            for col_idx, val in enumerate(row)
            if val == max_in_rows[row_idx] and val == min_in_cols[col_idx]
        )
    return matching_vals
