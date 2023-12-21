#!/usr/bin/python3
"""Defines a MagicClass that replicates given bytecode."""


import math


class MagicClass:
    """MagicClass that replicates the given bytecode."""

    def __init__(self, radius=0):
        """Initialize a new instance of MagicClass.

        Args:
            radius (int or float): The radius of the circle.
        """
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError('radius must be a number')
        self.__radius = radius

    def area(self):
        """Calculate the area of the circle.

        Returns:
            float: The area of the circle.
        """
        return self.__radius ** 2 * math.pi

    def circumference(self):
        """Calculate the circumference of the circle.

        Returns:
            float: The circumference of the circle.
        """
        return 2 * math.pi * self.__radius


if __name__ == "__main__":
    # Example usage:
    my_circle = MagicClass(5)
    print("Area:", my_circle.area())
    print("Circumference:", my_circle.circumference())
