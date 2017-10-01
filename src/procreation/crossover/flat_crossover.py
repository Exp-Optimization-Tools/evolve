"""This module contains the flat crossover procreator class."""
from .crossover_procreator import CrossoverProcreatorABC


class FlatCrossoverProcreator(CrossoverProcreatorABC):
    """This class performs flat crossover on parents."""


# explicitly specify exports
__all__ = [
    'FlatCrossoverProcreator'
]
