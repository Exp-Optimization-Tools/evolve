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

    def _subjective_fitnesses(self, ranked: List[Chromosome]) -> List[float]:
        """
        Return a list of subjective fitnesses for a population.

        Args:
            ranked: the list of RANKED individuals

        Returns: a list of subjective fitnesses based on rank and score
        """
        P = len(ranked)
        scores = [individual.fitness for individual in ranked]
        min_score = min(scores)
        max_score = max(scores)
        dScore = max_score - min_score
        # the list of ranked scores
        subjective_fitnesses = []
        # generate subjective fitness scores for each individual based on
        # their fitness and rank
        for rank, individual in enumerate(ranked):
            subjective_fitness = (P - rank) * dScore / (P - 1) + min_score
            subjective_fitnesses.append(subjective_fitness)
        return subjective_fitnesses

    def _probabilities(self,
                       subjective_fitnesses: List[float],
                       maximize: bool) -> List[float]:
        """
        Return probabilities based on subjective fitnesses.

        Args:
            subjective_fitnesses: the list of subjective fitness scores
            maximize: whether to maximize of minimize the fitness score

        Returns: a list of probabilities. (the L1 norm of the fitnesses)
        """
        if sum(subjective_fitnesses) == 0:
            # if the sum is 0, the selection is purely random
            return None
        else:
            if maximize:
                # maximize is standard functionality so return the L1 norm
                return subjective_fitnesses / sum(subjective_fitnesses)
            else:
                # minimizing, return the _inverted_ L1 norm
                return 1 - (subjective_fitnesses / sum(subjective_fitnesses))

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
        # determine the subjective fitnesses based on rank and fitness
        subjective_fitnesses = self._subjective_fitnesses(ranked)
        # generate a list of probabilities based on ranked scores
        probabilities = self._probabilities(subjective_fitnesses, maximize)
        # return the results from the NumPy choice function
        return self.select_random(ranked, probabilities)


# explicitly export classes
__all__ = ['LinearRankSelector']
