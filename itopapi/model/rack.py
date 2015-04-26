# -*- coding: utf8 -*-fr

"""
ItopapiRack is a abstraction of Rack representation on iTop
"""

from itopapi.model.prototype import ItopapiPrototype

__version__ = '1.0'
__authors__ = ['Guillaume Philippon <guillaume.philippon@lal.in2p3.fr>']


class ItopapiRack(ItopapiPrototype):
    """
    ItopapiRack is a object that represent a Rack from iTop
    """

    """ Configuration specific to itop """
    itop = {'name': 'Rack'}

    @staticmethod
    def find(key):
        """ Retrieve one or more instance of Rack with the given key or criteria """
        return ItopapiPrototype.find(ItopapiRack, key)

    @staticmethod
    def list_objects():
        """ Retrieve all instance of Rack """
        return ItopapiPrototype.list_objects(ItopapiRack)

    def __init__(self):
        """
        Add itop['name'] to use generic ItopapiPrototype method
        """
        super(ItopapiRack, self).__init__()