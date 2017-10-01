"""This module contains the unform crossover procreator class."""
from .crossover_procreator import CrossoverProcreatorABC


class UniformCrossoverProcreator(CrossoverProcreatorABC):
    """This class performs uniform crossover on parents."""


# explicitly specify exports
__all__ = [
    'UniformCrossoverProcreator'
]
