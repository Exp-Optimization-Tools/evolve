"""
This module contains a class for tournament parent selection.

*   selection pressure increases and decreases with k
"""
from typing import Union
from numpy import ndarray, random
from .parent_selector import ABCParentSelector


class TournamentSelector(ABCParentSelector):
    """A class for performing tournament parent selection."""

    def select(self,
               population: Union[list, ndarray],
               k: int = 1,
               size: int = None,
               replace: bool = True):
        """
        Select a subset from the population.

        Args:
            population: the list of Chromosomes to select from
            k: the size of the random subset to select the best individuals
               from (default 1)
            size: the size of the array to return if any (default None)
            replace: whether replacement is allowed in the selection
                     (default True)
        """
        # call super to check the super parameters
        super(TournamentSelector, self).select(population)
        # select k random individuals
        individuals = sorted(random.choice(population, size=k, replace=replace),
                             key=lambda ind: ind.fitness,
                             reverse=True)
        # if there is no size, return the first (highest)
        if size is None:
            return individuals[0]
        # return up to size individuals
        return individuals[:size]


# explicitly export classes
__all__ = [
    'TournamentSelector'
]
