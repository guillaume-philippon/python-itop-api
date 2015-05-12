# -*- coding: utf8 -*-fr

"""
ItopapiModel is a abstraction of Model representation on iTop
"""

from itopapi.model.prototype import ItopapiPrototype

__version__ = '1.0'
__authors__ = ['Julien Nauroy <julien.nauroy@u-psud.fr>']


class ItopapiModel(ItopapiPrototype):

    # Configuration specific to itop
    itop = {
        # Name of the class in Itop
        'name': 'Model',
        # Define which fields to save when creating or updating from the python API
        'save': ['name', 'type'],
        'foreign_keys': [
            {'id': 'brand_id', 'name': 'brand_name', 'table': 'Brand'},
        ]
    }

    @staticmethod
    def find(key):
        """ Retrieve one or more instance of Model with the given key or criteria """
        return ItopapiPrototype.find(ItopapiModel, key)

    @staticmethod
    def find_by_name(name):
        return ItopapiPrototype.find_by_name(ItopapiModel, name)

    @staticmethod
    def find_all():
        """ Retrieve all instance of Model """
        return ItopapiPrototype.find_all(ItopapiModel)

    """
    ItopapiModel is an object that represents a Model from iTop
    """
    def __init__(self, data=None):
        super(ItopapiModel, self).__init__(data)
        # Physical devices using this brand
        self.physicaldevices_list = None
        self.brand_id = None
        self.brand_id_friendlyname = None
        self.brand_name = None
        # Type of item the Brand refers to. Values are within
        # [DiskArray, Enclosure, IPPhone, MobilePhone, NAS, NetworkDevice, PC, PDU, Peripheral, Phone,
        # PowerSource, Printer, Rack, SANSwitch, Server, StorageSystem, Tablet, TapeLibrary]
        self.type = None

    def find_brand(self):
        """
        Retrieve the ItopapiBrand corresponding to this server
        """
        if self.brand_id is not None:
            ItopapiPrototype.get_itop_class('Brand').find(self.brand_id)
        return None