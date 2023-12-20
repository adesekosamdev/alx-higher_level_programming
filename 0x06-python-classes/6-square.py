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

    @property
    def position(self):
        """tuple position"""

        return self.__position

    @position.setter
    def position(self, value):
        """ set posotion of the square

        Args:
            value (tuple): position
        """
        if type(value) is not tuple:
            raise TypeError('position must be a tuple of 2 positive integers')
        elif len(value) is not 2:
            raise TypeError('position must be a tuple of 2 positive integers')
        elif type(value[0]) is not int or type(value[1]) is not int:
            raise TypeError('position must be a tuple of 2 positive integers')
        elif value[0] < 0 or value[1] < 0:
            raise TypeError('position must be a tuple of 2 positive integers')
        else:
            self.__position = value

    def area(self):
        """returns the current square area"""
        return self.__size**2

    def my_print(self):
        """prints in stdout the square with the character #"""
        if self.__size == 0:
            print()
        else:
            for k in range(self.__position[1]):
                print()
            for i in range(self.__size):
                if (self.__position[0] != 0):
                    for li in range(self.__position[0]):
                        print(' ', end='')
                for j in range(self.__size):
                    print('#', end='')
                print()
