# -*- coding: utf-8 -*-
from MyObject import MyObject


class Connection(MyObject):
    def __init__(self, obj_tuple):
        MyObject.__init__(self)
        self.put("conn", obj_tuple)