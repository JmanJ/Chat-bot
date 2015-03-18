# -*- coding: utf-8 -*-
from SemanticNodes import *


class TemplateEngine():
    """Сравнивает предложение с шаблоном. Возвращает имя семантического гнезда если шаблон распознан.
    Получить сформированный список с объектами распознанных гнезд с помощью метода get_node_list()"""

    def __init__(self, sentence):
        self.sentence = sentence
        self.template = {}
        self.node_list = []
        self.recognized_words = []

    def parse(self, template):
        self.template = template
        flag = False
        index = 0
        self.recognized_words = []
        while index != -1:
            index = self.parse_body(self.template["body"], index)
            if index != -1:
                flag = True
        #wablon raspoznan
        if flag:
            #node_list = list(self.node_set)
            for node in self.node_list:
                #takoi yje est' v spiske
                if isinstance(node, self.template["SemanticNode"]):
                    node.words.append(self.recognized_words)
                    node.chance = node.chance + self.template["chance"]
                    return None
            semantic_node = self.template["SemanticNode"](self.recognized_words, self.template["chance"])
            semantic_node.type = self.template["type"]
            self.node_list.append(semantic_node)
            return self.template["SemanticNode"].__name__
        return None

    def parse_body(self, template_body, start_word_index):
        #ordered = False
        for group in template_body:
            start_word_index = self.parse_group(group, start_word_index)
            #Ne ydalos' naiti neobhodimie konstrykcii
            if start_word_index == -1:
                break

        return start_word_index

    def parse_group(self, template_group, start_word_index):
        real_start_word_index = start_word_index
        current_start_word_index = -1
        flag = False
        for words_group in template_group:
            current_start_word_index = self.parse_word(words_group, start_word_index)
            if current_start_word_index > real_start_word_index:
                #nawel slovo
                break
        if current_start_word_index != -1:
            return current_start_word_index
        else:
            return -1

    def parse_word(self, words_group, start_word_index):
        if start_word_index < len(self.sentence.words):
            end_word_index = len(self.sentence.words)
            for sentence_word in self.sentence.words[start_word_index:end_word_index]:
                f_word = 0
                f_lexem = 0
                for word in words_group["kwords"]:
                    f_word = 1
                    #Slovo naideno, vozvrawaem sledyuwii nomer slova
                    if word == sentence_word.get_normal_form():
                        f_word = 2
                        break
                for lexem in words_group["lexems"]:
                    f_lexem = 1
                    if set(lexem.split(",")) in sentence_word.get_lexemes():
                        f_lexem = 2
                        break
                if f_word != 1 and f_lexem != 1:
                    if "repr" in words_group:
                        sentence_word.repr = words_group["repr"]
                    if "value" in words_group:
                        sentence_word.value = words_group["value"]
                    self.recognized_words.append(sentence_word)
                    return self.sentence.words.index(sentence_word) + 1
        #Slovo ne naideno, no ono doljno bit'
        if words_group["required"]:
            return -1
        else:
            return start_word_index
        #DOTO remember

    def get_node_list(self):
        return self.node_list