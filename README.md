# python-itop-api
Python API for iTop connecting to it through the REST interface

## itop-cli
itop-cli is a CLI (command line interface) to iTop REST interface. You can use it to list the content
of iTop instances of a particular class with the command

    user@machine> itop-cli --classes server rack
   
You can also search some specific instance with option --find

    user@machine> itop-cli --classes server --find host.domain.com
    
You can have a look of more option with command --help

    user@machine> itop-cli --help

    usage: itop-cli [-h] [--hostname HOSTNAME] [--username USERNAME]
                    [--password PASSWORD] [--organization ORGANIZATION-NAME]
                    [--virtualhost VIRTUAL-HOSTNAME] [--config CONFIG_FILE]
                    [--classes [ITOP-CLASS [ITOP-CLASS ...]]]
                    [--find INSTANCE [INSTANCE ...]] [--delete]
                    [--set SET_FIELDS SET_FIELDS] [--import-uri URI]
                    [--import-stdin] [--format FORMAT] [--save]
                    [--prevent-duplicates]

    python CLI for iTop REST api

    optional arguments:
      -h, --help            show this help message and exit

    itop:
      --hostname HOSTNAME   hostname of iTop server
      --username USERNAME   username for iTop authentication
      --password PASSWORD   password for iTop authentication
      --organization ORGANIZATION-NAME
                            iTop organization to use
      --virtualhost VIRTUAL-HOSTNAME
                            Itop's virtual host name for VMs

    cli:
      --config CONFIG_FILE  configuration file CLI must use (default = ./itop-
                            cli.cfg)
      --classes [ITOP-CLASS [ITOP-CLASS ...]]
                            iTop classes to use
      --find INSTANCE [INSTANCE ...]
                            Find and display information about a given class
                            instance givenits name or ID
      --delete              Delete all instances previously loaded
      --set SET_FIELDS SET_FIELDS
      --save                Save the instances loaded through import
      --prevent-duplicates  Check if objects with the same name already exist
                            before savingand don't save in this case

    import:
      --import-uri URI      URI of file to import
      --import-stdin        import data from STDIN
      --format FORMAT       Format of file you want import
