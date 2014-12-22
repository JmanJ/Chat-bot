# -*- coding: utf-8 -*-


class SemanticNode():
    def __init__(self, words, chance):
        self.chance = chance
        self.words = [words]


class Greeting(SemanticNode):
    """Присутствуют приветствующие конструкции языка"""


class Farewell(SemanticNode):
    """Присутствуют конструкции языка употребляющиеся при завершении беседы"""

