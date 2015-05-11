# -*- coding: utf8 -*-fr
# pylint: disable=too-few-public-methods
"""
ItopapiConfig holds the configuration for the whole project
"""

__version__ = '1.0'
__authors__ = ['Julien Nauroy <julien.nauroy@u-psud.fr>']

import ConfigParser


class ItopapiConfig(object):
    """
    static variables
    """
    hostname = None
    username = None
    password = None
    protocol = 'https'
    base_uri = '/'
    api_version = '1.0'
    api_suffix = '/webservices/rest.php'
    import_uri = None
    import_stdin = False
    save = None
    format = None
    organization = None
    virtualhost = None
    # Do not really delete, only check if the deletion would occur
    simulate_deletes = False
    # Prevent duplicate names when adding new items
    prevent_duplicates = False

    @staticmethod
    def read_config(config_file):
        """
        Read the configuration file given the file name given as an argument
        and update the configuration accordingly
        :param config_file: Configuration file to read
        :return:
        """
        config_parser = ConfigParser.ConfigParser()
        config_parser.read(config_file)
        try:
            ItopapiConfig.hostname = config_parser.get('main', 'hostname')
        except ConfigParser.NoOptionError:
            pass
        try:
            ItopapiConfig.username = config_parser.get('main', 'username')
        except ConfigParser.NoOptionError:
            pass
        try:
            ItopapiConfig.password = config_parser.get('main', 'password')
        except ConfigParser.NoOptionError:
            pass
        try:
            ItopapiConfig.protocol = config_parser.get('main', 'protocol')
        except ConfigParser.NoOptionError:
            pass
        try:
            ItopapiConfig.base_uri = config_parser.get('main', 'base_uri')
        except ConfigParser.NoOptionError:
            pass
        try:
            ItopapiConfig.api_version = config_parser.get('main', 'api_version')
        except ConfigParser.NoOptionError:
            pass
        try:
            ItopapiConfig.api_suffix = config_parser.get('main', 'api_suffix')
        except ConfigParser.NoOptionError:
            pass
        try:
            ItopapiConfig.organization = config_parser.get('main', 'organization')
        except ConfigParser.NoOptionError:
            pass
        try:
            ItopapiConfig.virtualhost = config_parser.get('main', 'virtualhost')
        except ConfigParser.NoOptionError:
            pass
        try:
            simulate_deletes = config_parser.get('main', 'simulate_deletes')
            if simulate_deletes.lower() == "true":
                ItopapiConfig.simulate_deletes = True
        except ConfigParser.NoOptionError:
            pass
        try:
            prevent_duplicates = config_parser.get('main', 'prevent_duplicates')
            if prevent_duplicates.lower() == "true":
                ItopapiConfig.prevent_duplicates = True
        except ConfigParser.NoOptionError:
            pass
