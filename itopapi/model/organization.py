# -*- coding: utf8 -*-fr
# pylint: disable=invalid-name
"""
ItopapiOrganization is a abstraction of Organization representation on iTop
"""

from itopapi.model.prototype import ItopapiPrototype
from itopapi.model.deliveryModel import ItopapiDeliveryModel

__version__ = '1.0'
__authors__ = ['Julien Nauroy <julien.nauroy@u-psud.fr>']

class ItopapiOrganization(ItopapiPrototype):

    # Configuration specific to itop
    itop = {
        # Name of the class in Itop
        'name': 'Organization',
        # Define which fields to save when creating or updating from the python API
        'save': ['name', 'code', 'status'],
        'foreign_keys': [
            {'id': 'parent_id', 'name': 'parent_name', 'table': 'Organization'},
            {'id': 'deliverymodel_id', 'name': 'deliverymodel_name', 'table': 'DeliveryModel'},
        ]
    }

    @staticmethod
    def find(key):
        """ Retrieve one or more instance of ApplicationSolution with the given key or criteria """
        return ItopapiPrototype.find(ItopapiOrganization, key)

    @staticmethod
    def find_by_name(name):
        return ItopapiPrototype.find_by_name(ItopapiOrganization, name)

    @staticmethod
    def find_all():
        """ Retrieve all instance of OSFamily """
        return ItopapiPrototype.find_all(ItopapiOrganization)

    """
    ItopapiOrganization is a object that represents an Application Solution from iTop
    """
    def __init__(self, data=None):
        super(ItopapiOrganization, self).__init__(data)

        self.code = None
        # Application Solution's status. Values within [inactive, active]
        self.status = None
        # Parent information
        self.parent_id = None
        self.parent_name = None
        self.parent_id_friendlyname = None
        # Delivery model
        self.deliverymodel_id = None
        self.deliverymodel_name = None
        self.deliverymodel_id_friendlyname = None

    def find_parent(self):
        """
        Retrieve the parent ItopapiOrganization
        """
        if self.parent_id is not None:
            return ItopapiOrganization.find(self.parent_id)
        return None

    def find_delivery_model(self):
        """
        Retrieve the ItopapiDeliveryModel associated with this entry
        """
        if self.deliverymodel_id is not None:
            return ItopapiDeliveryModel.find(self.deliverymodel_id)
        return None