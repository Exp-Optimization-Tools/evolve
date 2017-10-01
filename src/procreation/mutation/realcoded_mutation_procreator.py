"""This module contains the realcoded mutation procreator class."""
from .mutation_procreator import MutationProcreatorABC


class RealCodedMutationProcreator(MutationProcreatorABC):
    """This class performs realcoded mutation on parents."""


# explicitly specify exports
__all__ = [
    'RealCodedMutationProcreator'
]
