# -*- coding: utf8 -*-fr

"""
ItopapiOSVersion is a abstraction of Rack representation on iTop
"""

from itopapi.model.prototype import ItopapiPrototype

__version__ = '1.0'
__authors__ = ['Julien Nauroy <julien.nauroy@u-psud.fr>']


class ItopapiOSVersion(ItopapiPrototype):

    # Configuration specific to itop
    itop = {
        # Name of the class in Itop
        'name': 'OSVersion',
        # Define which fields to save when creating or updating from the python API
        'save': ['name'],
        'foreign_keys': [
            {'id': 'osfamily_id', 'name': 'osfamily_name', 'table': 'OSFamily'},
        ]
    }

    @staticmethod
    def find(key):
        """ Retrieve one or more instance of OSVersion with the given key or criteria """
        return ItopapiPrototype.find(ItopapiOSVersion, key)

    @staticmethod
    def find_by_name(name):
        return ItopapiPrototype.find_by_name(ItopapiOSVersion, name)

    @staticmethod
    def find_all():
        """ Retrieve all instance of OSVersion """
        return ItopapiPrototype.find_all(ItopapiOSVersion)

    """
    ItopapiOSVersion is an object that represents an OS Version from iTop
    """
    def __init__(self, data=None):
        super(ItopapiOSVersion, self).__init__(data)
        # OSFamily this OSVersion is attached to
        self.osfamily_id = None
        self.osfamily_id_friendlyname = None
        self.osfamily_name = None

    def find_os_family(self):
        """
        Retrieve the ItopapiOSFamily corresponding to this server
        """
        if self.osfamily_id is not None:
            ItopapiPrototype.get_itop_class('OSFamily').find(self.osfamily_id)
        return None
