# -*- coding: utf-8 -*-


class WordInfo():
    def __init__(self, text_info):
        self.info = text_info
        self.flags = []

    def add_flag(self, flag):
        self.flags.append(flag)

    def get_word(self):
        return self.info.word.encode("utf-8")

    def get_lexemes(self):
        return self.info.tag

    def get_normal_form(self):
        return self.info.normal_form.encode("utf-8")

    def get_score(self):
        return self.info.score

    def __str__(self):
        s = str.format("Слово: {0}\nЛексемы: {1}\nНормальная форма: {2}\nВероятность: {3}",
                            self.info.word.encode("utf-8"),
                            self.info.tag,
                            self.info.normal_form.encode("utf-8"),
                            self.info.score)
        return s