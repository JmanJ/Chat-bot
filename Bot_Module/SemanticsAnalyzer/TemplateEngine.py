# -*- coding: utf-8 -*-
from SemanticNodes import *


class TemplateEngine():
    def __init__(self, sentence, template, node_list):
        self.sentence = sentence
        self.template = template
        self.node_list = node_list
        self.recognized_words = []

    def parse(self):
        index = self.parse_body(self.template["body"])
        #wablon raspoznan
        if index > 0:
            for node in self.node_list:
                if isinstance(node, self.template["SemanticNode"]):
                    node.words.append(self.recognized_words)
                    node.chance = node.chance + self.template["chance"]
                    return self.node_list
            semantic_node = self.template["SemanticNode"](self.recognized_words, self.template["chance"])
            self.node_list.append(semantic_node)
            return self.node_list

    def parse_body(self, template_body):
        start_word_index = 0
        self.recognized_words = []
        for group in template_body:
            start_word_index = self.parse_group(group, start_word_index)
            #Ne ydalos' naiti neobhodimie konstrykcii
            if start_word_index == -1:
                break
        return start_word_index

    def parse_group(self, template_group, start_word_index):
        next_only = False
        for words_group in template_group:
            if not words_group:
                next_only = False
            start_word_index = self.parse_word(words_group, start_word_index, next_only)
            if start_word_index != -1:
                next_only = True
            else:
                break
        return start_word_index

    def parse_word(self, words_group, start_word_index, next_only):
        if start_word_index < len(self.sentence.words):
            end_word_index = len(self.sentence.words)
            if next_only:
                end_word_index = start_word_index + 1
            for sentence_word in self.sentence.words[start_word_index:end_word_index]:
                for word in words_group["kwords"]:
                    #Slovo naideno, vozvrawaem sledyuwii nomer slova
                    if word == sentence_word.get_normal_form() and set(words_group["lexems"]) in sentence_word.get_lexemes():
                        self.recognized_words.append(sentence_word)
                        return self.sentence.words.index(sentence_word) + 1
                #DOTO lexems
        #Slovo ne naideno, no ono doljno bit'
        if words_group["required"]:
            return -1
        else:
            return start_word_index
        #DOTO remember