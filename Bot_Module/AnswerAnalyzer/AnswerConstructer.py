# -*- coding: utf-8 -*-
from Bot_Module.SemanticsAnalyzer.Templates import templates
from Bot_Module.SemanticsAnalyzer.Randomizer import Randomizer
from Bot_Module.Exceptions.MyExceptions import *


class AnswerConstructer():
    def __init__(self, pymorphy, memory):
        self.pymorphy = pymorphy
        self.memory = memory
        self.result_string = ''
        self.node_list = []
        self._not_constructed = True

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
                    semantics_node[index].params = combination.params[index]
            for ind, semantic_node in enumerate(semantics_node):
                if not semantic_node:
                    raise IncorrectNode(combination.required_nodes[ind])
                if not semantic_node.body_list:
                    raise NoTemplates()
                result_node = None
                self._not_constructed = True
                while self._not_constructed:
                    self._not_constructed = False
                    random_body = Randomizer.get_random_item(semantic_node.body_list, True)
                    if not random_body:
                        raise CantConstruct(combination.required_nodes[ind])
                    result_node = self.construct_body(random_body, semantic_node)
                self.node_list.append(result_node)
        print '--ОТВЕТ->'
        for node in self.node_list:
            for word_groups in node.words:
                for word in word_groups:
                    print word
        print '<-ОТВЕТ--'

    def construct_body(self, body, semantic_node):
        for group in body:
            semantic_node.add_word_list(self.construct_group(group, semantic_node.params))
        return semantic_node

    def construct_group(self, group, params):
        #DOTO isRequired
        #DOTO morf lexems
        resut = []
        words_group = []
        if params:
            for word in group:
                for param in params:
                    for value in param[1]:
                        if word[param[0]] == int(value):
                            words_group.append(word)
        else:
            words_group = group

        w = self.construct_word(Randomizer.get_random_item(words_group))

        if w:
            resut.append(w)
        return resut

    def construct_word(self, word_group):
        words = word_group["kwords"]
        lexems = word_group["lexems"]
        #TODO Memory used
        if words:
            w = Randomizer.get_random_item(words)
            l = Randomizer.get_random_item(lexems)
            if l:
                results = self.pymorphy.parse(w.decode('utf_8'))
                for result in results:
                    result_word = result.inflect(set(l.split(',')))
                    if result_word:
                        return result_word.word
            else:
                return w
        else:
            self.construct_word_from_memory(lexems)
        self._not_constructed = True
        return None

    def construct_word_from_memory(self, lexems):
        pass