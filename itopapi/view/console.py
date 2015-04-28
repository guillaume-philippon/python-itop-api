# -*- coding: utf8 -*-fr


class ItopapiConsoleView(object):
    def __init__(self):
        pass

    def display(self, data):
        if isinstance(data, list):
            for item in data:
                if item is not None:
                    print item
        # else:
        #     print data