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
    def __init__(self):
        """
        Add itop['name'] to use generic ItopapiPrototype method
        """
        super(ItopapiServer, self).__init__()
        self.itop['name'] = 'Server'
        self.hostname_ = None
        self.organization_name = None
        self.serial = None
        self.ram = None
        self.ip = None
        self.cpu = None

    def load(self, name):
        data = self.search_object(name)
        servers = data['objects']
        for server in servers:
            self.hostname_ = servers[server]['fields']['friendlyname']
            self.organization_name = servers[server]['fields']['org_id_friendlyname']
            self.ip = None
            self.ram = servers[server]['fields']['ram']
            self.cpu = servers[server]['fields']['cpu']
            self.serial = servers[server]['fields']['serialnumber']

    def dict(self):
        return {
            'hostname': self.hostname_,
            'ram': self.ram,
            'cpu': self.cpu,
            'ip': self.ip,
            'organization': self.organization_name,
            'serial': self.serial,
        }