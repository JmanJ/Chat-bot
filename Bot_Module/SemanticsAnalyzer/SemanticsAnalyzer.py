# -*- coding: utf-8 -*-
from Bot_Module.WayAnalyzer.WayAnalyzer import WayAnalyzer
from Bot_Module.WayAnalyzer.Combination import Combination
from Bot_Module.DataStore.Memory import Memory
from TemplateEngine import TemplateEngine
from Templates import templates
from ManaginProcessing import ManaginProcessing
from SemanticNodes import *


class SemanticsAnalyzer():
    def __init__(self, morph_module):
        self.sentence = None
        self.node_list = []
        self.node_set = set()
        self.nodes_for_deleting = set()
        self.template_engine = None
        self.memory = Memory()
        self.manager = ManaginProcessing(self.memory)
        self.way_analyzer = WayAnalyzer(morph_module, self.memory)

    def parse_sentence(self, sentence):
        self.sentence = sentence
        self.node_list = self.get_semantic_nodes()
        self.deleting_same_nodes()
        #ManaginProcessing.process_sentence(sentence, self.node_list)
        self.way_analyzer.processing_nodes(Combination(list(self.node_set), self.get_params_list(self.node_list)))
        for node in self.node_list:
            if str(node.__class__.__name__) in self.node_set:
                print str(node.__class__.__name__) + ' :'
                for word_groups in node.words:
                    print '---'
                    for word in word_groups:
                        print word.get_word()
                        if node.type == "scale":
                            print word.repr

    def get_params_list(self, node_list):
        params_list = []
        for node in node_list:
            if node.type == "scale":
                params_list.append(("repr", node.words[0][0].repr))
            else:
                params_list.append([])

    def get_semantic_nodes(self):
        self.template_engine = TemplateEngine(self.sentence)
        self.node_set = set()
        for template in templates:
            node = self.template_engine.parse(template)
            if node:
                self.node_set.add(node)
        return self.template_engine.get_node_list()

    def deleting_same_nodes(self):
        self.nodes_for_deleting = set()
        for node in self.node_list:
            self.delete_parrent_nodes(node)
        self.node_set -= self.nodes_for_deleting

    def delete_parrent_nodes(self, node):
        for p_nodes in node.parent_nodes:
            self.nodes_for_deleting.update(self.node_set & set(p_nodes))


