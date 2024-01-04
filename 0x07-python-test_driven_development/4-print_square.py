def print_square(size):
    """
    Prints a square of '#' characters with the given size.

    Args:
    - size (int): The size length of the square.

    Raises:
    - TypeError: If size is not an integer.
    - ValueError: If size is less than 0.
    - TypeError: If size is a float and is less than 0.
    """

    # Check if size is an integer
    if not isinstance(size, int):
        raise TypeError("size must be an integer")

    # Check if size is less than 0
    if size < 0:
        raise ValueError("size must be >= 0")

    # Check if size is a float and less than 0
    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")

    # Print the square
    for i in range(size):
        print("#" * size)

# Example usage
if __name__ == "__main__":
    print_square(4)
    print("")
    print_square(10)
    print("")
    print_square(0)
    print("")
    print_square(1)

    try:
        print_square(-1)
    except Exception as e:
        print(e)
