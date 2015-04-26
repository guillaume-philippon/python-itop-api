# -*- coding: utf8 -*-fr

"""
ItopapiServers is a abstraction of Rack representation on iTop
"""

from itopapi.model.prototype import ItopapiPrototype
from itopapi.model.rack import ItopapiRack

__version__ = '1.0'
__authors__ = ['Guillaume Philippon <guillaume.philippon@lal.in2p3.fr>']


class ItopapiServer(ItopapiPrototype):
    """
    ItopapiServers is a object that represent a Servers from iTop
    """

    """ Configuration specific to itop """
    itop = {'name': 'Server'}

    @staticmethod
    def find(key):
        """ Retrieve one or mor instance of Server with the given key or criteria """
        return ItopapiPrototype.find(ItopapiServer, key)

    @staticmethod
    def list_objects():
        """ Retrieve all instance of Server """
        return ItopapiPrototype.list_objects(ItopapiServer)

    def __init__(self):
        """
        Add itop['name'] to use generic ItopapiPrototype method
        """
        super(ItopapiServer, self).__init__()

        """##############################"""
        """Properties/General Information"""
        """Server's common name"""
        self.name = None
        """Server's common name (bis?)"""
        self.friendlyname = None
        """Server's organization id. Call findOrganization to get the full information or just use org_id_friendlyname and organization_name"""
        self.org_id = None
        """Server's organization id's friendly name. Not sure the difference with organization_name"""
        self.org_id_friendlyname = None
        """Server's organization name"""
        self.organization_name = None
        """Server's status. Values within [implementation, obsolete, production, stock]"""
        self.status = None
        """Server's business criticity. Values within [high, medium, low]"""
        self.business_criticity = None
        """Server's location id. Call findLocation to get the full information or just use location_id_friendlyname and location_name"""
        self.location_id = None
        """Server's location id's friendly name. Not sure the difference with location_name"""
        self.location_id_friendlyname = None
        """Server's location name"""
        self.location_name = None
        """Server's rack id. Call findRack to get the full information or just use rack_id_friendlyname and rack_name"""
        self.rack_id = None
        """Server's rack id's friendly name. Not sure the difference with rack_name"""
        self.rack_id_friendlyname = None
        """Server's rack name"""
        self.rack_name = None
        """Server's enclosure (chassis) id. Call findEnclosure to get the full information or just use enclosure_id_friendlyname and enclosure_name"""
        self.enclosure_id = None
        """Server's enclosure id's friendly name. Not sure the difference with enclosure_name"""
        self.enclosure_id_friendlyname = None
        """Server's enclosure name"""
        self.enclosure_name = None

        """##############################"""
        """  Properties/More Information """
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
        """ Rack units """
        self.nb_u = None
        self.serialnumber = None
        """Server's asset number"""
        self.asset_number = None

        """##############################"""
        """        Properties/Date       """
        self.move2production = None
        self.purchase_date = None
        self.end_of_warranty = None

        """##############################"""
        """ Properties/Other information """
        self.powerA_id = None
        self.powerA_id_finalclass_recall = None
        self.powerA_id_friendlyname = None
        self.powerA_name = None
        self.powerB_id = None
        self.powerB_id_finalclass_recall = None
        self.powerB_id_friendlyname = None
        self.powerB_name = None
        self.description = None

        """##############################"""
        """           Softwares          """
        self.softwares_list = {}

        """##############################"""
        """           Contacts           """
        self.contacts_list = {}

        """##############################"""
        """           Documents          """
        self.documents_list = {}

        """##############################"""
        """            Tickets           """
        self.tickets_list = {}

        """##############################"""
        """     Application solutions    """
        self.applicationsolution_list = {}

        """##############################"""
        """      Network interfaces      """
        self.physicalinterface_list = {}

        """##############################"""
        """           FC ports           """
        self.fiberinterfacelist_list = {}

        """##############################"""
        """       network devices        """
        self.networkdevice_list = {}

        """##############################"""
        """             SANs             """
        self.san_list = {}

        """##############################"""
        """        Logical volumes       """
        self.logicalvolumes_list = {}

        """##############################"""
        """      Provider contracts      """
        self.providercontracts_list = {}

        """##############################"""
        """           Services           """
        self.services_list = {}

    def load_from_json_quattor(self, json_quattor):
        """
        Create a ItopapiServer description based on quattor s JSON output
        :param json_quattor: json
        """
        pass

    def findRack(self):
        """
        Retrieve the ItopapiRack corresponding to this server
        """
        if self.rack_id is not None:
            return ItopapiRack.find(self.rack_id)
        return None