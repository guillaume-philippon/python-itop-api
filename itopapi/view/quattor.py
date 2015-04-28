# -*- coding: utf8 -*-fr

"""
quattorJson will manage all interaction with JSON representation of quattor profile
"""
import urllib2
import json

class ItopapiQuattorView(object):
    """
    QuattorJson is a class that allow interaction with JSON
    """
    def __init__(self, uri):
        self.data = json.loads(urllib2.urlopen(uri).read())
        # General system information
        self.hostname = "{0}.{1}".format(self.data['system']['network']['hostname'],
                                  self.data['system']['network']['domainname'])
        self.ip = None
        interfaces = self.data['system']['network']['interfaces']
        for interface in interfaces:
            try:
                if interfaces[interface]['onboot'] == "yes":
                    self.ip = interfaces[interface]['ip']
            except KeyError:
                try:
                    self.ip = interfaces[interface]['ip']
                except KeyError:
                    pass

        # General information about hardware
        self.ram = self.data['hardware']['ram'][0]['size']
        cores = 0
        for cpu in self.data['hardware']['cpu']:
            cores += int(cpu['cores'])
        self.cpu = cores
        self.serial = self.data['hardware']['serialnumber']