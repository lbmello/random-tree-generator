"""Modulo files."""

from pathlib import Path

from ..queue import FolderQueue
from ..root import Root
from ..folder import Folder


class Files():
    """Responsavel por criar os arquivos nos diretorios e subdiretorios."""

    def __init__(self):
        self.path = Folder.path

    @classmethod
    def gen_files(cls, n_files):
        """Gera n{n_files} arquivos no diretorio informado em {path} e retorna lista com nomes dos arquivos."""
        
        if not FolderQueue.is_empty():
            folder = FolderQueue.fila.pop()

            for _ in range(n_files):
                file_name = Root.random_value()
                Path(f'{folder}/{file_name}').touch()

    @classmethod
    def create_queue_files(cls):
        """Limpa a fila e cria os arquivos."""

        if Root.debug == True:
            print('Criando arquivos!')

        if not FolderQueue.is_empty():
            for _ in range(FolderQueue.fila.len()):                
                cls.gen_files(n_files=Root.n_file_elements())
