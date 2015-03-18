# -*- coding: utf-8 -*-
from Bot_Module.WordAnalyzer.WordsAnalyzer import WordsAnalyzer

import pymorphy2
import time


def howlong(f):
    def tmp(*args, **kwargs):
        t = time.time()
        res = f(*args, **kwargs)
        print "time: %f" % (time.time()-t)
        return res
    return tmp


class ChatAnalyzer():
    def __init__(self):
        self.morph = pymorphy2.MorphAnalyzer()
        self.words_analysis = WordsAnalyzer(self.morph)

    @howlong
    def message_processing(self, text):
        self.words_analysis.processing(text)

    #DOTO history uploading, preservation





