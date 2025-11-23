#!/usr/bin/python3
"""Module that defines a Square class, enforcing size validation and providing an area calculation method."""


class Square:
    """
    Defines a square object.
    """
    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        return self.__size ** 2
