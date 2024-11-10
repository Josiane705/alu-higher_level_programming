#!/usr/bin/python3
Rectangle = __import__('3-rectangle').Rectangle

# Create a rectangle with width 2 and height 4
my_rectangle = Rectangle(2, 4)
print("Area: {} - Perimeter: {}".format(my_rectangle.area(), my_rectangle.perimeter()))

# Print the rectangle using the string representation
print(str(my_rectangle))
print(repr(my_rectangle))

# Update the width and height
my_rectangle.width = 10
my_rectangle.height = 3
print("-- Updated Rectangle --")
print(my_rectangle)
print(repr(my_rectangle))

# Test invalid values for width and height
try:
    my_rectangle.width = "5"  # Invalid width (should raise TypeError)
except Exception as e:
    print(e)

try:
    my_rectangle.height = -3  # Invalid height (should raise ValueError)
except Exception as e:
    print(e)

# Create a rectangle with zero width and height
my_rectangle2 = Rectangle(0, 0)
print("Area: {} - Perimeter: {}".format(my_rectangle2.area(), my_rectangle2.perimeter()))
print(str(my_rectangle2))  # Should print an empty string

