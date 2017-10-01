"""This module contains the blend crossover procreator class."""
from .crossover_procreator import CrossoverProcreatorABC


class BlendCrossoverProcreator(CrossoverProcreatorABC):
    """This class performs blend crossover on parents."""


# explicitly specify exports
__all__ = [
    'BlendCrossoverProcreator'
]
