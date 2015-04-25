# -*- coding: utf8 -*-fr

"""
ItopapiRack is a abstraction of Rack representation on iTop
"""

from itopapi.model.prototype import ItopapiPrototype

__version__ = '1.0'
__authors__ = ['Guillaume Philippon <guillaume.philippon@lal.in2p3.fr>']


class ItopapiOSFamily(ItopapiPrototype):
    """
    ItopapiRack is a object that represent a Rack from iTop
    """
    def __init__(self):
        """
        Add itop['name'] to use generic ItopapiPrototype method
        """
        super(ItopapiOSFamily, self).__init__()
        self.itop['name'] = 'OSFamily'
