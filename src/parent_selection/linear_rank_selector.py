"""This module contains a class for linear rank parent selection."""
from typing import Union
from numpy import ndarray
from .parent_selector import ABCParentSelector


class LinearRankSelector(ABCParentSelector):
    """A class for performing linear rank parent selection."""

    def select(self, population: Union[list, ndarray]):
        """
        Select a subset from the population.

        Args:
            population: the list of Chromosomes to select from
        """
        # call super to check the super parameters
        super(LinearRankSelector, self).select(population)

# explicitly export classes
__all__ = [
    'LinearRankSelector'
]
