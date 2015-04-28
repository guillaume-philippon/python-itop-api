#!/usr/bin/env python
# -*- coding: utf8 -*-fr
# pylint: disable=too-few-public-methods
"""
Module used to load configuration from different type of backend
 load_configuration_file : file configuration
 load_configuration_cli : arguments configuration
"""
from itopapi.itopapiconfig import ItopapiConfig
import argparse


class NeedMoreArgs(Exception):
    """
    Error trigged when there are not enough arguments
    """
    pass


class ItopcliConfig(object):
    """
    ItopcliConfig represent configuration for itop-cli
    """
    file = None
    classes = []
    find_instance = None
    delete_instance = None


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
    itop_group.add_argument('--organization', dest='organization',
                            help='iTop organization to use')

    #########################
    # CLI specific argument #
    #########################
    cli_group = parser.add_argument_group('cli')
    cli_group.add_argument('--config', dest='config_file', default='./itop-cli.cfg',
                           help='configuration file CLI must use'
                                ' (default = %(default)s)')
    cli_group.add_argument('--classes', dest='classes', nargs='*', metavar='ITOP-CLASS',
                           help='iTop classes to use')
    cli_group.add_argument('--find', dest='find_instance', nargs='+', metavar='INSTANCE',
                           help='Find and display information about a given class instance given'
                                'its name or ID')
    cli_group.add_argument('--delete', dest='delete_instance', nargs=2, metavar='INSTANCE',
                           help='Delete an instance given its class name and instance ID')

    ##################################
    # Import functionality arguments #
    ##################################
    import_group = parser.add_argument_group('import')
    import_group.add_argument('--import', dest='import_uri', metavar='URI',
                              help='URI of file to import')
    import_group.add_argument('--format', dest='format',
                              help='Format of file you want import')

    options = parser.parse_args()

    ##########################
    # Load CLI configuration #
    ##########################
    ItopcliConfig.file = options.config_file
    ItopcliConfig.classes = options.classes
    if ItopcliConfig.classes is not None:
        ItopcliConfig.find_instance = options.find_instance
    else:
        if ItopcliConfig.find_instance is not None:
            raise NeedMoreArgs('--find option need --classes')
    ItopcliConfig.delete_instance = options.delete_instance

    ###########################
    # Load iTop configuration #
    ###########################
    # From configuration file first
    ItopapiConfig.read_config(options.config_file)
    # Else overwrite it with arguments
    if options.hostname is not None:
        ItopapiConfig.hostname = options.hostname
    if options.username is not None:
        ItopapiConfig.username = options.username
    if options.password is not None:
        ItopapiConfig.password = options.password
    if options.organization is not None:
        ItopapiConfig.organization = options.organization
    if options.import_uri is not None:
        if options.format is None:
            raise NeedMoreArgs('--import option need --format')
        else:
            ItopapiConfig.import_uri = options.import_uri
    if options.format is not None:
        ItopapiConfig.format = options.format
