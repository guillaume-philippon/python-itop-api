# -*- coding: utf8 -*-fr


class ConsoleView(object):
    def __init__(self):
        pass

    def display(self, data):
        print '*************\n' \
              'Hostname:     {hostname}\n' \
              'IP:           {ip}\n' \
              'CPUS:         {cpu}\n' \
              'RAM:          {ram}\n' \
              'Organization: {organization}\n' \
              'Serial:       {serial}\n' \
              '*************\n'.format(**data)