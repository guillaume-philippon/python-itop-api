# -*- coding: utf8 -*-fr
# pylint: disable=too-many-instance-attributes,invalid-name, too-many-statements
"""
ItopapiServers is a abstraction of Rack representation on iTop
"""

from itopapi.model.prototype import ItopapiPrototype, ItopapiUnimplementedMethod
from itopapi.model.rack import ItopapiRack

__version__ = '1.0'
__authors__ = ['Guillaume Philippon <guillaume.philippon@lal.in2p3.fr>']


class ItopapiServer(ItopapiPrototype):
    """
    ItopapiServers is a object that represent a Servers from iTop
    """

    # Configuration specific to itop
    itop = {
        # Name of the class in Itop
        'name': 'Server',
        # Define which fields to save when creating or updating from the python API
        'save': ['name', 'friendlyname', 'status', 'business_criticity',
                 'rack_id', 'enclosure_id', 'brand_id', 'model_id', 'managementip',
                 'oslicence_id', 'cpu', 'ram', 'nb_u', 'serialnumber', 'asset_number', 'move2production',
                 'purchase_date', 'end_of_warranty', 'description'],
        'foreign_keys': [
            {'id': 'org_id', 'name': 'organization_name', 'table': 'Organization'},
            {'id': 'location_id', 'name': 'location_name', 'table': 'Localization'},
            {'id': 'osfamily_id', 'name': 'osfamily_name', 'table': 'OSFamily'},
            {'id': 'osversion_id', 'name': 'osversion_name', 'table': 'OSVersion'},
            {'id': 'oslicence_id', 'name': 'oslicence_name', 'table': 'OSLicence'},
            # TODO which is the relevant table?
            {'id': 'powerA_id', 'name': 'powerA_name', 'table': 'TODO'},
            {'id': 'powerB_id', 'name': 'powerB_name', 'table': 'TODO'},
        ]
    }

    @staticmethod
    def find(key):
        """ Retrieve one or mor instance of Server with the given key or criteria """
        return ItopapiPrototype.find(ItopapiServer, key)

    @staticmethod
    def find_by_name(name):
        return ItopapiPrototype.find_by_name(ItopapiServer, name)

    @staticmethod
    def find_all():
        """ Retrieve all instance of Server """
        return ItopapiPrototype.find_all(ItopapiServer)

    def __init__(self, data=None):
        super(ItopapiServer, self).__init__(data)

        ##################################
        # Properties/General Information #
        ##################################
        # Server's organization id. Call findOrganization to get the full information or just
        #  use org_id_friendlyname and organization_name
        self.org_id = None
        # Server's organization friendly name. Not sure the difference with organization_name
        self.org_id_friendlyname = None
        # Server's organization name
        self.organization_name = None
        # Server's status. Values within [implementation, obsolete, production, stock]
        self.status = None
        # Server's business criticity. Values within [high, medium, low]
        self.business_criticity = None
        # Server's location id. Call findLocation to get the full information or just use
        # location_id_friendlyname and location_name
        self.location_id = None
        # Server's location id's friendly name. Not sure the difference with location_name
        self.location_id_friendlyname = None
        # Server's location name
        self.location_name = None
        # Server's rack id. Call findRack to get the full information or just use rack_id
        # friendlyname and rack_name
        self.rack_id = None
        # Server's rack id's friendly name. Not sure the difference with rack_name
        self.rack_id_friendlyname = None
        # Server's rack name"""
        self.rack_name = None
        # Server's enclosure (chassis) id. Call findEnclosure to get the full information or just
        # use enclosure_id_friendlyname and enclosure_name
        self.enclosure_id = None
        # Server's enclosure id's friendly name. Not sure the difference with enclosure_name
        self.enclosure_id_friendlyname = None
        # Server's enclosure name
        self.enclosure_name = None

        ##################################
        #  Properties/More Information   #
        ##################################
        self.brand_id = None
        self.brand_id_friendlyname = None
        self.brand_name = None

        self.model_id = None
        self.model_id_friendlyname = None
        self.model_name = None

        self.osfamily_id = None
        self.osfamily_id_friendlyname = None
        self.osfamily_name = None

        self.osversion_id = None
        self.osversion_id_friendlyname = None
        self.osversion_name = None

        self.managementip = None

        self.oslicence_id = None
        self.oslicence_id_friendlyname = None
        self.oslicence_name = None

        self.cpu = None
        self.ram = None
        # Rack units
        self.nb_u = None
        self.serialnumber = None
        # Server's asset number
        self.asset_number = None

        ##################################
        #        Properties/Date         #
        ##################################
        self.move2production = None
        # Server's move to production date
        self.purchase_date = None
        # Server's purchase date
        self.end_of_warranty = None
        # Server's end of warranty date

        ##################################
        #  Properties/Other Information  #
        ##################################
        self.powerA_id = None
        self.powerA_id_finalclass_recall = None
        self.powerA_id_friendlyname = None
        self.powerA_name = None
        self.powerB_id = None
        self.powerB_id_finalclass_recall = None
        self.powerB_id_friendlyname = None
        self.powerB_name = None
        self.description = None
        # Server's description, as a free text

        ##################################
        #           Softwares            #
        ##################################
        # Server's softwares list
        self.softwares_list = {}

        ##################################
        #            Contacts            #
        ##################################
        # Server's contacts list
        self.contacts_list = {}

        ##################################
        #           Documents            #
        ##################################
        # Server's documents list
        self.documents_list = {}

        ##################################
        #            Tickets             #
        ##################################
        # Server's tickets list
        self.tickets_list = {}

        ##################################
        #     Application solutions      #
        ##################################
        # Server's application solutions list
        self.applicationsolution_list = {}

        ##################################
        #       Network interfaces       #
        ##################################
        # Server's network interfaces list
        self.physicalinterface_list = {}

        ##################################
        #            FC ports            #
        ##################################
        # Server's FC ports list
        self.fiberinterfacelist_list = {}

        ##################################
        #        Network devices         #
        ##################################
        # Server's network devices list
        self.networkdevice_list = {}

        ##################################
        #              SANs              #
        ##################################
        # Server's SANs list
        self.san_list = {}

        ##################################
        #        Logical volumes         #
        ##################################
        # Server's logical volumes list
        self.logicalvolumes_list = {}

        ##################################
        #       Provider contracts       #
        ##################################
        # Server's provider contracts list
        self.providercontracts_list = {}

        ##################################
        #            Services            #
        ##################################
        # Server's services list
        self.services_list = {}

    def load_from_json_quattor(self, json_quattor):
        """
        Create a ItopapiServer description based on quattor s JSON output
        :param json_quattor: json
        """
        pass

    def find_rack(self):
        """
        Retrieve the ItopapiRack corresponding to this server
        """
        if self.rack_id is not None:
            return ItopapiRack.find(self.rack_id)
        return None

    def find_organization(self):
        """
        Retrieve the ItopapiOrganization corresponding to this server
        """
        if self.org_id is not None:
            # TODO define ItopapiOrganization return ItopapiOrganization.find(self.org_id)
            raise ItopapiUnimplementedMethod()
        return None

    def find_location(self):
        """
        Retrieve the ItopapiLocation corresponding to this server
        """
        if self.location_id is not None:
            # TODO define ItopapiLocation return ItopapiLocation.find(self.location_id)
            raise ItopapiUnimplementedMethod()
        return None

    def find_enclosure(self):
        """
        Retrieve the ItopapiEnclosure corresponding to this server
        """
        if self.enclosure_id is not None:
            # TODO define ItopapiEnclosure return ItopapiEnclosure.find(self.enclosure_id)
            raise ItopapiUnimplementedMethod()
        return None

    def find_brand(self):
        """
        Retrieve the ItopapiBrand corresponding to this server
        """
        if self.brand_id is not None:
            # TODO define ItopapiBrand return ItopapiBrand.find(self.brand_id)
            raise ItopapiUnimplementedMethod()
        return None

    def find_model(self):
        """
        Retrieve the ItopapiModel corresponding to this server
        """
        if self.model_id is not None:
            # TODO define ItopapiModel return ItopapiModel.find(self.model_id)
            raise ItopapiUnimplementedMethod()
        return None

    def find_os_family(self):
        """
        Retrieve the ItopapiOSFamily corresponding to this server
        """
        if self.osfamily_id is not None:
            # TODO define ItopapiOSFamily return ItopapiOSFamily.find(self.osfamily_id)
            raise ItopapiUnimplementedMethod()
        return None

    def find_os_version(self):
        """
        Retrieve the ItopapiOSVersion corresponding to this server
        """
        if self.osversion_id is not None:
            # TODO define ItopapiOSVersion return ItopapiOSVersion.find(self.osversion_id)
            raise ItopapiUnimplementedMethod()
        return None

    def find_os_licence(self):
        """
        Retrieve the ItopapiOSLicence corresponding to this server
        """
        if self.oslicence_id is not None:
            # TODO define ItopapiOSLicence return ItopapiOSLicence.find(self.oslicence_id)
            raise ItopapiUnimplementedMethod()
        return None

    def find_power_a(self):
        """
        Retrieve the ItopapiPowerA corresponding to this server
        """
        if self.powerA_id is not None:
            # TODO define ItopapiPowerA return ItopapiOPowerA.find(self.powerA_id)
            raise ItopapiUnimplementedMethod()
        return None

    def find_power_b(self):
        """
        Retrieve the ItopapiPowerB corresponding to this server
        """
        if self.powerB_id is not None:
            # TODO define ItopapiPowerB return ItopapiOPowerB.find(self.powerB_id)
            raise ItopapiUnimplementedMethod()
        return None
