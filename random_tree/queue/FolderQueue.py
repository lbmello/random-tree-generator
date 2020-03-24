"""Modulo FolderQueue."""

from .queue import Queue


class FolderQueue():
    """ Instancia de fila para gerenciar o ponteiro dos diretorios."""

    fila = Queue()
    
    @classmethod
    def is_empty(cls):
        """Retorna se a fila está vazia."""
        if cls.fila.len() == 0:
            return True
        else:
            return False
