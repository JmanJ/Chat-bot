# -*- coding: utf-8 -*-

from Bot_Module.SemanticsAnalyzer.SemanticsAnalyzer import SemanticsAnalyzer
from SentenceInfo import SentenceInfo
from WordInfo import WordInfo
from IncorrectMessage import IncorrectMessage

#DOTO add a check in the dictionary
#DOTO delete and replace words
#DOTO processing score


class WordsAnalyzer():
    def __init__(self, morph_module):
        self.morph = morph_module
        self.semantics_analyzer = SemanticsAnalyzer(morph_module)
        self.sentence = None
        self.sentences = []

    def processing(self, text):
        self.sentence = SentenceInfo()
        self.sentences = []
        self.sentence = SentenceInfo()
        words = filter(None, text.split(' '))
        for word in words:
            w = self.word_processing(word)
            for cur_word in w:
                if cur_word.get_word in (".", "?", "!"):
                    self.sentences.append(self.sentence)
                    self.sentence = SentenceInfo()
                self.sentence.add_word(cur_word)
        print self.sentence
        self.sentences.append(self.sentence)
        #DOTO analysis any number of sentences
        self.semantics_analyzer.parse_sentence(self.sentences[0])

    def word_processing(self, word):
        #print type(word.encode("utf-8"))
        word = word.lower()
        text_info = self.morph.parse(word)[0]
        if "UNKN" in text_info.tag:
            #DOTO digital
            character = ''
            for character in word:
                if not u"а" <= character <= u"я" or u"А" <= character <= u"Я":
                    if character == '?':
                        self.sentence.add_flag("Question")
                    break
            new_words = filter(None, word.split(character))
            new_words.insert(1, character)
            words_list = []
            for w in new_words:
                text_info = self.morph.parse(w)[0]
                if "UNKN" in text_info.tag:
                    raise IncorrectMessage()
                words_list.append(WordInfo(text_info))
            return words_list
        else:
            return [WordInfo(text_info)]

    def replace_characters(self):
        pass
