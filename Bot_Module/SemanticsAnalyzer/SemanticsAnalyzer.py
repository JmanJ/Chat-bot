# -*- coding: utf-8 -*-
from Bot_Module.WayAnalyzer.WayAnalyzer import WayAnalyzer
from TemplateEngine import TemplateEngine
from Templates import templates
from ManaginProcessing import ManaginProcessing
from SemanticNodes import *


class SemanticsAnalyzer():
    def __init__(self):
        self.sentence = None
        self.node_list = []
        self.node_set = set()
        self.nodes_for_deleting = set()
        self.template_engine = None
        self.way_analyzer = WayAnalyzer()

    def parse_sentence(self, sentence):
        self.sentence = sentence
        self.node_list = self.get_semantic_nodes()
        self.deleting_same_nodes()
        #ManaginProcessing.process_sentence(sentence, self.node_list)
        self.way_analyzer.processing_nodes(list(self.node_set))
        for node in self.node_list:
            if str(node.__class__.__name__) in self.node_set:
                print str(node.__class__.__name__) + ' :'
                for word_groups in node.words:
                    print '---'
                    for word in word_groups:
                        print word.get_word()

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


