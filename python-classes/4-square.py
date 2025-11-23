#!/usr/bin/python3
"""This module defines a Square class with private size attribute,
getter/setter, area computation, and a method to print the square."""

class Square:
    """Defines a square object with size validation and printing."""

    def __init__(self, size=0):
        self.size = size

    @property
    def size(self):
        """Getter for size"""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter for size with type and value validation"""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return the current square area"""
        return self.__size ** 2

    def my_print(self):
        """Print the square with '#' characters"""
        if self.__size == 0:
            print("")
            return
        for _ in range(self.__size):
            print("#" * self.__size)
