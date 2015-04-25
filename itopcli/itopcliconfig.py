#!/usr/bin/env python
# -*- coding: utf8 -*-fr
"""
Module used to load configuration from different type of backend
 load_configuration_file : file configuration
 load_configuration_cli : arguments configuration
"""
from itopapi.itopapiconfig import ItopapiConfig
import ConfigParser
import argparse


class ItopcliConfig(object):
    """
    ItopcliConfig represent configuration for itop-cli
    """
    file = None
    classes = []


def load_configuration_file(config_file):
    """
    Load configuration from file
    :param config_file: name of configuration file
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


def load_configuration_cli():
    """
    Load configuration from CLI. This function return a dictionary of all parameters which is not
    related of API itself
    :return: dict
    """
    parser = argparse.ArgumentParser(description="python CLI for iTop REST api")
    ##########################
    # iTop specific argument #
    ##########################
    itop_group = parser.add_argument_group('itop')
    itop_group.add_argument('--hostname', dest='hostname',
                                  help='hostname of iTop server')
    itop_group.add_argument('--username', dest='username',
                                  help='username for iTop authentication')
    itop_group.add_argument('--password', dest='password',
                                  help='password for iTop authentication')

    #########################
    # CLI specific argument #
    #########################
    cli_group = parser.add_argument_group('cli')
    cli_group.add_argument('--config', dest='config_file', default='./itop-cli.cfg',
                           help='configuration file CLI must use'
                                ' (default = %(default)s)')
    cli_group.add_argument('--classes', dest='classes', nargs='*',
                           help='iTop classes to use')
    cli_group.add_argument('--organization', dest='organization',
                           help='iTop organization to use')
    cli_group.add_argument('--quattor-profile', dest='quattor_profile',
                           help='URI of quattor profile')

    options = parser.parse_args()

    ##########################
    # Load CLI configuration #
    ##########################
    ItopcliConfig.file = options.config_file
    ItopcliConfig.classes = options.classes

    ###########################
    # Load iTop configuration #
    ###########################
    # From configuration file first
    load_configuration_file(ItopcliConfig.file)
    # Else overwrite it with arguments
    if options.hostname is not None:
        ItopapiConfig.hostname = options.hostname
    if options.username is not None:
        ItopapiConfig.username = options.username
    if options.password is not None:
        ItopapiConfig.password = options.password
    if options.quattor_profile is not None:
        ItopapiConfig.quattor_profile = options.quattor_profile
