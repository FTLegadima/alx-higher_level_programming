#!/usr/bin/python3
"""Lazy matrix multiplication using NumPy
"""

import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """Multiplies two matrices using NumPy.

    Args:
        m_a (list of lists): First matrix.
        m_b (list of lists): Second matrix.

    Returns:
        np.ndarray: Result of the matrix multiplication.

    Raises:
        TypeError: If m_a or m_b is not a list, not a list of lists,
                    contains non-integer/float elements, or not a rectangle.
        ValueError: If m_a or m_b is empty or matrices cannot be multiplied.

    """
    if not isinstance(m_a, list) or not isinstance(m_b, list):
        raise TypeError("m_a must be a list or m_b must be a list")
    if not all(isinstance(row, list) for row in m_a) or not all(isinstance(row, list) for row in m_b):
        raise TypeError("m_a must be a list of lists or m_b must be a list of lists")
    if not m_a or not all(row == [] for row in m_a) or not m_b or not all(row == [] for row in m_b):
        raise ValueError("m_a can't be empty or m_b can't be empty")

    num_cols_a = len(m_a[0])
    num_cols_b = len(m_b[0])

    for row in m_a:
        if not all(isinstance(element, (int, float)) for element in row):
            raise TypeError("m_a should contain only integers or floats")

        if len(row) != num_cols_a:
            raise TypeError("each row of m_a must be of the same size")

    for row in m_b:
        if not all(isinstance(element, (int, float)) for element in row):
            raise TypeError("m_b should contain only integers or floats")

        if len(row) != num_cols_b:
            raise TypeError("each row of m_b must be of the same size")

    if num_cols_a != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    result = np.dot(m_a, m_b)
    return result


if __name__ == "__main__":
    m_a = np.array([[1, 2], [3, 4]])
    m_b = np.array([[1, 2], [3, 4]])
    print(lazy_matrix_mul(m_a, m_b))  # Output: [[7, 10], [15, 22]]

    m_a = np.array([[1, 2]])
    m_b = np.array([[3, 4], [5, 6]])
    print(lazy_matrix_mul(m_a, m_b))  # Output: [[13, 16]]

