# -*- coding: utf-8 -*-


class MyObject():
    def __init__(self):
        pass

    def put(self, name, value, importance=0):
        setattr(name, value)

    def get(self, name):
        return getattr(name)