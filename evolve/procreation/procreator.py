"""This module contains the procreator base class."""
from typing import List, Union
from abc import abstractmethod
from numpy import ndarray
from evolve.population import Chromosome


class Procreator:
    """A base class for procreators."""

    def __repr__(self):
        """Return a string representation of this object."""
        return f'{self.__class__.__name__}()'

    @abstractmethod
    def procreate(self, parents: Union[List[Chromosome], ndarray]) -> List[Chromosome]:
        """
        Return a list of new children generated from a list of parents.

        Args:
            parents: the list of parents to select genes from

        Returns: a list of new children
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
    'Procreator'
]
