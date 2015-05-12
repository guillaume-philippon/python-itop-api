# -*- coding: utf8 -*-fr
# pylint: disable=too-many-instance-attributes,invalid-name, too-many-statements
"""
ItopapiWebApplication is a abstraction of Rack representation on iTop
"""

from itopapi.model.prototype import ItopapiPrototype, ItopapiUnimplementedMethod
from itopapi.model.rack import ItopapiRack

__version__ = '1.0'
__authors__ = ['Guillaume Philippon <guillaume.philippon@lal.in2p3.fr>']


class ItopapiWebApplication(ItopapiPrototype):
    """
    ItopapiWebApplication is a object that represent a WebApplication from iTop
    """

    # Configuration specific to itop
    itop = {
        # Name of the class in Itop
        'name': 'WebApplication',
        # Define which fields to save when creating or updating from the python API
        'save': ['name', 'url', 'business_criticity',
                 'move2production', 'description'],
        'foreign_keys': [
            {'id': 'org_id', 'name': 'organization_name', 'table': 'Organization'},
            {'id': 'webserver_id', 'name': 'webserver_name', 'table': 'WebServer'},
        ],
        'list_types': {'services_list': 'Service'}
    }

    @staticmethod
    def find(key):
        """ Retrieve one or mor instance of WebApplication with the given key or criteria """
        return ItopapiPrototype.find(ItopapiWebApplication, key)

    @staticmethod
    def find_by_name(name):
        return ItopapiPrototype.find_by_name(ItopapiWebApplication, name)

    @staticmethod
    def find_all():
        """ Retrieve all instance of WebApplication """
        return ItopapiPrototype.find_all(ItopapiWebApplication)

    def __init__(self, data=None):
        super(ItopapiWebApplication, self).__init__(data)

        ##################################
        # Properties/General Information #
        ##################################
        # WebApplication's organization id. Call findOrganization to get the full information or just
        #  use org_id_friendlyname and organization_name
        self.org_id = None
        # WebApplication's organization friendly name. Not sure the difference with organization_name
        self.org_id_friendlyname = None
        # WebApplication's organization name
        self.organization_name = None
        # WebServer hosting the application
        self.webserver_id = None
        self.webserver_id_friendlyname = None
        self.webserver_name = None
        # WebApplication's URL
        self.url = None
        # WebApplication's business criticity. Values within [high, medium, low]
        self.business_criticity = None
        # WebApplication's move to production date
        self.move2production = None
        # WebApplication's description, as a free text
        self.description = None

        ##################################
        #            Contacts            #
        ##################################
        # WebApplication's contacts list
        self.contacts_list = {}

        ##################################
        #           Documents            #
        ##################################
        # WebApplication's documents list
        self.documents_list = {}

        ##################################
        #            Tickets             #
        ##################################
        # WebApplication's tickets list
        self.tickets_list = {}

        ##################################
        #     Application solutions      #
        ##################################
        # WebApplication's application solutions list
        self.applicationsolution_list = {}

        ##################################
        #       Provider contracts       #
        ##################################
        # WebApplication's provider contracts list
        self.providercontracts_list = {}

        ##################################
        #            Services            #
        ##################################
        # WebApplication's services list
        self.services_list = {}

    def load_from_json_quattor(self, json_quattor):
        """
        Create a ItopapiWebApplication description based on quattor s JSON output
        :param json_quattor: json
        """
        pass

    def find_organization(self):
        """
        Retrieve the ItopapiOrganization related to this instance
        """
        if self.org_id is not None:
            ItopapiPrototype.get_itop_class('Organization').find(self.org_id)
        return None

    def find_web_server(self):
        """
        Retrieve the ItopapiWebServer corresponding to this WebApplication
        """
        if self.webserver_id is not None:
            ItopapiPrototype.get_itop_class('WebServer').find(self.webserver_id)
        return None
