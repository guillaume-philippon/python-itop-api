# -*- coding: utf8 -*-fr

from itopapi.view import QuattorView, ConsoleView
from itopapi.model import ItopapiServer, ItopapiRack, ItopapiOSFamily


class UnknowItopClass(Exception):
    pass


class ItopapiController(object):
    def __init__(self, config):
        self.config = config
        self.input_view = None
        self.output_view = ConsoleView()
        self.model = None
        self.data = {}

    def load_from_quattor(self, json_quattor):
        self.input_view = QuattorView(json_quattor)
        self.data['hostname'] = self.input_view.hostname
        self.data['ip'] = self.input_view.ip
        self.data['cpu'] = self.input_view.cpu
        self.data['ram'] = self.input_view.ram
        self.data['organization'] = ""
        self.data['serial'] = self.input_view.serial

    def load_from_model(self, itop_class):
        if itop_class == 'rack':
            self.model = ItopapiRack(self.config)
        elif itop_class == 'server':
            self.model = ItopapiServer(self.config)
        elif itop_class == 'osfamily':
            self.model = ItopapiOSFamily(self.config)
        else:
            raise UnknowItopClass()
        if self.model is not None:
            self.model.load('grid01.lal.in2p3.fr')
            self.data = self.model.dict()

    def display(self):
        self.output_view.display(self.data)