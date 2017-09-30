"""This module contains the abstract base class for parent selection."""
import abc
from typing import Union
from numpy import ndarray


class ABCParentSelector:
    """An abstract base class outlining the API for parent selection"""

    @abc.abstractmethod
    def select(self, population: Union[list, ndarray]):
        """
        Select a subset from the population.

        Args:
            population: the list of Chromosomes to select from
        """
        if not isinstance(population, (list, ndarray)):
            raise TypeError('population should be one of type: array, list')


# explicitly export classes
__all__ = [
    'ABCParentSelector'
]
