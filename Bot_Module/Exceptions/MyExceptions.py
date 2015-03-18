# -*- coding: utf-8 -*-


class MyException(Exception):
    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        return self.msg


class NoTemplates(MyException):
    def __init__(self):
        self.msg = "Отсутствуют шаблоны для данного семантического гнезда"


class RoleNotDefine(MyException):
    def __init__(self):
        self.msg = "Роль говорящего не определена"


class IncorrectObjectName(MyException):
    def __init__(self):
        self.msg = "Имя объекта не найдено"


class CantConstruct(MyException):
    def __init__(self, node_name):
        self.msg = "Не возможно сконструировать семантическое гнездо:" + node_name


class IncorrectNode(MyException):
    def __init__(self, node_name):
        self.msg = "Обнаружено не известное семантическое гнездо: " + node_name