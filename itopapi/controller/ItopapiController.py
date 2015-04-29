# -*- coding: utf8 -*-fr
"""
itopacpiController is a controller for itopapi module
"""
from itopapi.view import ItopapiConsoleView
from itopapi.model import ItopapiPrototype, ItopapiServer
from itopapi.itopapiconfig import ItopapiConfig
import urllib2
import json


class UnsupportedImportFormat(Exception):
    """
    Exception raised when --format options is not supported
    """
    pass

class ItopapiController(object):
    """
    ItopapiController is a controller for itopapi module
    """
    def __init__(self):
        self.view = ItopapiConsoleView()
        self.data = []

    def get_data(self, uri, data_format):
        """
        Load self.data according --import / --format arguments
        :param uri: URI of import file (--import)
        :param data_format: format of file (--format)
        """
        if data_format == 'quattor':
            self.load_from_quattor(uri)
        else:
            raise UnsupportedImportFormat('Format %s not supported' % data_format)

    def load_from_quattor(self, uri):
        """
        Load from quattor profile
        """
        data = json.loads(urllib2.urlopen(uri).read())
        hostname = "{0}.{1}".format(data['system']['network']['hostname'],
                                    data['system']['network']['domainname'])
        model = ItopapiServer()
        model.name = hostname
        model.friendlyname = hostname
        model.ram = data['hardware']['ram'][0]['size']
        cores = 0
        for cpu in data['hardware']['cpu']:
            cores += int(cpu['cores'])
        model.cpu = cores
        model.organization_name = ItopapiConfig.organization
        self.data.append(model)

    def load_all(self, itop_class):
        """
        Load all specific iTop class object
        :param itop_class: iTop class
        :return: []
        """
        model = ItopapiPrototype.get_itop_class(itop_class)
        if model is not None:
            self.data.extend(model.find_all())

    def load_one(self, itop_class, id_instance):
        """
        Looking for instance id
        :param itop_class: iTop class
        :param id_instance: id you want load
        """
        model = ItopapiPrototype.get_itop_class(itop_class)
        if model is not None:
            if id_instance.isdigit():
                instance = model.find(id_instance)
            else:
                instance = model.find(model.find_by_name(id_instance))
            if instance is not None:
                self.data.extend(instance)

    def delete_one(self, itop_class, id_instance):
        """
        Delete a specific id_instance
        :param itop_class: iTop class
        :param id_instance: id you want delete
        """
        # TODO: Why not just self.delete() for current objects deletion
        model = ItopapiPrototype.get_itop_class(itop_class)
        if model is not None:
            self.data.extend(model.delete(id_instance))

    def display(self):
        """
        Display with current view
        """
        self.view.display(self.data)
