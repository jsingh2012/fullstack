import connexion
import six

from swagger_server.models.cat import Cat  # noqa: E501
from swagger_server.models.cats_response import CatsResponse  # noqa: E501
from swagger_server import util


def add_cat(body):  # noqa: E501
    """Add a new cat to the store

    Creates a new cat in the store # noqa: E501

    :param body: Cat object that needs to be added to the store
    :type body: dict | bytes

    :rtype: Cat
    """
    if connexion.request.is_json:
        body = Cat.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def delete_cat(cat_id):  # noqa: E501
    """Delete a cat

    Delete a cat # noqa: E501

    :param cat_id: Id of the cat desired to be deleted
    :type cat_id: str

    :rtype: None
    """
    return 'do some magic!'


def get_cat(cat_id):  # noqa: E501
    """Retrieve a single cat

    Retrieve a single cat # noqa: E501

    :param cat_id: Id of the cat desired to be retrieved
    :type cat_id: str

    :rtype: Cat
    """
    return 'do some magic!'


def list_cats():  # noqa: E501
    """Retrieves the list of all cats

    Retrieves the list of all cats # noqa: E501


    :rtype: CatsResponse
    """
    return 'do some magic!'


def update_cat(cat_id, body):  # noqa: E501
    """Update an existing cat

     # noqa: E501

    :param cat_id: Id of the cat desired to be updated
    :type cat_id: str
    :param body: Cat object that needs to be added to the store
    :type body: dict | bytes

    :rtype: Cat
    """
    if connexion.request.is_json:
        body = Cat.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
