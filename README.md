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
                    [--classes [ITOP-CLASS [ITOP-CLASS ...]]]
                    [--find INSTANCE [INSTANCE ...]] [--delete INSTANCE INSTANCE]
                    [--organization ORGANIZATION] [--import URI] [--format FORMAT]
    
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
      --classes [ITOP-CLASS [ITOP-CLASS ...]]
                            iTop classes to use
      --find INSTANCE [INSTANCE ...]
                            Find and display information about a given class
                            instance givenits name or ID
      --delete INSTANCE INSTANCE
                            Delete an instance given its class name and instance
                            ID
      --organization ORGANIZATION
                            iTop organization to use
    
    import:
      --import URI          URI of file to import
      --format FORMAT       Format of file you want import
