"""This module contains a class for tournament parent selection."""
from typing import Union
from numpy import ndarray
from .parent_selector import ABCParentSelector


class TournamentSelector(ABCParentSelector):
    """A class for performing tournament parent selection."""

    def select(self, population: Union[list, ndarray]):
        """
        Select a subset from the population.

        Args:
            population: the list of Chromosomes to select from
        """
        # call super to check the super parameters
        super(TournamentSelector, self).select(population)

# explicitly export classes
__all__ = [
    'TournamentSelector'
]
