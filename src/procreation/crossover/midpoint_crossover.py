"""This module contains the midpoint crossover procreator class."""
from .crossover_procreator import CrossoverProcreatorABC


class MidpointCrossoverProcreator(CrossoverProcreatorABC):
    """This class performs midpoint crossover on realcoded parents."""


# explicitly specify exports
__all__ = [
    'MidpointCrossoverProcreator'
]
