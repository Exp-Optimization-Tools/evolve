"""This module contains the abstract base class for parent selection."""
from typing import List
from abc import abstractmethod
from evolve.population_new._chromosome import Chromosome


class Selector(object):
    """An abstract base class outlining the API for parent selection"""

    def __init__(self, size: int=None, replace: bool=True) -> None:
        """
        Initialize a new abstract base parent selector.

        Args:
            size: the size of the sub population to select
            replace: whether to allow replacement when selecting
        """
        # check size. it can be: None, float, int
        if isinstance(size, (int, float)):
            if size < 0:
                raise ValueError('size must be greater than 0')
        elif size is not None:
            raise TypeError('size must be of type: int, float')
        # check replace. it can be only a bool
        if not isinstance(replace, bool):
            raise TypeError('replace must be of type boolean')
        # assign instance variables
        self.size = size
        self.replace = replace

    def __repr__(self) -> str:
        """Return a string representation of this object."""
        return '{}(size={}, replace={})'.format(*[
            self.__class__.__name__,
            self.size,
            self.replace
        ])

    @abstractmethod
    def select(self, population: List[Chromosome]) -> List[Chromosome]:
        """
        Select a subset from the population.

        Args:
            population: the list of Chromosome(s) to select from

        Returns: a list of selected Chromosome(s)
        """
        if not isinstance(population, list):
            raise TypeError('population should be one of types: list')


# explicitly export classes
__all__ = ['Selector']
