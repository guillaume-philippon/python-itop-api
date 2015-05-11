# -*- coding: utf8 -*-fr
"""
itopacpiController is a controller for itopapi module
"""
from itopapi.view import ItopapiConsoleView
from itopapi.model import ItopapiPrototype, ItopapiServer
from itopapi.itopapiconfig import ItopapiConfig
import urllib2
import json
import sys


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

    def get_data_from_uri(self, uri, data_format):
        """
        Load self.data according --import-uri / --format arguments
        :param uri: URI of import file (--import)
        :param data_format: format of file (--format)
        """
        data = json.loads(urllib2.urlopen(uri).read())
        self.parse_data(data, data_format)

    def get_data_from_stdin(self, data_format):
        """
        Load self.data according --import-stdin / --format arguments
        :param data_format: format of file (--format)
        """
        data = json.load(sys.stdin)
        self.parse_data(data, data_format)

    def parse_data(self, data, data_format):
        """
        Parse data loaded with --import-* / --format arguments
        :param data: data imported through (--import-*)
        :param data_format: format of file (--format)
        """
        if data_format == 'quattor':
            self.load_from_quattor(data)
        if data_format == 'itop':
            self.load_from_itop(data)
        else:
            raise UnsupportedImportFormat('Format %s not supported' % data_format)

    def load_from_quattor(self, data):
        """
        Load from quattor profile
        """
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
        model.virtualhost_name = ItopapiConfig.virtualhost
        self.data.append(model)

    def load_from_itop(self, data):
        """
        Load itop data serialized as JSON
        """
        for element in data:
            if "finalclass" in element:
                element_class = ItopapiPrototype.get_itop_class(element["finalclass"])
            else:
                raise UnsupportedImportFormat('data must have a finalclass element defined')
            if element_class is not None:
                obj = element_class(element)
                # Add the organization only if needed
                if hasattr(obj, 'organization_name'):
                    obj.organization_name = ItopapiConfig.organization
                # Add the virtualhost only if needed
                if hasattr(obj, 'virtualhost_name'):
                    obj.virtualhost_name = ItopapiConfig.virtualhost
                self.data.append(obj)
            else:
                raise UnsupportedImportFormat('data has an invalid or unsupported finalclass: %s'.format(element["finalclass"]))

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

    def delete(self):
        """
        Delete all currently-loaded instance
        """
        for obj in self.data:
            obj.delete()

    def save(self, prevent_duplicates):
        """
        Save all currently-loaded elements
        :param prevent_duplicates: Update the original object when a duplicate is found
        """
        for obj in self.data:
            has_duplicate = False
            if prevent_duplicates:
                duplicate = obj.__class__.find_by_name(obj.name)
                if duplicate is not None:
                    has_duplicate = True
            if not has_duplicate:
                obj.save()

    def display(self):
        """
        Display with current view
        """
        self.view.display(self.data)
