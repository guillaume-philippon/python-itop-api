# -*- coding: utf8 -*-fr

"""
ItopapiVLAN is a abstraction of VLAN representation on iTop
Note : VLAN has no finalclass and name. It complicates things...
"""

from itopapi.model.prototype import ItopapiPrototype

__version__ = '1.0'
__authors__ = ['Julien Nauroy <julien.nauroy@u-psud.fr>']


class ItopapiVLAN(ItopapiPrototype):

    # Configuration specific to itop
    itop = {
        # Name of the class in Itop
        'name': 'VLAN',
        # Define which fields to save when creating or updating from the python API
        'save': ['vlan_tag', 'description'],
        'foreign_keys': [
            {'id': 'org_id', 'name': 'organization_name', 'table': 'Organization'},
        ],
        'list_types': {'physicalinterfaces_list': 'PhysicalInterface', 'subnets_list': 'Subnet'},
    }

    @staticmethod
    def find(key):
        """ Retrieve one or more instance of PhysicalInterface with the given key or criteria """
        return ItopapiPrototype.find(ItopapiVLAN, key)

    @staticmethod
    def find_by_name(name):
        return ItopapiPrototype.find_by_name(ItopapiVLAN, name)

    @staticmethod
    def find_all():
        """ Retrieve all instance of PhysicalInterface """
        return ItopapiPrototype.find_all(ItopapiVLAN)

    """
    ItopapiPhysicalInterface is an object that represent a PhysicalInterface from iTop
    """
    def __init__(self, data=None):
        super(ItopapiVLAN, self).__init__(data)
        # VLAN tag, replaces the "name" value for other classes
        self.vlan_tag = None
        # VLAN's organization id. Call findOrganization to get the full information or just use
        # org_id_friendlyname and organization_name
        self.org_id = None
        # VLAN's organization friendly name. Not sure the difference with organization_name
        self.org_id_friendlyname = None
        # VLAN's organization name
        self.org_name = None
        # VLAN's description
        self.description = None
        # Interfaces
        self.physicalinterfaces_list = None
        # subnets
        self.subnets_list = None

    def find_organization(self):
        """
        Retrieve the ItopapiOrganization related to this instance
        """
        if self.org_id is not None:
            ItopapiPrototype.get_itop_class('Organization').find(self.org_id)
        return None