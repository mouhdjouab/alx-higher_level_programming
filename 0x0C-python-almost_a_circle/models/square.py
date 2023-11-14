#!/usr/bin/python3
"""0x0C. Python - Almost a circle, task 10 - 14"""
from models.rectangle import Rectangle
from models.base import Base


class Square(Rectangle):
    """Creates square objects with two dimensions and offset coordinates.

    Uses the super-superclass `Base` __init__ to create a valid instance id,
    and passes arguments to the superclass `__init__` to set attributes.
    Does not create its own attributes. `size` acts as an alias for `width`/`height`.

    Args:
        size (int): The x and y dimensions of the square.
        x (int): The horizontal offset of the square.
        y (int): The vertical offset of the square.
        id (int): The unique identifier for each instance of super().super().



    """
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Returns str with num representation of square

        Returns:
            '[Square] (<id>) <x>/<y> - <size>'


        """
        return ('[Square] ({:d}) {:d}/'.format(self.id, self.x) +
                '{:d} - {:d}'.format(self.y, self.width))

    @property
    def size(self):
        """Size of this square
        """
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Updates instance attributes via no-keyword & keyword args..
        """
        if len(args) == 0:
            if len(kwargs) == 0 or len(kwargs) > 4:
                raise TypeError('Square.update() takes 1 to 4 keyword,' +
                                ' or 1 to 4 non-keyword arguments')
            else:
                for key, value in kwargs.items():
                    if key == 'id':
                        if self.id != value:
                            temp = self.id
                            self.id = value
                            Base._Base__assigned_ids.remove(temp)
                            Base._Base__assigned_ids.add(value)
                    elif key == 'size':
                        self.size = value
                    elif key == 'x':
                        self.x = value
                    elif key == 'y':
                        self.y = value
                    else:
                        raise KeyError('invalid attribute name: ' +
                                       '{}'.format(key))
        elif len(args) > 4:
            raise TypeError('Square.update() takes 1 to 4 keyword,' +
                            ' or 1 to 4 non-keyword arguments')
        else:
            for i, arg in enumerate(args):
                if i == 0:
                    if self.id != arg:
                        temp = self.id
                        self.id = arg
                        Base._Base__assigned_ids.remove(temp)
                        Base._Base__assigned_ids.add(arg)
                elif i == 1:
                    self.size = arg
                elif i == 2:
                    self.x = arg
                elif i == 3:
                    self.y = arg

    def to_dictionary(self):
        """Returns dictionary representation of this class.
        """
        self_dict = dict()
        self_dict['id'] = self.id
        self_dict['size'] = self.size
        self_dict['x'] = self.x
        self_dict['y'] = self.y
        return self_dict
