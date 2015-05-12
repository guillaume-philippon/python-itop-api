# -*- coding: utf8 -*-fr
# pylint: disable=invalid-name
"""
ItopapiApplicationSolution is a abstraction of Application Solution representation on iTop
"""

from itopapi.model.prototype import ItopapiPrototype

__version__ = '1.0'
__authors__ = ['Julien Nauroy <julien.nauroy@u-psud.fr>']

""" TODO not completed and tested yet, created as a dependency of TiopapiRack """
class ItopapiApplicationSolution(ItopapiPrototype):

    # Configuration specific to itop
    itop = {
        # Name of the class in Itop
        'name': 'ApplicationSolution',
        # Define which fields to save when creating or updating from the python API
        'save': ['name', 'status', 'business_criticity', 'move2production', 'description'],
        'foreign_keys': [
            {'id': 'org_id', 'name': 'organization_name', 'table': 'Organization'},
        ]
    }

    @staticmethod
    def find(key):
        """ Retrieve one or more instance of ApplicationSolution with the given key or criteria """
        return ItopapiPrototype.find(ItopapiApplicationSolution, key)

    @staticmethod
    def find_by_name(name):
        return ItopapiPrototype.find_by_name(ItopapiApplicationSolution, name)

    @staticmethod
    def find_all():
        """ Retrieve all instance of ApplicationSolution """
        return ItopapiPrototype.find_all(ItopapiApplicationSolution)

    """
    ItopapiApplicationSolution is a object that represent an Application Solution from iTop
    """
    def __init__(self, data=None):
        super(ItopapiApplicationSolution, self).__init__(data)
        ##################################
        #           Properties           #
        ##################################
        # Application Solution's organization id. Call findOrganization to get the full information or just use
        #  org_id_friendlyname and organization_name
        self.org_id = None
        # Application Solution's organization friendly name. Not sure the difference with organization_name
        self.org_id_friendlyname = None
        # Application Solution's organization name
        self.organization_name = None
        # Application Solution's status. Values within [inactive, active]
        self.status = None
        # Application Solution's business criticity. Values within [high, medium, low]
        self.business_criticity = None
        # Application Solution's move to production date
        self.move2production = None
        # Application Solution's description, as a free text
        self.description = None
        ##################################
        #             Lists              #
        ##################################
        self.functionalcis_list = None
        self.documents_list = None
        self.softwares_list = None
        self.applicationsolution_list = None
        self.tickets_list = None
        self.businessprocess_list = None
        self.services_list = None
        self.contacts_list = None
        self.providercontracts_list = None