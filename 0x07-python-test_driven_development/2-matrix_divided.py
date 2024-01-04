def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by a given number.

    Args:
    - matrix (list of lists): The input matrix containing integers or floats.
    - div (int or float): The divisor.

    Returns:
    list of lists: A new matrix with elements rounded to 2 decimal places.

    Raises:
    - TypeError: If the matrix is not a list of lists of integers/floats, or if div is not a number.
    - TypeError: If each row of the matrix does not have the same size.
    - ZeroDivisionError: If div is equal to 0.
    """

    # Check if matrix is a list of lists of integers/floats
    if not all(isinstance(row, list) and all(isinstance(x, (int, float)) for x in row) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    # Check if each row of the matrix has the same size
    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    # Check if div is a number
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    # Check if div is not equal to 0
    if div == 0:
        raise ZeroDivisionError("division by zero")

    # Divide each element of the matrix by div and round to 2 decimal places
    result_matrix = [[round(x / div, 2) for x in row] for row in matrix]

    return result_matrix

# Example usage
if __name__ == "__main__":
    matrix = [
        [1, 2, 3],
        [4, 5, 6]
    ]
    print(matrix_divided(matrix, 3))
    print(matrix)
