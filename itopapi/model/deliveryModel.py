# -*- coding: utf8 -*-fr
# pylint: disable=invalid-name
"""
ItopapiDeliveryModel is a abstraction of Organization representation on iTop
"""

from itopapi.model.prototype import ItopapiPrototype

__version__ = '1.0'
__authors__ = ['Julien Nauroy <julien.nauroy@u-psud.fr>']

class ItopapiDeliveryModel(ItopapiPrototype):

    # Configuration specific to itop
    itop = {
        # Name of the class in Itop
        'name': 'DeliveryModel',
        # Define which fields to save when creating or updating from the python API
        'save': ['name', 'description'],
        'foreign_keys': [
            {'id': 'organization_id', 'name': 'organization_name', 'table': 'Organization'},
        ]
    }

    @staticmethod
    def find(key):
        """ Retrieve one or more instance of ApplicationSolution with the given key or criteria """
        return ItopapiPrototype.find(ItopapiDeliveryModel, key)

    @staticmethod
    def find_by_name(name):
        return ItopapiPrototype.find_by_name(ItopapiDeliveryModel, name)

    @staticmethod
    def find_all():
        """ Retrieve all instance of OSFamily """
        return ItopapiPrototype.find_all(ItopapiDeliveryModel)

    """
    ItopapiDeliveryModel is a object that represent an Application Solution from iTop
    """
    def __init__(self, data=None):
        super(ItopapiDeliveryModel, self).__init__(data)

        self.description = None
        self.org_id = None
        self.organization_name = None
        self.org_id_friendlyname = None

        ##################################
        #              Lists             #
        ##################################
        self.customers_list = []
        self.contacts_list = []

    def find_organization(self):
        """
        Retrieve the parent ItopapiOrganization
        """
        if self.org_id is not None:
            ItopapiPrototype.get_itop_class('Organization').find(self.org_id)
        return None