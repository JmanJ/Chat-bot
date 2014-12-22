# -*- coding: utf-8 -*-

from WordInfo import WordInfo


class SentenceInfo():
    def __init__(self):
        self.flags = []
        self.words = []

    def add_word(self, word):
        self.words.append(word)

    def add_flag(self, flag):
        self.flags.append(flag)

    def get_word(self, index):
        return self.words[index]

    def __str__(self):
        data = ''
        for word in self.words:
            data += "Слово " + str(self.words.index(word) + 1) + '\n' + word.__str__() + '\n'
        return data