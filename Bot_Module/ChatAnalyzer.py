# -*- coding: utf-8 -*-
from Bot_Module.WordAnalyzer.WordsAnalyzer import WordsAnalyzer

import pymorphy2


class ChatAnalyzer():
    def __init__(self):
        self.morph = pymorphy2.MorphAnalyzer()
        self.words_analysis = WordsAnalyzer(self.morph)

    def message_processing(self, text):
        self.words_analysis.processing(text)

    #DOTO history uploading, preservation
    #DOTO time to answer
