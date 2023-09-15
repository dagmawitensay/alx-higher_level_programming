#!/usr/bin/python3
"""
This module contains a square class.
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    A square class that inherits from a Rectangle object.
    """
    def __init__(self, size, x=0, y=0, id=None):
        """Instantiation of the square class"""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """
        Returns size of the square.
        """
        return self.width

    @size.setter
    def size(self, value):
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.width = value
        self.height = height

    def __str__(self):
        """
        Returns the string representation of the square.
        """
        return '[Square] ({}) {}/{} - {}'.format(self.id, self.x, self.y, self.size)

    def update(self, *args, **kwargs):
        """
        Updates the attributes of the square instance.
        """
        if args and len(args) > 0:
            for i in range(len(args)):
                if i == 0:
                    self.id = args[i]
                elif i == 1:
                    self.width = args[i]
                    self.height = args[i]
                elif i == 2:
                    self.x = args[i]
                elif i == 3:
                    self.y = args[i]
        else:
            if kwargs is not None:
                for k, v in kwargs.items():
                    if k == 'id':
                        self.id = v
                    elif k == 'size':
                        self.width = v
                        self.height = v
                    elif k == 'x':
                        self.x = v
                    elif k == 'y':
                        self.y = v

    def to_dictionary(self):
        """
        Returns the string representation of the square instance.
        """
        return {'id': getattr(self, 'id'),
                'x': getattr(self, 'x'),
                'y': getattr(self, 'y'),
                'width': getattr(self, 'width'),
                'height': getattr(self, 'height')}

