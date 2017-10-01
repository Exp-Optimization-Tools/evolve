"""This module contains the n-point crossover procreator class."""
from .crossover_procreator import CrossoverProcreatorABC


class NPointCrossoverProcreator(CrossoverProcreatorABC):
    """This class performs n-point crossover parents."""


# explicitly specify exports
__all__ = [
    'NPointCrossoverProcreator'
]
