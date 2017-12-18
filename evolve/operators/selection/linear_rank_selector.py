"""
This module contains a class for linear rank parent selection.

The proportionate selector is susceptible to:
*   sorting on each call to select
"""
from typing import List
from numpy import sum, random
from evolve.population_new._chromosome import Chromosome
from .selector import Selector


class LinearRankSelector(Selector):
    """A class for performing linear rank parent selection."""

    def __init__(self, size: int=None, replace: bool=True) -> None:
        """
        Initialize a new linear rank selector.

        Args:
            size: the size of the sub population to select
            replace: whether to allow replacement when selecting

        Returns: None
        """
        super(LinearRankSelector, self).__init__(size, replace)
        # setup the random selection method based on the size
        if self.size is None or self.size == 1:
            self.select_random = self._single
        else:
            self.select_random = self._multiple

    def _single(self,
                pop: List[Chromosome],
                p: list=None) -> List[Chromosome]:
        """
        Return a single random member from the population.

        Args:
            pop: the population to select from
            p: the probabilities to select with (default None)

        Returns: a list of 1 member from the population
        """
        index = random.choice(len(pop), replace=self.replace, p=p)
        return [pop[index]]

    def _multiple(self,
                  pop: List[Chromosome],
                  p: list=None) -> List[Chromosome]:
        """
        Return random members from the population.

        Args:
            pop: the population to select from
            p: the probabilities to select with (default None)

        Returns: a list of self.size member from the population
        """
        indexes = random.choice(len(pop),
                                size=self.size,
                                replace=self.replace, p=p)
        return [pop[i] for i in indexes]

    def select(self,
               population: List[Chromosome],
               maximize=True) -> List[Chromosome]:
        """
        Select a subset from the population.

        Args:
            population: the list of Chromosomes to select from
            maximize: whether to maximize or minimize fitness (default True)

        Returns: a list of selected chromosomes
        """
        # call super to check the super parameters
        super(LinearRankSelector, self).select(population)
        # sort the population by their fitness
        ranked = sorted(population, reverse=True)
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
        # generate a list of probabilities based on ranked scores
        if sum(ranked_scores) == 0:
            # if the sum is 0, the selection is purely random
            probablities = None
        else:
            # generate probabilities from the subject ranks
            probablities = ranked_scores / sum(ranked_scores)
            if not maximize:
                # invert probabilities to minimize
                probablities = 1 - probablities
        # return the results from the NumPy choice function
        return self.select_random(ranked, probablities)


# explicitly export classes
__all__ = ['LinearRankSelector']
