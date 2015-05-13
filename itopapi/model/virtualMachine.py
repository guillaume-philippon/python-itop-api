# -*- coding: utf8 -*-fr

"""
ItopapiVirtualMachine is a abstraction of VLAN representation on iTop
"""

from itopapi.model.prototype import ItopapiPrototype, ItopapiUnimplementedMethod

__version__ = '1.0'
__authors__ = ['Julien Nauroy <julien.nauroy@u-psud.fr>']


class ItopapiVirtualMachine(ItopapiPrototype):

    # Configuration specific to itop
    itop = {
        # Name of the class in Itop
        'name': 'VirtualMachine',
        'save': ['name', 'status', 'business_criticity',
                 'managementip', 'oslicence_id', 'cpu', 'ram', 'move2production',
                 'description'],
        'foreign_keys': [
            {'id': 'virtualhost_id', 'name': 'virtualhost_name', 'table': 'VirtualHost'},
            {'id': 'org_id', 'name': 'organization_name', 'table': 'Organization'},
            {'id': 'osfamily_id', 'name': 'osfamily_name', 'table': 'OSFamily'},
            {'id': 'osversion_id', 'name': 'osversion_name', 'table': 'OSVersion'},
            {'id': 'oslicence_id', 'name': 'oslicence_name', 'table': 'OSLicence'},
        ]
    }

    @staticmethod
    def find(key):
        """ Retrieve one or more instance of PhysicalInterface with the given key or criteria """
        return ItopapiPrototype.find(ItopapiVirtualMachine, key)

    @staticmethod
    def find_by_name(name):
        return ItopapiPrototype.find_by_name(ItopapiVirtualMachine, name)

    @staticmethod
    def find_all():
        """ Retrieve all instance of PhysicalInterface """
        return ItopapiPrototype.find_all(ItopapiVirtualMachine)

    """
    ItopapiPhysicalInterface is an object that represents a PhysicalInterface from iTop
    """
    def __init__(self, data=None):
        super(ItopapiVirtualMachine, self).__init__(data)

        ##################################
        # Properties/General Information #
        ##################################
        # VirtualMachine's organization id. Call find_organization to get the full information or just
        #  use org_id_friendlyname and organization_name
        self.org_id = None
        # VirtualMachine's organization friendly name. Not sure the difference with organization_name
        self.org_id_friendlyname = None
        # VirtualMachine's organization name
        self.organization_name = None
        # VirtualMachine's status. Values within [implementation, obsolete, production, stock]
        self.status = None
        # VirtualMachine's business criticity. Values within [high, medium, low]
        self.business_criticity = None
        # VirtualMachine's virtual host
        self.virtualhost_id = None
        self.virtualhost_id_finalclass_recall = None
        self.virtualhost_id_friendlyname = None
        self.virtualhost_name = None

        ##################################
        #  Properties/More Information   #
        ##################################

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

        ##################################
        #        Properties/Date         #
        ##################################

        ##################################
        #  Properties/Other Information  #
        ##################################
        # VirtualMachine's move to production date
        self.move2production = None
        # VirtualMachine's description, as a free text
        self.description = None

        ##################################
        #           Softwares            #
        ##################################
        # VirtualMachine's softwares list
        self.softwares_list = {}

        ##################################
        #            Contacts            #
        ##################################
        # VirtualMachine's contacts list
        self.contacts_list = {}

        ##################################
        #           Documents            #
        ##################################
        # VirtualMachine's documents list
        self.documents_list = {}

        ##################################
        #            Tickets             #
        ##################################
        # VirtualMachine's tickets list
        self.tickets_list = {}

        ##################################
        #     Application solutions      #
        ##################################
        # VirtualMachine's application solutions list
        self.applicationsolution_list = {}

        ##################################
        #       Network interfaces       #
        ##################################
        # VirtualMachine's network interfaces list
        self.physicalinterface_list = {}

        ##################################
        #        Logical volumes         #
        ##################################
        # VirtualMachine's logical volumes list
        self.logicalvolumes_list = {}

        ##################################
        #       Provider contracts       #
        ##################################
        # VirtualMachine's provider contracts list
        self.providercontracts_list = {}

        ##################################
        #            Services            #
        ##################################
        # VirtualMachine's services list
        self.services_list = {}

    def load_from_json_quattor(self, json_quattor):
        """
        Create a ItopapiVirtualMachine description based on quattor s JSON output
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

    def find_os_family(self):
        """
        Retrieve the ItopapiOSFamily corresponding to this VirtualMachine
        """
        if self.osfamily_id is not None:
            ItopapiPrototype.get_itop_class('OSFamily').find(self.osfamily_id)
        return None

    def find_os_version(self):
        """
        Retrieve the ItopapiOSVersion corresponding to this server
        """
        if self.osversion_id is not None:
            ItopapiPrototype.get_itop_class('OSVersion').find(self.osfamily_id)
        return None

    def find_os_licence(self):
        """
        Retrieve the ItopapiOSLicence corresponding to this server
        """
        if self.oslicence_id is not None:
            ItopapiPrototype.get_itop_class('OSLicence').find(self.osfamily_id)
        return None