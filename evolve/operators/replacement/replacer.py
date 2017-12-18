"""A module containing the replacer abstract base class."""
from typing import Union, List
from numpy import ndarray
from abc import abstractmethod
from evolve.population_new._chromosome import Chromosome


class Replacer(object):
    """An abstract base class for survivor replacer."""

    def __repr__(self):
        """Return a string representation of this object."""
        return '{}()'.format(self.__class__.__name__)

    @abstractmethod
    def select(self,
               population: Union[List[Chromosome], ndarray],
               parents: Union[List[Chromosome], ndarray],
               children: Union[List[Chromosome], ndarray]) -> List[Chromosome]:
        """Return a population with the children replacing the parents.

        Args:
            population: the population to mutate
            parents: the population of parents that were selected
            children: the population of children that were generated

        Returns: A population with the some distribution of replacement
        """
        if not isinstance(population, list):
            raise TypeError('population must be of type: list')
        if not isinstance(parents, list):
            raise TypeError('parents must be of type: list')
        if not isinstance(children, list):
            raise TypeError('children must be of type: list')


# explicitly specify exports
__all__ = [
    'Replacer'
]
