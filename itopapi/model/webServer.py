# -*- coding: utf8 -*-fr
# pylint: disable=too-many-instance-attributes,invalid-name, too-many-statements
"""
ItopapiWebServer is a abstraction of Rack representation on iTop
"""

from itopapi.model.prototype import ItopapiPrototype, ItopapiUnimplementedMethod
from itopapi.model.rack import ItopapiRack

__version__ = '1.0'
__authors__ = ['Guillaume Philippon <guillaume.philippon@lal.in2p3.fr>']


class ItopapiWebServer(ItopapiPrototype):
    """
    ItopapiWebServer is a object that represent a WebServer from iTop
    """

    # Configuration specific to itop
    itop = {
        # Name of the class in Itop
        'name': 'WebServer',
        # Define which fields to save when creating or updating from the python API
        'save': ['name', 'status', 'business_criticity', 'path', 'move2production', 'description'],
        'foreign_keys': [
            {'id': 'org_id', 'name': 'organization_name', 'table': 'Organization'},
            {'id': 'system_id', 'name': 'system_id_friendlyname', 'table': 'Server'},
            {'id': 'software_id', 'name': 'software_name', 'table': 'Software'},
            {'id': 'softwarelicence_id', 'name': 'softwarelicence_name', 'table': 'SoftwareLicence'},
        ]
    }

    @staticmethod
    def find(key):
        """ Retrieve one or mor instance of WebServer with the given key or criteria """
        return ItopapiPrototype.find(ItopapiWebServer, key)

    @staticmethod
    def find_by_name(name):
        return ItopapiPrototype.find_by_name(ItopapiWebServer, name)

    @staticmethod
    def find_all():
        """ Retrieve all instance of WebServer """
        return ItopapiPrototype.find_all(ItopapiWebServer)

    def __init__(self, data=None):
        super(ItopapiWebServer, self).__init__(data)

        ##################################
        # Properties/General Information #
        ##################################
        # WebServer's organization id. Call findOrganization to get the full information or just
        #  use org_id_friendlyname and organization_name
        self.org_id = None
        # WebServer's organization friendly name. Not sure the difference with organization_name
        self.org_id_friendlyname = None
        # WebServer's organization name
        self.organization_name = None
        # WebServer's status. Values within [implementation, obsolete, production, stock]
        self.status = None
        # WebServer's business criticity. Values within [high, medium, low]
        self.business_criticity = None
        # System containing the WebServer
        self.system_id = None
        self.system_id_finalclass_recall = None
        self.system_id_friendlyname = None
        self.system_name = None
        # Web server's software
        self.software_id = None
        self.software_id_friendlyname = None
        self.software_name = None
        # Web server's software licence
        self.softwarelicence_id = None
        self.softwarelicence_id_friendlyname = None
        self.softwarelicence_name = None
        # Web server's path ?
        self.path = None
        # WebServer's move to production date
        self.move2production = None
        # WebServer's description, as a free text
        self.description = None

        ##################################
        #            Contacts            #
        ##################################
        # WebServer's contacts list
        self.contacts_list = {}

        ##################################
        #           Documents            #
        ##################################
        # WebServer's documents list
        self.documents_list = {}

        ##################################
        #            Tickets             #
        ##################################
        # WebServer's tickets list
        self.tickets_list = {}

        ##################################
        #     Application solutions      #
        ##################################
        # WebServer's application solutions list
        self.applicationsolution_list = {}

        ##################################
        #        Web applications        #
        ##################################
        # WebServer's web applications list
        self.webapp_list = {}

        ##################################
        #       Network interfaces       #
        ##################################
        # WebServer's network interfaces list
        self.physicalinterface_list = {}

        ##################################
        #            FC ports            #
        ##################################
        # WebServer's FC ports list
        self.fiberinterfacelist_list = {}

        ##################################
        #        Network devices         #
        ##################################
        # WebServer's network devices list
        self.networkdevice_list = {}

        ##################################
        #              SANs              #
        ##################################
        # WebServer's SANs list
        self.san_list = {}

        ##################################
        #        Logical volumes         #
        ##################################
        # WebServer's logical volumes list
        self.logicalvolumes_list = {}

        ##################################
        #       Provider contracts       #
        ##################################
        # WebServer's provider contracts list
        self.providercontracts_list = {}

        ##################################
        #            Services            #
        ##################################
        # WebServer's services list
        self.services_list = {}

    def load_from_json_quattor(self, json_quattor):
        """
        Create a ItopapiWebServer description based on quattor s JSON output
        :param json_quattor: json
        """
        pass

    def find_organization(self):
        """
        Retrieve the ItopapiOrganization corresponding to this WebServer
        """
        if self.org_id is not None:
            # TODO define ItopapiOrganization return ItopapiOrganization.find(self.org_id)
            raise ItopapiUnimplementedMethod()
        return None

    def find_system(self):
        """
        Retrieve the ItopapiPowerB corresponding to this WebServer
        """
        if self.system_id is not None:
            # TODO
            raise ItopapiUnimplementedMethod()
        return None

    def find_software(self):
        """
        Retrieve the ItopapiPowerB corresponding to this WebServer
        """
        if self.software_id is not None:
            # TODO
            raise ItopapiUnimplementedMethod()
        return None

    def find_software_licence(self):
        """
        Retrieve the ItopapiPowerB corresponding to this WebServer
        """
        if self.software_licence_id is not None:
            # TODO
            raise ItopapiUnimplementedMethod()
        return None
