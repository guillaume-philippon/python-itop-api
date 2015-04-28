# -*- coding: utf8 -*-fr
# pylint: disable=wildcard-import, no-member, unused-wildcard-import
"""
Prototype is an empty class which defines all required methods for child classes
"""
import urllib2
import urllib
import json
from itopapi.itopapiconfig import ItopapiConfig

__version__ = '1.0'
__authors__ = ['Guillaume Philippon <guillaume.philippon@lal.in2p3.fr>']


class ItopapiUnimplementedMethod(Exception):
    """
    Exception raised when a method is not implemented on child class but cannot be generic
    """
    pass


class ItopapiPrototype(object):
    """
    Standard interface with iTop is in ItopapiConfig
    """
    def __init__(self):
        self.instance_id = None
        # Every instance should have an unique ID
        self.name = None
        # Every instance has a common name
        self.friendlyname = None
        # Every instance has a friendlyname
        self.finalclass = None
        # Should be the same as self.itop['name']. Each instance has one

    @staticmethod
    def _uri_():
        """
        Build a URI to access to rest interface of iTop
        :return: string
        """
        return '{protocol}://{hostname}{base_uri}{api_suffix}'.format(**ItopapiConfig.__dict__)

    @staticmethod
    def _params_(json_data):
        """
        Build a URLEncoded JSON file
        :param json_data:
        :return: urlib
        """
        return urllib.urlencode({
            'version': ItopapiConfig.api_version,
            'auth_user': ItopapiConfig.username,
            'auth_pwd': ItopapiConfig.password,
            'json_data': json_data
        })

    @staticmethod
    def list_commands():
        """
        List all operations available by REST API
        :return: dict
        """
        json_data = json.dumps({
            'operation': 'list_operations'
        })
        uri = ItopapiPrototype._uri_()
        params = ItopapiPrototype._params_(json_data)
        return json.loads(urllib2.urlopen(uri, params).read())

    def __str__(self):
        """
        Formats java-style
        :return: string
        """
        return "{0}{{id={1},name={2}}}".format(self.__class__.__name__, self.instance_id, self.name)

    @staticmethod
    def find_all(itop_class):
        """
        List all objects for a given class
        :return: dict
        """
        return ItopapiPrototype.find(itop_class, 'SELECT {0}'.format(itop_class.itop['name']))

    @staticmethod
    def find(itop_class, key):
        """
        Find a list of objects given its id or some criteria passed as a dictionary
        :param itop_class:
        :param key:
        :return: array or None if there is no object
        """
        json_data = json.dumps({
            'operation': 'core/get',
            'class': itop_class.itop['name'],
            'key': key,
        })

        uri = ItopapiPrototype._uri_()

        params = ItopapiPrototype._params_(json_data)
        data = json.loads(urllib2.urlopen(uri, params).read())

        # If there's no object to process, return immediately
        if data['objects'] is None:
            return None

        objects = []
        for information in data['objects']:
            obj = itop_class()
            obj.instance_id = data['objects'][information]['key']
            # update all the object's fields with the following line
            obj.__dict__.update(data['objects'][information]['fields'])
            objects.append(obj)

        # Return None, as a commodity, if there's 0 result
        if len(objects) == 0:
            return None
        else:
            return objects

    @staticmethod
    def find_by_name(itop_class, name):
        """
        Find specific name entry into all itop_class
        :param itop_class: string
        :param name: string
        :return: Itopapi*
        """
        return ItopapiPrototype.find(itop_class, {'name': name})

    def save(self):
        """
        Updates the current instance if it already exists in itop's database (i.e. the id is set)
        or creates a new one
        :return:
        """
        operation = 'core/create'
        if self.instance_id is not None:
            operation = 'core/update'
        # TODO the main problem will be automatically sorting keys that would have to be saved
        # or not. As an example, org_id should be saved, org_id_friendlyname should not
        raise ItopapiUnimplementedMethod()

    def delete(self):
        """
        Deletes the current instance if it exists in itop's database (i.e. the id is set)
        :return:
        """
        if self.instance_id is not None:
            json_data = json.dumps({
                'operation': 'core/delete',
                'comment': 'Deleting object from python-itop-api',
                'class': self.__class__.itop['name'],
                'key': self.instance_id,
                'simulate': ItopapiConfig.simulate_deletes
            })
            uri = ItopapiPrototype._uri_()
            params = ItopapiPrototype._params_(json_data)
            result = json.loads(urllib2.urlopen(uri, params).read())
            # Reset the id to None to reflect that the instance doesn't exist anymore in the
            # database
            self.instance_id = None
            return result
