"""
This module contains a class for linear rank parent selection.

The proportionate selector is susceptible to:
*   sorting on each call to select
"""
from typing import Union
from numpy import ndarray, sum, random
from .parent_selector import ABCParentSelector


class LinearRankSelector(ABCParentSelector):
    """A class for performing linear rank parent selection."""

    def __init__(self, size: int = None, replace: bool = True):
        """
        Initialize a new linear ranke parent selector.

        Args:
            size: the size of the sub population to select
            replace: whether to allow replacement when selecting
        """
        super(LinearRankSelector, self).__init__(size, replace)

    def select(self, population: Union[list, ndarray]):
        """
        Select a subset from the population.

        Args:
            population: the list of Chromosomes to select from
        """
        # call super to check the super parameters
        super(LinearRankSelector, self).select(population)
        # sort the population by their fitness
        ranked = sorted(population, reverse=True,
                        key=lambda individual: individual.fitness)
        # calculate some static values for readability, mild performance
        P = len(population)
        scores = [individual.fitness for individual in ranked]
        min_score = min(scores)
        max_score = max(scores)
        dScore = max_score - min_score
        # the list of ranked scores
        ranked_scores = []
        # generate subjective fitness scores for each individual based on
        # their fitness and rank
        for rank, individual in enumerate(ranked):
            subjective_fitness = (P - rank) * dScore / (P - 1) + min_score
            ranked_scores.append(subjective_fitness)
        # if the sum is 0, the selection is random
        if sum(ranked_scores) == 0:
            return random.choice(population, size=self.size, replace=self.replace)
        # generate probablities from the subject ranks
        probablities = ranked_scores / sum(ranked_scores)
        # return the results from the numpy choice function
        return random.choice(population, size=self.size, replace=self.replace, p=probablities)


# explicitly export classes
__all__ = [
    'LinearRankSelector'
]
