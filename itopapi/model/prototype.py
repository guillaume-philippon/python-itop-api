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


class UnknownItopClass(Exception):
    """
    Error raised if ItopClass is not supported
    """
    pass


class ItopapiUnimplementedMethod(Exception):
    """
    Exception raised when a method is not implemented on child class but cannot be generic
    """
    pass


class ItopapiPrototype(object):
    """
    Standard interface with iTop is in ItopapiConfig
    """

# Configuration specific to itop, not relevant to Prototype
    itop = {'name': '', 'save': [], 'foreign_keys': []}

    def __init__(self, data=None):
        self.instance_id = None
        # Every instance should have an unique ID
        self.name = None
        # Every instance has a common name
        self.friendlyname = None
        # Every instance has a friendlyname
        self.finalclass = None
        # Should be the same as self.itop['name']. Each instance has one

        # If default data was passed as an argument, load it and then resolve sub-lists
        if data is not None:
            self.__dict__.update(data)
            self.__process_lists()

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
        return "{0}{{id={1},name={2}}}".format(self.__class__.__name__, self.instance_id, self.name.encode(
            'ascii', 'ignore'))

    @staticmethod
    def find_all(itop_class):
        """
        List all objects for a given class
        :return: dict
        """
        return ItopapiPrototype.find(itop_class, 'SELECT {0}'.format(itop_class.itop['name']))

    @staticmethod
    def find_by_name(itop_class, name):
        """
        Find specific name entry into all itop_class
        :param itop_class: string
        :param name: string
        :return: Itopapi*
        """
        return ItopapiPrototype.find(itop_class, {'name': name})

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
            obj = itop_class({})
            obj.instance_id = data['objects'][information]['key']
            # update all the object's fields with the following line
            obj.__dict__.update(data['objects'][information]['fields'])
            obj.__process_lists()
            objects.append(obj)

        # Return None, as a commodity, if there's 0 result
        if len(objects) == 0:
            return None
        else:
            return objects

    def save(self):
        """
        Updates the current instance if it already exists in itop's database (i.e. the id is set)
        or creates a new one
        :return:
        """

        # Define the fields to save
        fields = {}
        for field in self.__class__.itop['save']:
            value = self.__dict__[field]
            if value is not None:
                fields[field] = value
        # Add the foreign keys. The rule is: if there's an id, then use it, else use the name as a subquery
        for field in self.__class__.itop['foreign_keys']:
            field_id = field['id']
            field_name = field['name']
            field_id_value = self.__dict__[field_id]
            field_name_value = self.__dict__[field_name]
            if field_id_value is not None:
                fields[field_id] = field_id_value
            elif field_name_value is not None:
                fields[field_id] = 'SELECT {0} WHERE name = "{1}"'.format(field['table'], field_name_value)

        print json.dumps(fields, sort_keys=True, indent=4, separators=(',', ': '))

        query = {
            'comment': 'Creating/Updating object from python-itop-api',
            'class': self.__class__.itop['name'],
            'fields': fields
            }
        if self.instance_id is not None:
            query['operation'] = 'core/update'
            query['key'] = self.instance_id
        else:
            query['operation'] = 'core/create'
            query['output_fields'] = self.instance_id
            query['output_fields'] = 'id, friendlyname',

        json_data = json.dumps(query)
        uri = ItopapiPrototype._uri_()
        params = ItopapiPrototype._params_(json_data)
        result = json.loads(urllib2.urlopen(uri, params).read())
        # In case of a save, update the ID
        if (result['code'] == '0') and (self.instance_id is None):
            objects = result['objects']
            self.instance_id = objects[objects.keys()[0]].id

        return result

    def delete(self):
        """
        Deletes the current instance if it exists in itop's database (i.e. the id is set)
        :return:
        """
        data = {
            'operation': 'core/delete',
            'comment': 'Deleting object from python-itop-api',
            'class': self.__class__.itop['name'],
            'simulate': ItopapiConfig.simulate_deletes
            }
        if self.instance_id is not None:
            data['key'] = self.instance_id
        elif self.name is not None:
            # Attempt at deleting an object with the same name
            data['key'] = {'name': self.name}
        else:
            print "Error: neither instance_id nor name is set for the following object:"
            print self
            exit(1)

        json_data = json.dumps(data)
        uri = ItopapiPrototype._uri_()
        params = ItopapiPrototype._params_(json_data)
        result = json.loads(urllib2.urlopen(uri, params).read())
        # Reset the id to None to reflect that the instance doesn't exist anymore in the
        # database
        self.instance_id = None
        return result

    def __process_lists(self):
        """
        Process all sub-lists of an instance and instantiate regular Itopapi classes where dictionaries
        are fetched using the Itop API.
        :return:
        """
        ItopapiPrototype.__subclasses__()
        for key, value in self.__dict__.iteritems():
            if isinstance(value, list):
                new_list = []
                # For each element, find its type given by the "finalclass" attribute
                # and instantiate the corresponding object
                for element in value:
                    element_class = ItopapiPrototype.get_itop_class(element["finalclass"])
                    obj = element_class(element)
                    new_list.append(obj)

                self.__dict__[key] = new_list

    # __classes contains the list of ItopapiPrototype's subclasses
    __classes = {}

    @staticmethod
    def get_itop_class(itop_class):
        """
        Associate the string passed as an argument to the corresponding Itop class
        Maybe move it to ItopapiPrototype someday
        :param itop_class: iTop class
        """
        itop_class = itop_class.lower()
        # Populate the list of classes if need be
        if len(ItopapiPrototype.__classes) == 0:
            for c in ItopapiPrototype.__subclasses__():
                ItopapiPrototype.__classes[c.itop["name"].lower()] = c

        # Retrieve the proper class depending on the name
        c = ItopapiPrototype.__classes[itop_class]
        if c is not None:
            return c
        else:
            raise UnknownItopClass()
