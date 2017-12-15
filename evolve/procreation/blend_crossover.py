"""This module contains the blend crossover procreator class."""
from typing import List
from numpy import ndarray
from evolve.population import Chromosome
from .procreator import Procreator


# TODO: introduce the alpha parameter. With a parameter alpha, flat crossover
# is then a special case of this with alpha = 0. it could then be removed
class BlendCrossoverProcreator(Procreator):
    """This class performs blend crossover on parents."""

    def procreate(self, parents: List[Chromosome]) -> List[Chromosome]:
        """
        Return a list of new children generated from a list of parents.

        Args:
            parents: the list of parents to select genes from

        Returns: a list of new children
        """
        super(BlendCrossoverProcreator, self).procreate(parents)
        # TODO: implement


# explicitly specify exports
__all__ = [
    'BlendCrossoverProcreator'
]
