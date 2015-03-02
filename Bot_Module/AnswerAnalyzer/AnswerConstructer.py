# -*- coding: utf-8 -*-
from Bot_Module.SemanticsAnalyzer.Templates import templates
from Bot_Module.SemanticsAnalyzer.Randomizer import Randomizer
from Bot_Module.Exceptions.MyExceptions import *


class AnswerConstructer():
    def __init__(self):
        self.result_string = ''
        self.node_list = []

    def construct_answer(self, combinations):
        #list of combinations for constructing answer
        self.result_string = ''
        self.node_list = []
        for combination in combinations:
            body_list = []
            semantics_node = [None] * len(combination.required_nodes)
            for template in templates:
                if template['SemanticNode'].__name__ in combination.required_nodes:
                    index = combination.required_nodes.index(template['SemanticNode'].__name__)
                    if not semantics_node[index]:
                        semantics_node[index] = template['SemanticNode']()
                        semantics_node[index].body_list = []
                    semantics_node[index].body_list.append(template['body'])
            for semantic_node in semantics_node:
                if not semantic_node.body_list:
                    raise NoTemplates()
                self.node_list.append(self.construct_body(Randomizer.get_random_item(semantic_node.body_list, True),
                                                          semantic_node))
        print '--ОТВЕТ->'
        for node in self.node_list:
            for word_groups in node.words:
                for word in word_groups:
                    print word
        print '<-ОТВЕТ--'

    def construct_body(self, body, semantic_node):
        for group in body:
            semantic_node.add_word_list(self.construct_group(group))
        return semantic_node

    def construct_group(self, group):
        words = []
        for word in group:
            w = self.construct_word(word['kwords'])
            #DOTO isRequired
            #DOTO morf lexems
            if w:
                words.append(w)
        return words

    def construct_word(self, words):
        return Randomizer.get_random_item(words)