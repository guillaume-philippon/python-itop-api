# -*- coding: utf8 -*-fr


class ConsoleView(object):
    def __init__(self):
        pass

    def display(self, data):
        if isinstance(data, list):
            for item in data:
                print item
        else:
            print data