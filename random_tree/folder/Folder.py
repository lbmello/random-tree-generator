"""Modulo Folder."""

import os

from ..root import Root
from ..queue import FolderQueue
from ..tree import Tree

class Folder(Root):
    """Responsavel por criar os diretorios e subdiretorios."""
    
    def __init__(self):
        self.path = Root.path  

    def create_branch(self):
        """Cria o path completo dos galhos e os adiciona na fila."""

        begin_folders = Folder.gen_folder_name(path=self.path, n_folders=Root.n_folder_elements())

        for branch in begin_folders:
            for _ in range(Root.levels):
                branch = f'{branch}/{Root.random_value()}'

            FolderQueue.fila.push(branch)
    
    def tree_to_queue(self):
        """Roda um tree e adiciona todas as pastas na fila."""

        tree = Tree().get_tree(path=self.path)

        for folder in tree:
            FolderQueue.fila.push(folder)
    
    @classmethod
    def create_queue_folders(cls):
        """Limpa a fila e cria as pastas."""

        if Root.debug == True:
            print('Criando pastas!')

        for _ in range(FolderQueue.fila.len()):
            folder = FolderQueue.fila.pop()
            
            os.makedirs(folder)

    @classmethod
    def create_queue_subfolders(cls):
        """Limpa a fila e cria as subpastas."""

        if Root.debug == True:
            print('Criando subpastas!')

        for _ in range(FolderQueue.fila.len()):
            folder = FolderQueue.fila.pop()
            subfolder = Root.random_value()

            os.makedirs(f'{folder}/{subfolder}')

    @classmethod
    def gen_folder_name(cls, path=str, n_folders=int):    
        """Gera n{n_folders} de nomes para pasta e retorna lista com nomes das pastas."""
        
        folders_name = []

        for _ in range(n_folders):
            dir_name = Root.random_value()

            folders_name.append(f'{Folder.path}/{dir_name}')

        return folders_name