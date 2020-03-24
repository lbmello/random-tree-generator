"""Modulo Tree."""

import os

class Tree:
    """Gera a lista de pastas, semelhante ao comando tree do linux."""

    def __init__(self):
        self.tree = []

    def get_tree(self, path):
        """ Retorna a lista das pastas."""

        for root, _, _ in os.walk(top=path, topdown=True):              
            self.tree.append(f'{root}')
        return self.tree
