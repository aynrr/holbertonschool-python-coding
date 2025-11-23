#!/usr/bin/python3
"""Square class definition with properties for size and area computation."""


class Square:
    """
    Defines a square object, allowing safe access and update of its size
    using properties (getters and setters).

    Attributes:
        __size (int): The side length of the square, enforced to be a non-negative integer.
    """

    def __init__(self, size=0):
        """
        Initializes a new Square instance.

        Args:
            size (int): The size of the new square. Defaults to 0.
        """
        # Setter metodunu çağırır. Bu, ilk instanslaşdırma zamanı
        # ölçü dəyərinin yoxlanılmasını təmin edir.
        self.size = size

    @property
    def size(self):
        """
        Getter metodu: Kvadratın cari ölçüsünü qaytarır.
        
        Returns:
            int: Kvadratın tərəf uzunluğu (__size).
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Setter metodu: Kvadratın ölçüsünü təyin edir və yoxlayır.

        Args:
            value (int): Təyin ediləcək yeni ölçü dəyəri.

        Raises:
            TypeError: Əgər value tam ədəd deyilsə.
            ValueError: Əgər value 0-dan kiçikdirsə.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Calculates and returns the current area of the square.

        The area is calculated as size * size.

        Returns:
            int: The area of the square. [Image of the formula for the area of a square]
        """
        return self.__size ** 2
