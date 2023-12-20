#!/usr/bin/python3
"""class Square that defines a square"""


class Square:
    """class Square that defines a square"""
    def __init__(self, size=0):
        """Instantiation with size"""
        self.size = size

    @property
    def size(self):
        """retrieves size"""
        return self.__size

    @size.setter
    def size(self, value):
        """sets size"""
        if type(value) is not int:
            raise TypeError('size must be an integer')
        elif value < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = value

    def area(self):
        """returns the current square area"""
        return self.__size**2

    def my_print(self):
        """prints in stdout the square with the character #"""
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                for j in range(self.__size):
                    print('#', end='')
                print()
