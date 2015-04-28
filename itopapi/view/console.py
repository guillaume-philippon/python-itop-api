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

    def display(self, data):
        """
        Display information
        :param data: data to display
        """
        if isinstance(data, list):
            for item in data:
                if item is not None:
                    print item
        # else:
        #     print data
