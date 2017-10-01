"""
This module contains a class for tournament parent selection.

*   selection pressure increases and decreases with k
"""
from typing import Union
from numpy import ndarray, random
from .parent_selector import ABCParentSelector


class TournamentSelector(ABCParentSelector):
    """A class for performing tournament parent selection."""

    def __init__(self,
                 size: int = None,
                 replace: bool = True,
                 individuals_per_tournament: int = None):
        """
        Initialize a new tournament selector.

        Args:
            size: the size of the sub population to select
            replace: whether to allow replacement when selecting
            individuals_per_tournament: the number of individuals to select
                                        from for each tournment (default None)
        """
        # call super to verify and asssign super parameters
        super(TournamentSelector, self).__init__(size, replace)
        # verify the individuals_per_tournament parameter
        if individuals_per_tournament is None:
            pass
        elif not isinstance(individuals_per_tournament, int):
            raise TypeError('individuals_per_tournament must be of type: None, int')
        elif individuals_per_tournament < 0:
            raise ValueError('individuals_per_tournament must be >= 0')
        # set the individuals_per_tournament to self
        self.individuals_per_tournament = individuals_per_tournament

    def select(self, population: Union[list, ndarray]):
        """
        Select a subset from the population.

        Args:
            population: the list of Chromosomes to select from
        """
        # call super to check the super parameters
        super(TournamentSelector, self).select(population)
        # select a subset of random individuals
        if self.individuals_per_tournament is None:
            participants = population
        else:
            participants = random.choice(population,
                                         size=self.individuals_per_tournament,
                                         replace=self.replace)
        individuals = sorted(participants,
                             key=lambda ind: ind.fitness,
                             reverse=True)
        # if there is no size, return the first (highest)
        if self.size is None:
            return individuals[0]
        # return up to size individuals
        return individuals[:self.size]


# explicitly export classes
__all__ = [
    'TournamentSelector'
]
