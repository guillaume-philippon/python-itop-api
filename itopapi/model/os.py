# -*- coding: utf8 -*-fr

"""
ItopapiRack is a abstraction of Rack representation on iTop
"""

from itopapi.model.prototype import ItopapiPrototype

__version__ = '1.0'
__authors__ = ['Guillaume Philippon <guillaume.philippon@lal.in2p3.fr>']


class ItopapiOSFamily(ItopapiPrototype):

    # Configuration specific to itop
    itop = {'name': 'OSFamily'}

    """
    ItopapiOSFamily is an object that represent an OS Family from iTop
    """
    def __init__(self, data = None):
        super(ItopapiOSFamily, self).__init__(data)
