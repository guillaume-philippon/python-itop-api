"""
Prototype is a empty class which define all needed method
"""
import urllib2
import urllib
import json


class ItopapiUnimplementedMethod(Exception):
    pass


class ItopapiPrototype(object):
    def __init__(self):
        self.hostname = None;
        self.api_suffix = '/webservices/rest.php';
        self.version = '1.0';
        self.username = None;
        self.password = None;
        self.itop_name = None;

    def _params_(self, json_data):
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
        uri = 'https://{0}{1}'.format(self.hostname, self.api_suffix)
        params = self._params_(json_data)
        return json.loads(urllib2.urlopen(uri, params).read())

    def list_objects(self):
        json_data = json.dumps({
            'operation': 'core/get',
            'class': self.itop_name,
            'key': 'SELECT {0}'.format(self.itop_name),
        })
        uri = 'https://{0}{1}'.format(self.hostname, self.api_suffix)
        params = self._params_(json_data)
        return json.loads(urllib2.urlopen(uri, params).read())
