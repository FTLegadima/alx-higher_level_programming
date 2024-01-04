def add_integer(a, b=98):
    """
    Adds two integers.

    Args:
    - a (int or float): The first number.
    - b (int or float): The second number (default is 98).

    Returns:
    int: The sum of a and b.

    Raises:
    TypeError: If a or b is not an integer or float.
    """

    # Check if a is not an int or float
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")

    # Check if b is not an int or float
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    # Convert a and b to integers
    a = int(a)
    b = int(b)

    # Return the sum of a and b
    return a + b

# Example usage
if __name__ == "__main__":
    print(add_integer(1, 2))        # Output: 3
    print(add_integer(100, -2))     # Output: 98
    print(add_integer(2))           # Output: 100
    print(add_integer(100.3, -2))   # Output: 98

    # Test cases with exceptions
    try:
        print(add_integer(4, "School"))
    except Exception as e:
        print(e)

    try:
        print(add_integer(None))
    except Exception as e:
        print(e)
