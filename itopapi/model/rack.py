# -*- coding: utf8 -*-fr
# pylint: disable=too-many-instance-attributes, invalid-name
"""
ItopapiRack is a abstraction of Rack representation on iTop
"""

from itopapi.model.prototype import ItopapiPrototype

__version__ = '1.0'
__authors__ = ['Guillaume Philippon <guillaume.philippon@lal.in2p3.fr>']


class ItopapiRack(ItopapiPrototype):
    """
    ItopapiRack is a object that represents a Rack from iTop
    """

    """ Configuration specific to itop """
    itop = {
        # Name of the class in Itop
        'name': 'Rack',
        # Define which fields to save when creating or updating from the python API
        'save': ['name', 'status', 'business_criticity', 'nb_u',
                 'serialnumber', 'asset_number', 'move2production', 'purchase_date', 'end_of_warranty', 'description'],
        'foreign_keys': [
            {'id': 'org_id', 'name': 'organization_name', 'table': 'Organization'},
            {'id': 'location_id', 'name': 'location_name', 'table': 'Localization'},
        ]
    }

    @staticmethod
    def find(key):
        """ Retrieve one or more instance of Rack with the given key or criteria """
        return ItopapiPrototype.find(ItopapiRack, key)

    @staticmethod
    def find_by_name(name):
        return ItopapiPrototype.find_by_name(ItopapiRack, name)

    @staticmethod
    def find_all():
        """ Retrieve all instance of Rack """
        return ItopapiPrototype.find_all(ItopapiRack)

    def __init__(self, data=None):
        super(ItopapiRack, self).__init__(data)

        ##################################
        #           Properties           #
        ##################################
        # Rack's organization id. Call find_organization to get the full information or just use
        # org_id_friendlyname and organization_name
        self.org_id = None
        # Rack's organization friendly name. Not sure the difference with organization_name
        self.org_id_friendlyname = None
        # Rack's organization name
        self.organization_name = None
        # Rack's status. Values within [implementation, obsolete, production, stock]
        self.status = None
        # Rack's business criticity. Values within [high, medium, low]
        self.business_criticity = None
        # Rack's location id. Call find_location to get the full information or just use location_id
        # _friendlyname and location_name
        self.location_id = None
        # Rack's location id's friendly name. Not sure the difference with location_name
        self.location_id_friendlyname = None
        # Rack's location name
        self.location_name = None
        # Rack's height in "rack units"
        self.nb_u = None
        # Rack's serial number
        self.serialnumber = None
        # Rack's asset number
        self.asset_number = None
        # Rack's move to production date
        self.move2production = None
        # Rack's purchase date
        self.purchase_date = None
        # Rack's end of warranty date
        self.end_of_warranty = None
        # Rack's description, as a free text
        self.description = None

        ##################################
        #            Contacts            #
        ##################################
        # Rack's contacts list
        self.contacts_list = {}

        ##################################
        #            Documents           #
        ##################################
        # Rack's documents list
        self.documents_list = {}

        ##################################
        #             Tickets            #
        ##################################
        # Rack's tickets list
        self.tickets_list = {}

        ##################################
        #           Enclosures           #
        ##################################
        # Rack's enclosures list
        self.enclosure_list = {}

        ##################################
        #            Devices             #
        ##################################
        # Rack's devices list
        self.device_list = {}

        ##################################
        #       Provider contracts       #
        ##################################
        # Rack's provider contracts list
        self.providercontracts_list = {}

        ##################################
        #            Services            #
        ##################################
        # Rack's services list
        self.services_list = {}

        # Other lists
        self.applicationsolution_list = None
        self.softwares_list = None
        self.logicalvolumes_list = None

    def find_organization(self):
        """
        Retrieve the ItopapiOrganization related to this instance
        """
        if self.org_id is not None:
            ItopapiPrototype.get_itop_class('Organization').find(self.org_id)
        return None

    def find_location(self):
        """
        Retrieve the ItopapiLocation related to this instance
        """
        if self.location_id is not None:
            ItopapiPrototype.get_itop_class('Location').find(self.location_id)
        return None
