"""This module contains the binary mutation procreator class."""
from .mutation_procreator import MutationProcreatorABC


class BinaryMutationProcreator(MutationProcreatorABC):
    """This class performs binary mutation on parents."""


# explicitly specify exports
__all__ = [
    'BinaryMutationProcreator'
]
