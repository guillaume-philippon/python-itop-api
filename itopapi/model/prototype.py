# -*- coding: utf8 -*-fr

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
    Exeception raised when a method is not implemented on child class but cannot be generic
    """
    pass


class ItopapiPrototype(object):
    """
    Standard interface with iTop is in ItopapiConfig
    """
    def __init__(self):
        self.itop = {}

    def _uri_(self):
        """
        Build a URI to access to rest interface of iTop
        :return: string
        """
        return '{0}://{1}{2}{3}'.format(ItopapiConfig.protocol,
                                        ItopapiConfig.hostname,
                                        ItopapiConfig.base_suffix,
                                        ItopapiConfig.api_suffix)

    def _params_(self, json_data):
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

    # TODO: list_command must be a @staticmethod
    def list_command(self):
        """
        List all operations available by REST API
        :return: dict
        """
        json_data = json.dumps({
            'operation': 'list_operations'
        })
        uri = self._uri_()
        params = self._params_(json_data)
        return json.loads(urllib2.urlopen(uri, params).read())

    def list_objects(self):
        """
        List all objects from child class
        :return: dict
        """
        json_data = json.dumps({
            'operation': 'core/get',
            'class': self.itop['name'],
            'key': 'SELECT {0}'.format(self.itop['name']),
        })
        uri = self._uri_()

        params = self._params_(json_data)
        return json.loads(urllib2.urlopen(uri, params).read())
