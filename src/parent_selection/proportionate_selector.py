"""
This module contains a class for proportionate parent selection.

The proportionate selector is susceptible to:
*   the super individual problem
*   loss of selection pressure as the algorithm converges
"""
from typing import Union
from numpy import ndarray, sum, random
from .parent_selector import ABCParentSelector

# TODO: Update to support minimization

class ProportionateSelector(ABCParentSelector):
    """A class for performing proportionate parent selection."""

    def __init__(self, size: int = None, replace: bool = True):
        """
        Initialize a new proportionate parent selector.

        Args:
            size: the size of the sub population to select
            replace: whether to allow replacement when selecting
        """
        super(ProportionateSelector, self).__init__(size, replace)

    def select(self, population: Union[list, ndarray]):
        """
        Select a subset from the population.

        Args:
            population: the list of Chromosomes to select from
        """
        # call super to check the super parameters
        super(ProportionateSelector, self).select(population)
        # score every individual in the population
        scores = [individual.fitness for individual in population]
        # if the score is 0, they have equal chances
        if sum(scores) == 0:
            return random.choice(population, size=self.size, replace=self.replace)
        # generate probabilities as the proportion of score to total score
        probablities = scores / sum(scores)
        # return the results from the numpy choice function
        return random.choice(population, size=self.size, replace=self.replace, p=probablities)


# explicitly export classes
__all__ = [
    'ProportionateSelector'
]
