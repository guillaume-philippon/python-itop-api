# -*- coding: utf8 -*-fr

"""
ItopapiConfig holds the configuration for the whole project
"""

__version__ = '1.0'
__authors__ = ['Julien Nauroy <julien.nauroy@u-psud.fr>']


class ItopapiConfig(object):
    """
    static variables
    """
    hostname = None
    username = None
    password = None
    protocol = 'https'
    base_uri = '/'
    base_suffix = None
    api_version = '1.0'
    api_suffix = '/webservices/rest.php'
    quattor_profile = None
