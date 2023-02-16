
# Finding Max Values in Rows that are also Min Values in Columns
This code provides a function find_max_in_row_min_in_col that takes a matrix as input and returns a list of numbers that are the maximum value in their respective rows but the minimum value in their respective columns. The function is implemented in Python and uses descriptive variable names and comments to improve readability and maintainability of the code.

## The find_max_in_row_min_in_col function can be imported and used as follows:

```python
from max_in_row_min_in_col import find_max_in_row_min_in_col

matrix = [
    [5, 16, 20],
    [9, 11, 18],
    [15, 16, 17]
]

result = find_max_in_row_min_in_col(matrix)
print(result)  # Output: [17]

```
##The function takes a matrix as input, where each row of the matrix is a list of integers. The function returns a list of integers that meet the criteria of being the maximum value in their respective rows but the minimum value in their respective columns.


## Run Locally

Clone the project

```bash
  git clone https://github.com/Godfrey-Ndungu/max-min-matrix.git
```
Go to project directory and create virtual environment and activate

```bash
  python3 -m venv venv
  source venv/bin/activate
```

Install dependencies

```bash
  pip install -r requirements.txt
```




## Running Tests
The code includes a test suite implemented using pytest. The tests can be run using the following command:

```bash
  pytest
```


## complexity

The time complexity of the find_max_in_row_min_in_col function is O(n^2), where n is the number of elements in the matrix, because the function iterates over each element of the matrix twice. The space complexity of the function is O(n), where n is the number of rows or columns in the matrix, because the function creates two lists of length n to store the maximum values in rows and the minimum values in columns.
