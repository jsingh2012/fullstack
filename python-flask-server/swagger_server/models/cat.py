# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class Cat(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, id: str=None, name: str=None, breed: str=None):  # noqa: E501
        """Cat - a model defined in Swagger

        :param id: The id of this Cat.  # noqa: E501
        :type id: str
        :param name: The name of this Cat.  # noqa: E501
        :type name: str
        :param breed: The breed of this Cat.  # noqa: E501
        :type breed: str
        """
        self.swagger_types = {
            'id': str,
            'name': str,
            'breed': str
        }

        self.attribute_map = {
            'id': 'id',
            'name': 'name',
            'breed': 'breed'
        }

        self._id = id
        self._name = name
        self._breed = breed

    @classmethod
    def from_dict(cls, dikt) -> 'Cat':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Cat of this Cat.  # noqa: E501
        :rtype: Cat
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self) -> str:
        """Gets the id of this Cat.


        :return: The id of this Cat.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id: str):
        """Sets the id of this Cat.


        :param id: The id of this Cat.
        :type id: str
        """

        self._id = id

    @property
    def name(self) -> str:
        """Gets the name of this Cat.

        Name of the cat  # noqa: E501

        :return: The name of this Cat.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name: str):
        """Sets the name of this Cat.

        Name of the cat  # noqa: E501

        :param name: The name of this Cat.
        :type name: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def breed(self) -> str:
        """Gets the breed of this Cat.

        Breed of the cat  # noqa: E501

        :return: The breed of this Cat.
        :rtype: str
        """
        return self._breed

    @breed.setter
    def breed(self, breed: str):
        """Sets the breed of this Cat.

        Breed of the cat  # noqa: E501

        :param breed: The breed of this Cat.
        :type breed: str
        """
        allowed_values = ["Abyssinian", "Aegean", "American Bobtail", "American Curl", "American Shorthair", "American Wirehair", "Arabian Mau", "Australian Mist", "Balinese", "Bambino", "Bengal", "Birman", "Bombay", "British Longhair", "British Shorthair", "Burmese", "Burmilla", "California Spangled", "Chantilly-Tiffany", "Chartreux", "Chausie", "Cheetoh", "Colorpoint Shorthair", "Cornish Rex", "Cymric", "Cyprus", "Devon Rex", "Donskoy", "Dragon Li", "Egyptian Mau", "European Burmese", "Exotic Shorthair", "Havana Brown", "Himalayan", "Japanese Bobtail", "Javanese", "Khao Manee", "Korat", "Kurilian", "LaPerm", "Maine Coon", "Malayan", "Manx", "Munchkin", "Nebelung", "Norwegian Forest Cat", "Ocicat", "Oriental", "Persian", "Pixie-bob", "Ragamuffin", "Ragdoll", "Russian Blue", "Savannah", "Scottish Fold", "Selkirk Rex", "Siamese", "Siberian", "Singapura", "Snowshoe", "Somali", "Sphynx", "Tonkinese", "Toyger", "Turkish Angora", "Turkish Van", "York Chocolate"]  # noqa: E501
        if breed not in allowed_values:
            raise ValueError(
                "Invalid value for `breed` ({0}), must be one of {1}"
                .format(breed, allowed_values)
            )

        self._breed = breed
