# -*- coding: utf-8 -*-
from TemplateEngine import TemplateEngine
from Templates import templates


class SemanticsAnalyzer():
    def __init__(self, morph_module):
        self.morphy = morph_module
        self.node_list = []

    def parse_sentence(self, sentence):
        self.node_list = []
        for template in templates:
            TemplateEngine(sentence, template, self.node_list).parse()

        for node in self.node_list:
            print str(node.__class__.__name__) + ' :'
            for word_groups in node.words:
                print '---'
                for word in word_groups:
                    print word.get_word()