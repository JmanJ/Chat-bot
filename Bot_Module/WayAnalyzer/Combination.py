# -*- coding: utf-8 -*-


class Combination():
    def __init__(self, required_nodes, params, n_required_nodes=None):
        self.required_nodes = required_nodes
        self.n_required_nodes = n_required_nodes
        self.params = params   # [(name, values), ]