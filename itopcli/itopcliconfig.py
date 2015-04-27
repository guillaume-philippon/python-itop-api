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

    #########################
    # CLI specific argument #
    #########################
    cli_group = parser.add_argument_group('cli')
    cli_group.add_argument('--config', dest='config_file', default='./itop-cli.cfg',
                           help='configuration file CLI must use'
                                ' (default = %(default)s)')
    cli_group.add_argument('--classes', dest='classes', nargs='*',
                           help='iTop classes to use')
    cli_group.add_argument('--find', dest='find_instance', nargs=2,
                           help='Find and display information about'
                                ' a given class instance given its name and ID')
    cli_group.add_argument('--delete', dest='delete_instance', nargs=2,
                           help='Delete an instance given its class name'
                                ' and instance ID')
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
    ItopcliConfig.find_instance = options.find_instance
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
    if options.quattor_profile is not None:
        ItopapiConfig.quattor_profile = options.quattor_profile
