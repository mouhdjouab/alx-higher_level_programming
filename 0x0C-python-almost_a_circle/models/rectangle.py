#!/usr/bin/python3
"""0x0C. Python - Almost a circle, task 2 - 13"""
from models.base import Base


class Rectangle(Base):
    """Creates rectangle objects with two dimensions and offset coordinates.

    Uses the superclass `__init__` to create a valid instance id and sets
    instance variables from the provided arguments.

    Args:
        width (int): The x dimension of the rectangle.
        height (int): The y dimension of the rectangle.
        x (int): The horizontal offset of the rectangle.
        y (int): The vertical offset of the rectangle.
        id (int): The unique identifier for each instance of the superclass.



    """
    def __init__(self, width, height, x=0, y=0, id=None):
          '''Constructor.'''
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def __integer_validator(self, attr, value):
        """Method for validating the value."""
        if type(value) is not int:
            raise TypeError('{} must be an integer'.format(attr))
        if attr is 'width' or attr is 'height':
            if value <= 0:
                raise ValueError('{} must be > 0'.format(attr))
        elif attr is 'x' or attr is 'y':
            if value < 0:
                raise ValueError('{} must be >= 0'.format(attr))

    @property
    def width(self):
        """Width of  rectangle"""
        return self.__width

    @width.setter
    def width(self, value):

        self.__integer_validator('width', value)
        self.__width = value

    @property
    def height(self):
        """height of  rectangle"""
        return self.__height

    @height.setter
    def height(self, value):

        self.__integer_validator('height', value)
        self.__height = value

    @property
    def x(self):
        """x of  rectangle """
        return self.__x

    @x.setter
    def x(self, value):

        self.__integer_validator('x', value)
        self.__x = value

    @property
    def y(self):
        """y of  rectangle"""
        return self.__y

    @y.setter
    def y(self, value):

        self.__integer_validator('y', value)
        self.__y = value

    def area(self):
        """
        Returns area of rectangle as product of `width` and `height`.

        """
        return self.width * self.height

    def display(self):
        """ Prints the representation of a rectangle to stdout using '#'
        """
        display = ''
        for row in range(self.y):
            display += '\n'
        for row in range(self.height):
            for column in range(self.x):
                display += ' '
            for column in range(self.width):
                display += '#'
            if row < self.height - 1:
                display += '\n'
        self.__display = display
        print(display)

    def __str__(self):
        """ Returns a string with the numeric representation of the rectangle.

        """
        return ('[Rectangle] ({:d}) {:d}/'.format(self.id, self.x) +
                '{:d} - {:d}/{:d}'.format(self.y, self.width, self.height))

    def update(self, *args, **kwargs):
        """Updates attributes in a given order based on a variable number of non-keyword args or in any order with keyword args """
        if len(args) == 0:
            if len(kwargs) == 0 or len(kwargs) > 5:
                raise TypeError('Rectangle.update() takes 1 to 5 keyword,' +
                                ' or 1 to 5 non-keyword arguments')
            else:
                for key, value in kwargs.items():
                    if key == 'id':
                        self.id = value
                        Base._Base__assigned_ids.add(value)
                    elif key == 'width':
                        self.width = value
                    elif key == 'height':
                        self.height = value
                    elif key == 'x':
                        self.x = value
                    elif key == 'y':
                        self.y = value
                    else:
                        raise KeyError('invalid attribute name: ' +
                                       '{}'.format(key))
        elif len(args) > 5:
            raise TypeError('Rectangle.update() takes 1 to 5 keyword,' +
                            ' or 1 to 5 non-keyword arguments')
        else:
            for i, arg in enumerate(args):
                if i == 0:
                    if self.id != arg:
                        self.id = arg
                        Base._Base__assigned_ids.add(arg)
                elif i == 1:
                    self.width = arg
                elif i == 2:
                    self.height = arg
                elif i == 3:
                    self.x = arg
                elif i == 4:
                    self.y = arg

    def to_dictionary(self):
        """Creates dictionary representation of self without revealing private
        attribute names, as would __dict__.

        Returns:
            self_dict (dict): custom dictionary of private attribute values
                populated using getters


        """
        self_dict = dict()
        self_dict['id'] = self.id
        self_dict['width'] = self.width
        self_dict['height'] = self.height
        self_dict['x'] = self.x
        self_dict['y'] = self.y
        return self_dict
