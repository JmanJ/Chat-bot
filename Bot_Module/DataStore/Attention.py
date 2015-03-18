# -*- coding: utf-8 -*-


class Attention():
    def __init__(self, size):
        self._time_list = []
        self.size = size

    def add_to_attention(self, obj):
        self._time_list.insert(0, obj)
        if not len(self._time_list) < self.size:
            self._time_list.remove(len(self._time_list)-1)

    def get_attention_list(self):
        return self._time_list