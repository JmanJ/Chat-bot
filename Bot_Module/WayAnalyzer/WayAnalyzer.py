# -*- coding: utf-8 -*-
import os
from Bot_Module.AnswerAnalyzer.AnswerConstructer import AnswerConstructer
from Combination import *


class WayAnalyzer():
    def __init__(self, morph_module, memory):
        self.memory = memory
        self.answer_analywer = AnswerConstructer(morph_module, memory)
        #spisok kortejei iz 2yh kombinacii
        self.variants = []
        self.upload_variants()

    def upload_variants(self):
        print os.path.abspath(os.curdir)
        variants_file = open("Variants", 'r')
        for line in variants_file:
            variant = line.split('=')
            self.variants.append((self._construct_combination(variant[0]), self._construct_combination(variant[1])))

    def _construct_combination(self, combination_string):
        comb_r = combination_string.split(' ')
        comb_nr = []
        params_list = []
        for index, node_name in enumerate(comb_r):
                if node_name[-1] == '*':
                    node_name = node_name[:-1]
                    comb_nr.append(node_name)
                node_name, params = self._parse_params(node_name)
                comb_r[index] = node_name
                params_list.append(params)
        return Combination(comb_r, params_list, comb_nr)

    def _parse_params(self, node_string):
        if "<" in node_string:
            node_name = node_string.split('<')[0]
            params = []
            params_str = node_string.split('<')[1].split('>')[0]
            param_str_list = params_str.split(';')
            for param_str in param_str_list:
                param_name = param_str.split(':')[0]
                param_values = param_str.split(':')[1].split(',')
                params.append((param_name, param_values))
            return node_name, params
        else:
            return node_string, []

    def processing_nodes(self, combination):
        relevant_variants = []
        for variant in self.variants:
            if self.compare_combination(combination, variant[0]):
                relevant_variants.append(variant[1])
        self.answer_analywer.construct_answer(relevant_variants)

    def compare_combination(self, comb1, comb2):
        isCorrect = True
        #TODO empty list in comb1
        for index1, node in enumerate(comb1.required_nodes):
            if not node in comb2.required_nodes:
                isCorrect = False
                break
            else:
                index2 = comb2.required_nodes.index(node)
                if comb2.params[index2]:
                    self.compare_params(comb1.params[index1], comb2.params[index2])
        return isCorrect

    def compare_params(self, params1, params2):
        pass
