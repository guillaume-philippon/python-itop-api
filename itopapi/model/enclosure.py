# -*- coding: utf8 -*-fr

"""
ItopapiEnclosure is a abstraction of Rack representation on iTop
"""

from itopapi.model.prototype import ItopapiPrototype

__version__ = '1.0'
__authors__ = ['Julien Nauroy <julien.nauroy@u-psud.fr>']


class ItopapiEnclosure(ItopapiPrototype):

    # Configuration specific to itop
    itop = {
        # Name of the class in Itop
        'name': 'Enclosure',
        # Define which fields to save when creating or updating from the python API
        'save': ['name', 'status', 'business_criticity', 'nb_u', 'serialnumber', 'asset_number',
                 'move2production', 'purchase_date', 'end_of_warranty', 'description'],
        'foreign_keys': [
            {'id': 'org_id', 'name': 'organization_name', 'table': 'Organization'},
            {'id': 'location_id', 'name': 'location_name', 'table': 'Localization'},
            {'id': 'rack_id', 'name': 'rack_name', 'table': 'Rack'},
            {'id': 'brand_id', 'name': 'brand_name', 'table': 'Brand'},
            {'id': 'model_id', 'name': 'model_name', 'table': 'Model'},
        ]
    }
    @staticmethod
    def find(key):
        """ Retrieve one or more instance of Enclosure with the given key or criteria """
        return ItopapiPrototype.find(ItopapiEnclosure, key)

    @staticmethod
    def find_by_name(name):
        return ItopapiPrototype.find_by_name(ItopapiEnclosure, name)

    @staticmethod
    def find_all():
        """ Retrieve all instance of Enclosure """
        return ItopapiPrototype.find_all(ItopapiEnclosure)

    """
    """
    def __init__(self, data=None):
        super(ItopapiEnclosure, self).__init__(data)
        # Enclosure's organization id. Call find_organization to get the full information or just
        #  use org_id_friendlyname and organization_name
        self.org_id = None
        # Enclosure's organization friendly name. Not sure the difference with organization_name
        self.org_id_friendlyname = None
        # Enclosure's organization name
        self.organization_name = None
        # Enclosure's status. Values within [implementation, obsolete, production, stock]
        self.status = None
        # Enclosure's business criticity. Values within [high, medium, low]
        self.business_criticity = None
        # Enclosure's location id. Call find_location to get the full information or just use
        # location_id_friendlyname and location_name
        self.location_id = None
        # Enclosure's location id's friendly name. Not sure the difference with location_name
        self.location_id_friendlyname = None
        # Enclosure's location name
        self.location_name = None
        # Enclosure's rack id. Call findRack to get the full information or just use rack_id
        # friendlyname and rack_name
        self.rack_id = None
        # Enclosure's rack id's friendly name. Not sure the difference with rack_name
        self.rack_id_friendlyname = None
        # Enclosure's rack name
        self.rack_name = None
        self.brand_id = None
        self.brand_id_friendlyname = None
        self.brand_name = None
        self.model_id = None
        self.model_id_friendlyname = None
        self.model_name = None
        # Rack units
        self.nb_u = None
        # Serial number
        self.serialnumber = None
        # Asset number
        self.asset_number = None
        # Server's move to production date
        self.move2production = None
        # Server's purchase date
        self.purchase_date = None
        # Server's end of warranty date
        self.end_of_warranty = None
        self.description = None

    def find_organization(self):
        """
        Retrieve the ItopapiOrganization corresponding to this server
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

    def find_rack(self):
        """
        Retrieve the ItopapiRack corresponding to this server
        """
        if self.rack_id is not None:
            ItopapiPrototype.get_itop_class('Rack').find(self.rack_id)
        return None
