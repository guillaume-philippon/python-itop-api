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
    """
    ItopapiApplicationSolution is a object that represent an Application Solution from iTop
    """
    def __init__(self):
        """
        Add itop['name'] to use generic ItopapiPrototype method
        """
        super(ItopapiApplicationSolution, self).__init__()
        self.itop['name'] = 'ApplicationSolution'
