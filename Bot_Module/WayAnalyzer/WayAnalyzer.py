# -*- coding: utf-8 -*-
import os
from Bot_Module.AnswerAnalyzer.AnswerConstructer import AnswerConstructer
from Combination import Combination


class WayAnalyzer():
    def __init__(self):
        self.answer_analywer = AnswerConstructer()
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
        for index, node_name in enumerate(comb_r):
                if node_name[-1] == '*':
                    node_name = node_name[:-1]
                    comb_r[index] = node_name
                    comb_nr.append(node_name)
        return Combination(comb_r, comb_nr)

    def processing_nodes(self, nodes_list):
        relevant_variants = []
        desired_combination = Combination(nodes_list)
        for variant in self.variants:
            if self.compare_combination(desired_combination, variant[0]):
                relevant_variants.append(variant[1])
        self.answer_analywer.construct_answer(relevant_variants)

    def compare_combination(self, comb1, comb2):
        isCorrect = True
        for node in comb1.required_nodes:
            if not node in comb2.required_nodes:
                isCorrect = False
        return isCorrect
