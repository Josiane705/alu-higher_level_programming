#!/usr/bin/python3
class Rectangle:
    def __init__(self, width=0, height=0):
        # Initialize the rectangle with optional width and height values (default is 0)
        self.width = width
        self.height = height

    @property
    def width(self):
        # Getter for width
        return self.__width

    @width.setter
    def width(self, value):
        # Setter for width with validation
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        # Getter for height
        return self.__height

    @height.setter
    def height(self, value):
        # Setter for height with validation
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        # Calculate and return the area of the rectangle
        return self.__width * self.__height

    def perimeter(self):
        # Calculate and return the perimeter of the rectangle
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        # String representation of the rectangle using '#' character
        if self.__width == 0 or self.__height == 0:
            return ""
        return "\n".join(["#" * self.__width] * self.__height)

    def __repr__(self):
        # Official string representation (used in the interactive interpreter)
        return f"<{self.__class__.__name__} {self.__width}, {self.__height}>"

