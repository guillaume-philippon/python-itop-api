# -*- coding: utf8 -*-fr

"""
ItopapiServers is a abstraction of Rack representation on iTop
"""

from itopapi.model.prototype import ItopapiPrototype

__version__ = '1.0'
__authors__ = ['Guillaume Philippon <guillaume.philippon@lal.in2p3.fr>']


class ItopapiServer(ItopapiPrototype):
    """
    ItopapiServers is a object that represent a Servers from iTop
    """
    def __init__(self, config):
        """
        Add itop['name'] to use generic ItopapiPrototype method
        """
        super(ItopapiServer, self).__init__(config)
        self.itop['name'] = 'Server'
        data = self.search_object('grid01.lal.in2p3.fr')
        print data
