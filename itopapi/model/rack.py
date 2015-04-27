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
    def find_by_name(name):
        ItopapiPrototype.find_by_name(ItopapiRack, name)

    @staticmethod
    def find_all():
        """ Retrieve all instance of Rack """
        return ItopapiPrototype.find_all(ItopapiRack)

    def __init__(self):
        super(ItopapiRack, self).__init__()

        ##################################
        #           Properties           #
        ##################################
        self.org_id = None
        """Rack's organization id. Call findOrganization to get the full information or just use org_id_friendlyname and organization_name"""
        self.org_id_friendlyname = None
        """Rack's organization id's friendly name. Not sure the difference with organization_name"""
        self.organization_name = None
        """Rack's organization name"""
        self.status = None
        """Rack's status. Values within [implementation, obsolete, production, stock]"""
        self.business_criticity = None
        """Rack's business criticity. Values within [high, medium, low]"""
        self.location_id = None
        """Rack's location id. Call findLocation to get the full information or just use location_id_friendlyname and location_name"""
        self.location_id_friendlyname = None
        """Rack's location id's friendly name. Not sure the difference with location_name"""
        self.location_name = None
        """Rack's location name"""
        self.nb_u = None
        """Rack's height in "rack units" """
        self.serialnumber = None
        """Rack's serial number"""
        self.asset_number = None
        """Rack's asset number"""
        self.move2production = None
        """Rack's move to production date"""
        self.purchase_date = None
        """Rack's purchase date"""
        self.end_of_warranty = None
        """Rack's end of warranty date"""
        self.description = None
        """Rack's description, as a free text"""

        ##################################
        #            Contacts            #
        ##################################
        self.contacts_list = {}
        """Rack's contacts list"""

        ##################################
        #            Documents           #
        ##################################
        self.documents_list = {}
        """Rack's documents list"""

        ##################################
        #             Tickets            #
        ##################################
        self.tickets_list = {}
        """Rack's tickets list"""

        ##################################
        #           Enclosures           #
        ##################################
        self.enclosure_list = {}
        """Rack's enclosures list"""

        ##################################
        #            Devices             #
        ##################################
        self.device_list = {}
        """Rack's devices list"""

        ##################################
        #       Provider contracts       #
        ##################################
        self.providercontracts_list = {}
        """Rack's provider contracts list"""

        ##################################
        #            Services            #
        ##################################
        self.services_list = {}
        """Rack's services list"""

        # TODO WTF is this doing here?!?
        self.applicationsolution_list = None
        self.softwares_list = None
        self.logicalvolumes_list = None
