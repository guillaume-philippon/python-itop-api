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
    Error triggered when there are not enough arguments
    """
    pass


class IncompatibleArgs(Exception):
    """
    Error triggered when there are not enough arguments
    """
    pass


class ItopcliConfig(object):
    """
    ItopcliConfig represent configuration for itop-cli
    """
    file = None
    classes = []
    find_instance = None
    delete_instances = None
    save = None


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
    itop_group.add_argument('--organization', dest='organization', metavar='ORGANIZATION-NAME',
                            help='iTop organization to use')
    itop_group.add_argument('--virtualhost', dest='virtualhost', metavar='VIRTUAL-HOSTNAME',
                            help='Itop\'s virtual host name for VMs')

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
    cli_group.add_argument('--delete', dest='delete_instances', action='store_true',
                           help='Delete all instances previously loaded')

    ##################################
    # Import functionality arguments #
    ##################################
    import_group = parser.add_argument_group('import')
    import_group.add_argument('--import-uri', dest='import_uri', metavar='URI',
                              help='URI of file to import')
    import_group.add_argument('--import-stdin', dest='import_stdin', action='store_true',
                              help='import data from STDIN')
    import_group.add_argument('--format', dest='format',
                              help='Format of file you want import')
    cli_group.add_argument('--save', dest='save', action='store_true',
                           help='Save the instances loaded through import')
    cli_group.add_argument('--prevent-duplicates', dest='prevent_duplicates', action='store_true',
                           help='Check if objects with the same name already exist before saving'
                                'and don\'t save in this case')
    cli_group.set_defaults(save=False)

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
    if ItopcliConfig.delete_instances is not None:
        if (ItopcliConfig.find_instance is None) or (
                        ItopapiConfig.import_uri is None and ItopapiConfig.import_stdin is None):
            raise NeedMoreArgs('--delete option needs a fetch function such as --classes or --import-* ')
    ItopcliConfig.delete_instances = options.delete_instances
    ItopcliConfig.save = options.save

    ###########################
    # Load iTop configuration #
    ###########################
    # From configuration file first
    ItopapiConfig.read_config(options.config_file)
    # Then overwrite it with arguments
    if options.hostname is not None:
        ItopapiConfig.hostname = options.hostname
    if options.username is not None:
        ItopapiConfig.username = options.username
    if options.password is not None:
        ItopapiConfig.password = options.password
    if options.organization is not None:
        ItopapiConfig.organization = options.organization
    if options.virtualhost is not None:
        ItopapiConfig.virtualhost = options.virtualhost
    if options.save and options.delete_instances:
        raise IncompatibleArgs('--save and --delete are mutually exclusive')
    if options.save and (options.import_uri and None or options.import_stdin is None):
        raise NeedMoreArgs('--save option needs --import-uri or --import-stdin')
    if (options.import_uri is not None) and (options.format is None):
        raise NeedMoreArgs('--import-uri option needs --format')
    ItopapiConfig.import_uri = options.import_uri
    if options.import_stdin and (options.format is None):
        raise NeedMoreArgs('--import-stdin option needs --format')
    ItopapiConfig.import_stdin = options.import_stdin
    if options.prevent_duplicates and not options.save:
        raise NeedMoreArgs('--prevent-duplicates option needs --save')
    ItopapiConfig.prevent_duplicates = options.prevent_duplicates
    if options.format is not None:
        ItopapiConfig.format = options.format
