# -*- coding: utf-8 -*-
from Bot_Module.Exceptions.MyExceptions import *
from Conversation import Conversation
from MyObject import MyObject
from Attention import Attention
from Connection import Connection


class Memory():
    def __init__(self, roles=["Я", "Собеседник"]):
        self.roles = roles
        self.convers = Conversation(self.roles)
        self.short_attention = Attention(2)
        self.role_attention = 0
        self.objects_list = []
        self.connections_list = []
        self.connection_cache = []  # tuple = number in connections_lists

    def new_object(self, name):
        obj = MyObject()
        obj.put("name", name)
        self.objects_list.append(obj)

    def new_connection(self, obj_names):
        self.connections_list.append(Connection((self.get_object_by_name(obj_names[0]),
                                                 self.get_object_by_name(obj_names[1]))))

    def add_object_attr(self, obj_name, attr_name, value):
        self.get_object_by_name(obj_name).put(attr_name, value)

    def add_connection_attr(self, obj_names, attr_name, value):
        #self.get_object_by_name(obj_names[0])
        pass

    def get_object_attr(self, obj_name, attr_name):
        self.get_object_by_name(obj_name).get(attr_name)

    def get_connection_attr(self, obj_names, attr_name):
        pass

    def get_object_by_name(self, obj_name):
        for obj in self.objects_list:
            if obj.name == obj_name:
                return obj
        else:
            raise IncorrectObjectName()