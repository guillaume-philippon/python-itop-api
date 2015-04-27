# python-itop-api
API python pour iTop via l'interface REST

## itop-cli
itop-cli is a CLI (command line interface) to iTop REST interface. We can use it to list the content
of iTop classes with the command

    user@machine> itop-cli --classes server rack
   
You can also search some specific instance with option --find

    user@machine> itop-cli --classes server --find host.domain.com
    
You can have a look of more option with command --help

    user@machine> itop-cli --help
    
    usage: itop-cli [-h] [--hostname HOSTNAME] [--username USERNAME]
                [--password PASSWORD] [--config CONFIG_FILE]
                [--classes [CLASSES [CLASSES ...]]]
                [--find FIND_INSTANCE [FIND_INSTANCE ...]]
                [--delete DELETE_INSTANCE DELETE_INSTANCE]
                [--organization ORGANIZATION]
                [--quattor-profile QUATTOR_PROFILE]

    python CLI for iTop REST api
    
    optional arguments:
      -h, --help            show this help message and exit
    
    itop:
      --hostname HOSTNAME   hostname of iTop server
      --username USERNAME   username for iTop authentication
      --password PASSWORD   password for iTop authentication
    
    cli:
      --config CONFIG_FILE  configuration file CLI must use (default = ./itop-
                            cli.cfg)
      --classes [CLASSES [CLASSES ...]]
                            iTop classes to use
      --find FIND_INSTANCE FIND_INSTANCE
                            Find and display information about a given class
                            instance given its name and ID
      --delete DELETE_INSTANCE DELETE_INSTANCE
                            Delete an instance given its class name and instance
                            ID
      --organization ORGANIZATION
                            iTop organization to use
      --quattor-profile QUATTOR_PROFILE
                        URI of quattor profile