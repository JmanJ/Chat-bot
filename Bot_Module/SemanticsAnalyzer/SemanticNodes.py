# -*- coding: utf-8 -*-


#bugs
#выходите из машины это не Planning
#быть иметь


class SemanticNode():
    parent_nodes = []

    def __init__(self, words=None, chance=0):
        self.chance = chance
        if words:
            self.words = [words]
        else:
            self.words = []

    def add_word_list(self, word_list):
        self.words.append(word_list)

#---Манерные гнезда


class Greeting(SemanticNode):
    """Присутствуют приветствующие конструкции языка"""


class Farewell(SemanticNode):
    """Присутствуют конструкции языка употребляющиеся при завершении беседы"""


#---Гнезда с глаголами


class Narrative(SemanticNode):
    """Повествование о некотором действие, наличие глагола несовершенного вида в изъявительном наклонении"""


class Desire(SemanticNode):
    """Желание что-либо, хочу, требую, желаю; время не учитывается
    Наличие определенных глаголов несовершенного вида в изъявительном наклонении"""
    parent_nodes = [["Narrative"], ]


class Request(SemanticNode):
    """Прошение о чем-либо"""
    parent_nodes = [["Desire"], ]


class Recommendation(SemanticNode):
    """Рекомендация сделать что-то,  наличие глагола несовершенного вида в повелительном наклонении"""


class Confession(SemanticNode):
    """Признание в некотором действие, наличие глагола совершенного вида в изъявительном наклонении, прош. времени"""


class Planning(SemanticNode):
    """Планирвоание сделать что-то, наличие глагола совершенного вида в изъявительном наклонении будущего времени"""


class Order(SemanticNode):
    """Приказание сделать, наличие глаголов совершенного вида в повелительном наклонении,говорящий включен в действие"""


class Offer(SemanticNode):
    """Предложение сделать что-то вместе, наличие глаголов совершенного вида в повелительном наклонении,
        говорящий не включен в действие"""


class Action(SemanticNode):
    """Действие, глагол в инфинитиве"""


#---Гнезда с существительными
#Какие планы на будущее?


#---Гнезда с местоимениями
#себе сам, я сам, он себя

class Myself(SemanticNode):
    """Говорит о себе"""


class Yourself(SemanticNode):
    """Говорит о собеседнике"""


class Themself(SemanticNode):
    """Говорит о 3ем лице"""


class Himself(SemanticNode):
    """Присутствует конструкция сам себе."""


class FullyUsed(SemanticNode):
    """Наличие местоимения весь. Указывает на то, что объект был полностью использован"""


#---Гнезда с частицами


class Thinking(SemanticNode):
    """Сделал бы что-то, возможно, присутствуют частицы бы, ли, же"""


#---Гнезда смешанные


class Agression(SemanticNode):
    """Присутствуют прилагательные с негативным значением"""


class Goodwill(SemanticNode):
    """Присутствуют прилагательные с положительным значением"""


class Approval(SemanticNode):
    """Согласие, подтверждение"""


#---Гнезда пунктуации


class Question(SemanticNode):
    """Присутствует знак вопроса"""

