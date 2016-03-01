# -*- coding: utf8 -*-fr

"""
ItopapiPhysicalInterface is a abstraction of PhysicalInterface representation on iTop
"""

from itopapi.model.prototype import ItopapiPrototype

__version__ = '1.0'
__authors__ = ['Julien Nauroy <julien.nauroy@u-psud.fr>']


class ItopapiPhysicalInterface(ItopapiPrototype):

    # Configuration specific to itop
    itop = {
        # Name of the class in Itop
        'name': 'PhysicalInterface',
        # Define which fields to save when creating or updating from the python API
        'save': ['name', 'ipaddress', 'macaddress', 'comment', 'ipgateway', 'ipmask', 'speed'],
        'foreign_keys': [
            # TODO the table is not necessarily a server, it is defined by connectableci_id_finalclass_recall
            {'id': 'connectableci_id', 'name': 'connectableci_name', 'table': 'Server'},
            # TODO good for fetching, but not for saving since there is no "name" and "finalclass" in this list!
            # Find a solution
            # {'id': 'vlan_id', 'name': 'vlan_tag', 'table': 'VLAN'},
        ],
        'list_types': {'vlans_list': 'VLAN'},
    }

    @staticmethod
    def find(key):
        """ Retrieve one or more instance of PhysicalInterface with the given key or criteria """
        return ItopapiPrototype.find(ItopapiPhysicalInterface, key)

    @staticmethod
    def find_by_name(name):
        return ItopapiPrototype.find_by_name(ItopapiPhysicalInterface, name)

    @staticmethod
    def find_all():
        """ Retrieve all instance of PhysicalInterface """
        return ItopapiPrototype.find_all(ItopapiPhysicalInterface)

    """
    ItopapiPhysicalInterface is an object that represents a PhysicalInterface from iTop
    """
    def __init__(self, data=None):
        super(ItopapiPhysicalInterface, self).__init__(data)
        # CI the Physical Interface is connected to
        self.connectableci_name = None
        self.connectableci_id = None
        self.connectableci_id_friendlyname = None
        self.connectableci_id_finalclass_recall = None
        # IP address of the PhysicalInterface
        self.ipaddress = None
        # MAC address of the PhysicalInterface
        self.macaddress = None
        # Any kind of comment
        self.comment = None
        # IP gateway of the PhysicalInterface
        self.ipgateway = None
        # IP mask of the PhysicalInterface
        self.ipmask = None
        # speed of the PhysicalInterface
        self.speed = None
        # List of vlans for the PhysicalInterface
        self.vlans_list = None