# -*- coding: utf8 -*-fr

"""
ItopapiService is a abstraction of Service representation on iTop
"""

from itopapi.model.prototype import ItopapiPrototype

__version__ = '1.0'
__authors__ = ['Julien Nauroy <julien.nauroy@u-psud.fr>']


class ItopapiService(ItopapiPrototype):

    # Configuration specific to itop
    itop = {
        # Name of the class in Itop
        'name': 'Service',
        # Define which fields to save when creating or updating from the python API
        'save': ['name', 'description', 'status'],
        'foreign_keys': [
            {'id': 'servicefamily_id', 'name': 'servicefamily_name', 'table': 'ServiceFamily'},
            {'id': 'org_id', 'name': 'organization_name', 'table': 'Organization'},
        ],
        'list_types': {'functionalcis_list': None},
    }

    @staticmethod
    def find(key):
        """ Retrieve one or more instance of PhysicalInterface with the given key or criteria """
        return ItopapiPrototype.find(ItopapiService, key)

    @staticmethod
    def find_by_name(name):
        return ItopapiPrototype.find_by_name(ItopapiService, name)

    @staticmethod
    def find_all():
        """ Retrieve all instance of PhysicalInterface """
        return ItopapiPrototype.find_all(ItopapiService)

    """
    ItopapiService is an object that represents a Service from iTop
    """
    def __init__(self, data=None):
        super(ItopapiService, self).__init__(data)
        # Note: the Organization is called "Provider" for Services
        self.org_id = None
        self.org_id_friendlyname = None
        self.organization_name = None
        # Service Family
        self.servicefamily_id = None
        self.servicefamily_id_friendlyname = None
        self.servicefamily_name = None
        # Description
        self.description = None
        # Service's status. Values within [implementation, obsolete, production]
        self.status = None
        # Lists
        self.servicesubcategories_list = None
        self.documents_list = None
        self.contacts_list = None
        self.customercontracts_list = None
        self.providercontracts_list = None
        self.functionalcis_list = None

    def find_organization(self):
        """
        Retrieve the ItopapiOrganization corresponding to this server
        """
        if self.org_id is not None:
            ItopapiPrototype.get_itop_class('Organization').find(self.org_id)
        return None
