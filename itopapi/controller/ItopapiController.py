# -*- coding: utf8 -*-fr
"""
itopacpiController is a controller for itopapi module
"""
from itopapi.view import ItopapiQuattorView, ItopapiConsoleView
from itopapi.model import ItopapiServer, ItopapiRack, ItopapiOSFamily


class UnknownItopClass(Exception):
    """
    Error raised if ItopClass is not supported
    """
    pass


class ItopapiController(object):
    """
    ItopapiController is a controller for itopapi module
    """
    def __init__(self):
        self.input_view = None
        self.output_view = ItopapiConsoleView()
        self.model = None
        self.data = {}

    def load_from_quattor(self, json_quattor):
        """
        Load from quattor profile
        :param json_quattor: uri
        """
        # TODO: Need to be redone
        self.input_view = ItopapiQuattorView(json_quattor)
        self.data['hostname'] = self.input_view.hostname
        self.data['ip'] = self.input_view.ip
        self.data['cpu'] = self.input_view.cpu
        self.data['ram'] = self.input_view.ram
        self.data['organization'] = ""
        self.data['serial'] = self.input_view.serial

    def load_all(self, itop_class):
        """
        Load all specific iTop class object
        :param itop_class: iTop class
        :return: []
        """
        self.model = ItopapiController._get_itop_class(itop_class)
        if self.model is not None:
            self.data = self.model.find_all()

    def load_one(self, itop_class, id_instance):
        """
        Looking for instance id
        :param itop_class: iTop class
        :param id_instance: id you want load
        """
        self.model = ItopapiController._get_itop_class(itop_class)
        if self.model is not None:
            if id_instance.isdigit():
                self.data = self.model.find(id_instance)
            else:
                self.data = self.model.find_by_name(id_instance)

    def delete_one(self, itop_class, id_instance):
        """
        Delete a specific id_instance
        :param itop_class: iTop class
        :param id_instance: id you want delete
        """
        # TODO: Why not just self.delete() for current objects deletion
        self.model = ItopapiController._get_itop_class(itop_class)
        if self.model is not None:
            self.data = self.model.delete(id_instance)

    def display(self):
        """
        Display with current view
        """
        self.output_view.display(self.data)

    @staticmethod
    def _get_itop_class(itop_class):
        """
        Associate the string passed as an argument to the corresponding Itop class
        Maybe move it to ItopapiPrototype someday
        :param itop_class: iTop class
        """
        if itop_class == "rack":
            return ItopapiRack
        elif itop_class == "server":
            return ItopapiServer
        elif itop_class == "osfamily":
            return ItopapiOSFamily
        else:
            raise UnknownItopClass()
