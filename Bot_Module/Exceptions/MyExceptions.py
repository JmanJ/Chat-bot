# -*- coding: utf-8 -*-


class MyException(Exception):
    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        return self.msg


class NoTemplates(MyException):
    def __init__(self):
        self.msg = "Отсутствуют шаблоны для данного семантического гнезда"