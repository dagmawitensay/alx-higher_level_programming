#!/usr/bin/python3
"""
The rectangle module contains the Reactangle class for the models.
"""
from models.base import Base



class Rectangle(Base):
    """
    Rectangle class for the models.
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """Instanitaion of the Rectangle instance"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """
        Getter method for width.
        Returns:
            width
        """
        return self.__width

    @width.setter
    def width(self, width):
        """
        Setter method for width.
        """
        if type(width) != int:
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width

    @property
    def height(self):
        """
        Getter method for height.
        Returns:
            height.
        """
        return self.__height

    @height.setter
    def height(self, height):
        """
        Setter mehtod for height.
        """
        if type(height) != int:
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height

    @property
    def x(self):
        """
        Getter method for x.
        Returns:
            x
        """
        return self.__x

    @x.setter
    def x(self, x):
        """
        Setter method for x.
        """
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

    @property
    def y(self):
        """
        Getter mehod for y.
        Returns:
            y
        """
        return self.__y

    @y.setter
    def y(self, y):
        """
        Setter method for y.
        Returns:
            y
        """
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y

    def area(self):
        """Returns the area of the rectangle"""
        return self.width * self.height

    def display(self):
        """prints the rectangle using #"""
        rectangle = ""
        print_symbol = "#"
        # for i in range(self.height):
        #    for j in range(self.width):
        #        print("#", end="")
        #    print()

        for i in range(self.height):
            rectangle += (" " * self.x) + (print_symbol*self.width) + "\n"
        print(rectangle, end="")

    def __str__(self):
        """Returns the string representation."""
        return '[Rectangle] ({}) {}/{} - {}/{}'.format(self.id, self.x, self.y, self.width, self.height)

    def update(self, *args, **kwargs):
        """Update attributes based ont the values of args."""
        if len(args) != 0:
            for i in range(len(args)):
                if i == 0:
                    self.id = args[0]
                elif i == 1:
                    self.width = args[i]
                elif i == 2:
                    self.height = args[i]
                elif i == 3:
                    self.x = args[i]
                elif i == 4:
                    self.y = args[i]
        else:
            if kwargs is not None:
                for k, v in kwargs.items():
                    if k == 'id':
                        self.id = v
                    elif k == 'width':
                        self.width = v
                    elif k == 'height':
                        self.height = v
                    elif k == 'x':
                        self.x = v
                    elif k == 'y':
                        self.y = v

    def to_dictionary(self):
        """
        Returns the dictonary representation of the recntangle.
        """
        return {'id': getattr(self, 'id'),
                'x': getattr(self, 'x'),
                'y': getattr(self, 'y'),
                'width': getattr(self, 'width'),
                'height': getattr(self, 'height')}
