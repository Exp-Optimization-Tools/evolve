"""This module contains the n-point crossover procreator class."""
from numpy import arange, random, array
from numpy.random import choice
from .crossover_procreator import CrossoverProcreatorABC


def flattened(some_list: list) -> list:
    """
    Return a flattened version of a list.

    Args:
        some_list: the list to flatten

    Returns a 1D flattened version of a 2D list
    """
    return [item for sublist in some_list for item in sublist]


class NPointCrossoverProcreator(CrossoverProcreatorABC):
    """This class performs n-point crossover parents."""

    def __init__(self, crossovers: int = 1):
        """
        Initialize a new n point crossover.

        Args:
            crossovers: the number of crossovers to perform (default 1)
                        the default is single-point crossover
        """
        if not isinstance(crossovers, int):
            raise TypeError('crossovers must be of type in')
        if crossovers < 0:
            raise ValueError('crossovers must >= 0')
        self.crossovers = crossovers

    def procreate(self, parents: list) -> list:
        """
        Args:
            parents: the list of parents to select from
            crossovers: the number of crossovers to perform
        """
        # verify that there are at least 2 parents
        if len(parents) < 2:
            raise ValueError('crossovers must have at least 2 parents')
        # verify that the size of the parents is more than the number of cuts
        if parents[0].size <= self.crossovers:
            raise ValueError('too many crossover points for chromosome size')
        # generate the list of indecies to cut along
        cuts = [0] + sorted(random.choice(arange(1, parents[0].size),
                                          size=self.crossovers,
                                          replace=False)) + [parents[0].size]
        # zip the indecies into ranges for indexing from parents
        cut_pairs = [(cuts[i], cuts[i + 1]) for i in range(0, len(cuts) - 1)]
        # TODO: option to select from one or the other (or others) randomly
        # instead of lock step
        # print(cut_pairs)
        # parents = random.choice(arange(0, len(parents)),
        #                         size=len(cut_pairs),
        #                         replace=True)
        # print(parents)
        # print()
        pieces = [parents[index % len(parents)].genes[cut[0]:cut[1]] for index, cut in enumerate(cut_pairs)]
        child = parents[0].copy()
        child.genes = array(flattened(pieces))
        return child


# explicitly specify exports
__all__ = [
    'NPointCrossoverProcreator'
]
