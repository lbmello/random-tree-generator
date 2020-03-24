"""Modulo Root."""

from datetime import datetime
from random import randint
import hashlib
import os

from ..queue import FolderQueue
from ..data import YamlReader

class Root(object):
    """Gerencia o diretório onde a árvore será gerada."""

    # Configuracoes lidas do arquivo YAML
    path = YamlReader.path
    levels = YamlReader.levels
    size = YamlReader.size
    debug = YamlReader.debug

    def __init__(self):
        self.path = Root.path

        try:
            os.mkdir(self.path)
            if Root.debug == True:
                print(f'Diretorio Raiz criado em {self.path}')
        
        except FileExistsError:
            if Root.debug == True:
                print('Diretorio Raiz ja criado!')


    @classmethod
    def add_existing_subdir_to_queue(cls):
        """Se a fila estiver vazia, percorre o diretorio atual e adiciona subpastas na fila."""

        if FolderQueue.is_empty():
            for dirpath, _, _ in os.walk(top=cls.path, topdown=True):
                FolderQueue.fila.push(dirpath)

    @classmethod
    def n_file_elements(cls):
        """Retorna algum inteiro randomico entre 1 e 3*{size} para gerar arquivos."""
        
        return randint(1, (3 * Root.size))

    @classmethod
    def n_folder_elements(cls):
        """Retorna algum inteiro randomico entre 1 e 2*{size} para gerar pastas."""
        
        return randint(1, (2 * Root.size))

    @classmethod
    def random_value(cls):
        """Retorna string com uma hash MD5 aleatoria, gerada a partir da hora atual, multiplicado por um valor de 1 a 1000000."""

        #TODO: Refatorar seguinte altaracao de valores!
        random_value = datetime.now()
        random_value = str(random_value)
        random_value = random_value.replace('-','').replace(':','').replace(' ','').replace('.','')
        random_value = random_value * (randint(0, 1000000))
        random_value = bytes(random_value, encoding='utf8')

        obj = hashlib.md5()
        obj.update(random_value)

        return obj.hexdigest()