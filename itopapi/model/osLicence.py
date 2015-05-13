# -*- coding: utf8 -*-fr

"""
ItopapiOSLicence is a abstraction of Rack representation on iTop
"""

from itopapi.model.prototype import ItopapiPrototype

__version__ = '1.0'
__authors__ = ['Julien Nauroy <julien.nauroy@u-psud.fr>']


class ItopapiOSLicence(ItopapiPrototype):

    # Configuration specific to itop
    itop = {
        # Name of the class in Itop
        'name': 'OSLicence',
        # Define which fields to save when creating or updating from the python API
        'save': ['name', 'usage_limit', 'description', 'perpetual', 'start_date', 'end_date', 'licence_key'],
        'foreign_keys': [
            {'id': 'osversion_id', 'name': 'osversion_name', 'table': 'OSVersion'},
            {'id': 'org_id', 'name': 'organization_name', 'table': 'Organization'},
        ]
    }

    @staticmethod
    def find(key):
        """ Retrieve one or more instance of OSLicence with the given key or criteria """
        return ItopapiPrototype.find(ItopapiOSLicence, key)

    @staticmethod
    def find_by_name(name):
        return ItopapiPrototype.find_by_name(ItopapiOSLicence, name)

    @staticmethod
    def find_all():
        """ Retrieve all instance of OSLicence """
        return ItopapiPrototype.find_all(ItopapiOSLicence)

    """
    ItopapiOSLicence is an object that represents an OSLicence from iTop
    """
    def __init__(self, data=None):
        super(ItopapiOSLicence, self).__init__(data)
        self.osversion_id = None
        self.osversion_id_friendlyname = None
        self.osversion_name = None
        # OSLicence's organization id. Call find_organization to get the full information or just
        #  use org_id_friendlyname and organization_name
        self.org_id = None
        # OSLicence's organization friendly name. Not sure the difference with organization_name
        self.org_id_friendlyname = None
        # OSLicence's organization name
        self.organization_name = None
        # Number of concurrent users or licences
        self.usage_limit = None
        self.description = None
        # Possible values are ['yes', 'no']
        self.perpetual = 'no'
        self.start_date = None
        self.end_date = None
        self.licence_key = None
        # Lists
        self.documents_list = []
        self.servers_list = []
        self.virtualmachines_list = []

    def find_os_version(self):
        """
        Retrieve the ItopapiOSVersion corresponding to this server
        """
        if self.osversion_id is not None:
            ItopapiPrototype.get_itop_class('OSVersion').find(self.osfamily_id)
        return None

    def find_organization(self):
        """
        Retrieve the ItopapiOrganization corresponding to this server
        """
        if self.org_id is not None:
            ItopapiPrototype.get_itop_class('Organization').find(self.org_id)
        return None
