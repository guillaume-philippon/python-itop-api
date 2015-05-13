# -*- coding: utf8 -*-fr

"""
ItopapiOSFamily is a abstraction of Rack representation on iTop
"""

from itopapi.model.prototype import ItopapiPrototype

__version__ = '1.0'
__authors__ = ['Julien Nauroy <julien.nauroy@u-psud.fr>']


class ItopapiOSFamily(ItopapiPrototype):

    # Configuration specific to itop
    itop = {
        # Name of the class in Itop
        'name': 'OSFamily',
        # Define which fields to save when creating or updating from the python API
        'save': ['name'],
        'foreign_keys': []
    }

    @staticmethod
    def find(key):
        """ Retrieve one or more instance of OSFamily with the given key or criteria """
        return ItopapiPrototype.find(ItopapiOSFamily, key)

    @staticmethod
    def find_by_name(name):
        return ItopapiPrototype.find_by_name(ItopapiOSFamily, name)

    @staticmethod
    def find_all():
        """ Retrieve all instance of OSFamily """
        return ItopapiPrototype.find_all(ItopapiOSFamily)

    """
    ItopapiOSFamily is an object that represents an OS Family from iTop
    """
    def __init__(self, data=None):
        super(ItopapiOSFamily, self).__init__(data)
