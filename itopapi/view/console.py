# -*- coding: utf8 -*-fr
# pylint: disable=too-few-public-methods
"""
Console View for itopapi
"""


class ItopapiConsoleView(object):
    """
    Define all method to manage view console
    """
    def __init__(self):
        pass

    @staticmethod
    def display(data):
        """
        Display information
        :param data: data to display
        """
        if isinstance(data, list):
            for item in data:
                if item.__class__.__name__ == "ItopapiServer":
                    ItopapiConsoleView.display_server(item)
                elif item.__class__.__name__ == "ItopapiRack":
                    ItopapiConsoleView.display_rack(item)
                else:
                    print item
        # else:
        #     print data

    @staticmethod
    def display_server(data):
        print data
        print "    Hostname: {name}\n" \
              "    Organization: {org_id_friendlyname}".format(**data.__dict__)

    @staticmethod
    def display_rack(data):
        print data
        print "    Rack name: {name}\n" \
              "    Organization: {org_id_friendlyname}".format(**data.__dict__)
