# -*- coding: utf-8 -*-
from Bot_Module.DataStore.Memory import Memory


class ManaginProcessing():
    def __init__(self, memory):
        self.memory = memory
        self.deixis_list = []
        self.uploading_memory()

    def uploading_memory(self):
        pass

    def process_sentence(self, sentence, node_list):
        pass

    def add_new_deixis(self, combination, obj):
        self.deixis_list.append((combination, obj))