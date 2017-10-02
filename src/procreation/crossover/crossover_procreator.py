"""This module contains the crossover procreator abstract base class."""
from typing import List, Union
from abc import abstractmethod
from numpy import ndarray
from src.population import Chromosome


class CrossoverProcreatorABC:
    """This class is an abstract base class for crossover procreators."""

    @abstractmethod
    def procreate(self, parents: Union[List[Chromosome], ndarray]) -> List[Chromosome]:
        """
        Create children from a collection of parents.

        Args:
            parents: the list of parents to select from

        Returns: a list of children from the parents (1 child for each parent)
        """
        # make sure the parents collection is the right type
        if not isinstance(parents, (list, ndarray)):
            raise TypeError('parents should be in datastructure: list, ndarray')
        # verify that there are at least 2 parents
        if len(parents) < 2:
            raise ValueError('crossovers must have at least 2 parents')
        # return the input, this is abstract
        return parents


# explicitly specify exports
__all__ = [
    'CrossoverProcreatorABC'
]
