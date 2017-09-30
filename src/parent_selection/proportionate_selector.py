"""This module contains a class for proportionate parent selection."""
from typing import Union
from numpy import ndarray
from .parent_selector import ABCParentSelector


class ProportionateSelector(ABCParentSelector):
    """A class for performing proportionate parent selection."""

    def select(self, population: Union[list, ndarray]):
        """
        Select a subset from the population.

        Args:
            population: the list of Chromosomes to select from
        """
        # call super to check the super parameters
        super(ProportionateSelector, self).select(population)


# explicitly export classes
__all__ = [
    'ProportionateSelector'
]
