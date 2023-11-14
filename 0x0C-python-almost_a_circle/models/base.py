#!/usr/bin/python3
''' base classe module'''

import json
import csv


class Base:
    """Manages the assignment of unique identifiers (`id`) and related attributes across all instances.

    This class assigns a valid `id` based on the provided argument. If no argument is given,
    it uses the current count of instances, `__nb_objects`. Additionally, the implementation includes:
    - `__assigned_ids` (set[int]): a set containing all `id` values assigned at least once.
    - `__serial` (int) + getter/setter: Represents `__nb_objects` after the initialization of the instance.
      It remains constant even if the `id` changes.

    Args:
        id (int, optional): Identifying number for each instance of `Base`. If not provided, it is assigned
            based on the current count of instances.

    Attributes:
        __nb_objects (int): Number of `Base` instances not assigned an `id` at initialization.
        __true_nb_objects (int): Total count of all `Base` instances.
        __assigned_ids (set[int]): Set of all `id` numbers assigned at least once.



"""
    __nb_objects = 0
    __true_nb_objects = 0
    __assigned_ids = set()



    def __init__(self, id=None):
        if id is not None:

            self.id = id

            Base.__true_nb_objects += 1
            self.serial = Base.__true_nb_objects
            Base.__assigned_ids.add(self.id)
        else:

            Base.__nb_objects += 1
            self.id = Base.__nb_objects

            Base.__true_nb_objects += 1
            self.serial = Base.__true_nb_objects
            Base.__assigned_ids.add(self.id)

    @property
    def id(self):
        """Getter for `id`

        Returns:
            __id (int): unique identifer for each instance of cls

        """
        return self.__id

    @id.setter
    def id(self, value):
        """Args:
        value (int): The number to be assigned as the unique identifier (`id`).

    Attributes:
        __id (int): Unique identifier for each instance of the class.

    Raises:
        ValueError: If the `id` argument is 0, negative, or already assigned.

        """
        if value < 1:
            raise ValueError('id should be positive')
        self.__id = value

    @property
    def serial(self):
        """Getter for `serial`

        Returns:
            __serial (int): unique identifer for each instance of cls, taken
                from __true_nb_objects at time of instantiation

        """
        return self.__serial

    @serial.setter
    def serial(self, value):
        """Args:
            value int number to be  `serial`

        Attributes:
            __serial (int): unique identifer for instance of class,
                from __true_nb_objects at time
        """
        self.__serial = value

    @staticmethod
    def to_json_string(list_dictionaries):
        """Converts a list of dictionaries to a JSON string.

    Args:
        list_dictionaries (list of dict): The list to be converted.

    Returns:
        str: JSON string representation of `list_dictionaries`, or '[]' if None or empty.



        """
        if list_dictionaries is None or list_dictionaries == []:
            return '[]'
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Saves to a file a JSON formatted string of a list of dictionary representations of objects
    of `Base` derived classes, specifically `Rectangle` and `Square`.

    Args:
        list_objs (list of dict): List of `Base` derived objects (in this project `Rectangle` and `Square`).



        """
        if list_objs is None:
            list_objs = []

        list_dicts = []
        for item in list_objs:
            list_dicts.append(item.to_dictionary())
        json_dict = cls.to_json_string(list_dicts)

        filename = cls.__name__ + '.json'
        with open(filename, 'w', encoding='utf-8') as file:
            file.write(json_dict)

    @staticmethod
    def from_json_string(json_string):
        """Returns a list of objects represented by a JSON format string, or [] if `json_string` is None or empty.

    Args:
        json_string (str): JSON format string to be converted.

    Returns:
        list: List of objects represented by the JSON format string, or [] if `json_string` is None or empty.



        """
        if json_string is None or json_string == '':
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Creates a new dummy instance of the class and updates it using `dictionary` as keyword arguments.

    Args:
        dictionary (dict): Dictionary to be used as keyword arguments.


        """
        if cls.__name__ is 'Rectangle':
            temp = cls(1, 1)
        elif cls.__name__ is 'Square':
            temp = cls(1)
        temp.update(**dictionary)
        return temp

    @classmethod
    def load_from_file(cls):
        """Returns a list of instances from the file <class name>.json, or an empty list if the file does not exist.
    The class of instances is determined by `cls`.

    Returns:
        list: List of instances of `cls` from the file <class name>.json, or an empty list if no file.

        """
        import os.path

        filename = cls.__name__ + '.json'
        if os.path.exists(filename):
            with open(filename, 'r', encoding='utf-8') as file:
                json_str = file.read()
        else:
            return []
        obj_list = cls.from_json_string(json_str)
        instance_list = []
        for item in obj_list:
            instance_list.append(cls.create(**item))
        return instance_list

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """ Saves to a file a CSV formatted string of a list of dictionary representations of objects
    of `Base` derived classes, specifically `Rectangle` and `Square`.

    Args:
        list_objs (list of dict): List of `Base` derived objects (in this project `Rectangle` and `Square`).

        """
        if list_objs is None:
            list_objs = []

        if cls.__name__ == 'Rectangle':
            keys = ('id', 'width', 'height', 'x', 'y')
        elif cls.__name__ == 'Square':
            keys = ('id', 'size', 'x', 'y')

        list_dicts = []
        for item in list_objs:
            list_dicts.append(item.to_dictionary())

        filename = cls.__name__ + '.csv'
        with open(filename, 'w', encoding='utf-8') as file:
            csv_writer = csv.DictWriter(file, keys)
            csv_writer.writeheader()
            for dict in list_dicts:
                csv_writer.writerow(dict)

    @classmethod
    def load_from_file_csv(cls):
        """ Returns a list of instances from the file <class name>.csv, or an empty list if the file does not exist.
    The class of instances is determined by `cls`.

    Returns:
        list: List of instances of `cls` from the file <class name>.csv, or an empty list if no file.



        """
        import os.path

        if cls.__name__ == 'Rectangle':
            keys = ('id', 'width', 'height', 'x', 'y')
        elif cls.__name__ == 'Square':
            keys = ('id', 'size', 'x', 'y')

        filename = cls.__name__ + '.csv'
        if os.path.exists(filename):
            with open(filename, 'r', encoding='utf-8') as file:
                csv_reader = csv.DictReader(file)
                instance_list = []
                for row in csv_reader:
                    for key in keys:
                        row[key] = int(row[key])
                    instance_list.append(cls.create(**row))
                return instance_list
        else:
            return []
