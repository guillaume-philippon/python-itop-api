"""
ItopapiServers is a abstraction of Rack representation on iTop
"""

from itopapi.prototype import ItopapiPrototype

__version__ = '1.0'
__authors__ = ['Guillaume Philippon <guillaume.philippon@lal.in2p3.fr>']


class ItopapiServers(ItopapiPrototype):
    """
    ItopapiServers is a object that represent a Servers from iTop
    """
    def __init__(self):
        """
        Add itop['name'] to use generic ItopapiPrototype method
        """
        super(ItopapiServers, self).__init__()
        self.itop['name'] = 'Server'
