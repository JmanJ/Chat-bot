# -*- coding: utf-8 -*-
import random


class Randomizer():
    def __init__(self):
        pass

    @staticmethod
    def get_random_item(items_list, is_deleting=False):
        if len(items_list):
            n = random.randint(0, len(items_list)-1)
            if is_deleting:
                return items_list.pop(n)
            else:
                return items_list[n]
        else:
            return None

    @staticmethod
    def get_random_bool(chanse):
        n = random.randint(0, 100)/100.
        return n <= chanse