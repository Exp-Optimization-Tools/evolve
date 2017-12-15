"""This module contains the n-point crossover procreator class."""
from typing import List, Union
from numpy import arange, array, ndarray, zeros
from numpy.random import choice
from evolve.population import Chromosome
from .procreator import Procreator


def cut_points(num_genes: int, crossovers: int):
    """
    Return a list of cutpoints for the chromosome size and crossover points.

    Args:
        num_genes: the size of the chromosome to cut up
        crossovers: the number of crossover points

    Returns: an ordered list of cutpoint tuples in the [(first, last),...]
        format. first index is inclusive, last is not
    """
    # use numpy to genereate an index based on the number of genes then select
    # a random number equal to the number of crossovers _without_ replacement
    crossovers = choice(arange(1, num_genes), size=crossovers, replace=False)
    # generate the indexes to cut along including the first and last indeces
    cuts = [0] + sorted(crossovers) + [num_genes]
    # rewrap the list of indexes into a list of tuples of indexes [lower, upper)
    return [(cuts[i], cuts[i + 1]) for i in range(len(cuts) - 1)]


class NPointCrossoverProcreator(Procreator):
    """This class performs n-point crossover parents."""

    def __init__(self, crossovers: int=1):
        """
        Initialize a new n point crossover.

        Args:
            crossovers: the number of crossovers to perform (default 1)
                        the default is single-point crossover
        """
        if not isinstance(crossovers, int):
            raise TypeError('crossovers must be of type: int')
        if crossovers < 0:
            raise ValueError('crossovers must greater than or equal to 0')
        self.crossovers = crossovers

    def __repr__(self):
        """Return a string representation of this object."""
        return f'{self.__class__.__name__}(crossovers={self.crossovers})'

    def procreate(self, parents: Union[List[Chromosome], ndarray]) -> List[Chromosome]:
        """
        Return a list of new children generated from a list of parents.

        Args:
            parents: the list of parents to select genes from

        Returns: a list of new children
        """
        super(NPointCrossoverProcreator, self).procreate(parents)
        # verify that the size of the parents is more than the number of cuts
        if parents[0].size <= self.crossovers:
            raise ValueError('too many crossover points for chromosome size')
        # generate the list of indecies to cut along
        cuts = cut_points(parents[0].size, self.crossovers)
        # create the empty list of children
        children = [zeros(parents[0].size), zeros(parents[0].size)]
        # switch between the left and right parent
        parent_index = 0
        # iterate over all the cut pairs
        for cut in cuts:
            # build the cut range slice to reduce duplication
            cut_range = slice(cut[0], cut[1])
            # fetch the next pieces of the 2 chidlren based on cut range
            children[0][cut_range] = parents[parent_index][cut_range]
            children[1][cut_range] = parents[1 - parent_index][cut_range]
            # invert the index to switch to the other parent on the next iter
            parent_index = 1 - parent_index
        # return a list of copies chromosome with the new child genes
        return [parents[0].copy(genes=genes) for genes in children]


# explicitly specify exports
__all__ = [
    'NPointCrossoverProcreator'
]
