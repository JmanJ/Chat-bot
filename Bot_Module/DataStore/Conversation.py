# -*- coding: utf-8 -*-
from Bot_Module.Exceptions.MyExceptions import *


class Conversation():
    def __init__(self, roles):
        self.roles = roles
        self.history = []  #{role:message}
        self.nodes_combinations = []

    def add_message(self, role, message):
        if not role in self.roles:
            raise RoleNotDefine()
        self.history.append(dict(role=message))

    def add_combination(self, combination, index=0):
        p = index - len(self.nodes_combinations)
        while p > -1:
            self.nodes_combinations.append([])
            p -= 1
        self.nodes_combinations[index].append(combination)

    def get_cur_combinations(self, deleting=True):
        if deleting:
            return self.nodes_combinations.pop(0)
        else:
            return self.nodes_combinations[0]

