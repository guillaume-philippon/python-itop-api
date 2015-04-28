# -*- coding: utf8 -*-fr

from itopapi.view import ItopapiQuattorView, ItopapiConsoleView
from itopapi.model import ItopapiServer, ItopapiRack, ItopapiOSFamily


class UnknownItopClass(Exception):
    pass


class ItopapiController(object):
    def __init__(self):
        self.input_view = None
        self.output_view = ItopapiConsoleView()
        self.model = None
        self.data = {}

    def load_from_quattor(self, json_quattor):
        self.input_view = ItopapiQuattorView(json_quattor)
        self.data['hostname'] = self.input_view.hostname
        self.data['ip'] = self.input_view.ip
        self.data['cpu'] = self.input_view.cpu
        self.data['ram'] = self.input_view.ram
        self.data['organization'] = ""
        self.data['serial'] = self.input_view.serial

    def load_all(self, itop_class):
        self.model = ItopapiController._get_itop_class(itop_class)
        if self.model is not None:
            self.data = self.model.find_all()

    def load_one(self, itop_class, id):
        self.model = ItopapiController._get_itop_class(itop_class)
        if self.model is not None:
            if id.isdigit():
                self.data = self.model.find(id)
            else:
                self.data = self.model.find_by_name(id)

    def delete_one(self, itop_class, id):
        self.model = ItopapiController._get_itop_class(itop_class)
        if self.model is not None:
            self.data = self.model.delete(id)

    def display(self):
        self.output_view.display(self.data)

    @staticmethod
    def _get_itop_class(itop_class):
        """
        Associate the string passed as an argument to the corresponding Itop class
        Maybe move it to ItopapiPrototype someday
        """
        if itop_class == "rack":
            return ItopapiRack
        elif itop_class == "server":
            return ItopapiServer
        elif itop_class == "osfamily":
            return ItopapiOSFamily
        else:
            raise UnknownItopClass()