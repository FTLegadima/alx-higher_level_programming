#!/usr/bin/python3
"""Module defining the Rectangle class"""


class Rectangle:
    """Rectangle class with private width and height attributes"""

    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """Initialize the rectangle with optional width and height"""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Getter method for width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter method for width"""
        if not isinstance(value
