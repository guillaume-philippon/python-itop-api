"""
Prototype is a empty class which define all needed method
"""
import urllib2
import urllib
import json

__version__ = '1.0'
__authors__ = ['Guillaume Philippon <guillaume.philippon@lal.in2p3.fr>']


class ItopapiUnimplementedMethod(Exception):
    """
    Exeception raised when a method is not implemented on child class but cannot be generic
    """
    pass


class ItopapiPrototype(object):
    """
    Standard interface with iTop
    """
    def __init__(self):
        self.hostname = None
        self.api_suffix = '/webservices/rest.php'
        self.version = '1.0'
        self.username = None
        self.password = None
        self.itop = {}
        self.protocol = 'https'
        self.base_suffix = ''

    def _uri_(self):
        """
        Build a URI to access to rest interface of iTop
        :return: string
        """
        return '{0}://{1}{2}{3}'.format(self.protocol,
                                        self.hostname,
                                        self.base_suffix,
                                        self.api_suffix)

    def _params_(self, json_data):
        """
        Build a URLEncoded JSON file
        :param json_data:
        :return:
        """
        return urllib.urlencode({
            'version': self.version,
            'auth_user': self.username,
            'auth_pwd': self.password,
            'json_data': json_data
        })

    def list_command(self):
        json_data = json.dumps({
            'operation': 'list_operations'
        })
        uri = self._uri_()
        params = self._params_(json_data)
        return json.loads(urllib2.urlopen(uri, params).read())

    def list_objects(self):
        json_data = json.dumps({
            'operation': 'core/get',
            'class': self.itop['name'],
            'key': 'SELECT {0}'.format(self.itop['name']),
        })
        uri = self._uri_()
        params = self._params_(json_data)
        return json.loads(urllib2.urlopen(uri, params).read())
