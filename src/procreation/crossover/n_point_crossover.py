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
        super(NPointCrossoverProcreator, self).procreate(parents)
        # verify that the size of the parents is more than the number of cuts
        if parents[0].size <= self.crossovers:
            raise ValueError('too many crossover points for chromosome size')
        # generate the list of indecies to cut along
        cuts = [0] + sorted(random.choice(arange(1, parents[0].size),
                                          size=self.crossovers,
                                          replace=False)) + [parents[0].size]
        # zip the indecies into ranges for indexing from parents
        cut_pairs = [(cuts[i], cuts[i + 1]) for i in range(0, len(cuts) - 1)]
        # the list of lists that need crushed into a single list
        child_pieces = [[] for _ in range(len(parents))]
        # loop over the indexes and cuts in the cut pairs
        for index, cut in enumerate(cut_pairs):
            # loop over each parent to get the same number of children as
            # parents
            for parent_index in range(len(parents)):
                # make a child piece by cutting the parent along the cut
                child_piece = parents[parent_index].genes[cut[0]:cut[1]]
                # append to the appropriate child piece list in a cyclical
                # fashion using the index, parent index, and modulo of parent
                # length
                child_pieces[(parent_index + index) % len(parents)].append(child_piece)
        # flatten the lists of pieces into single lists of bits
        child_genes = [flattened(child_piece) for child_piece in child_pieces]
        # create new genes by copying parents and replacing their genes, one
        # could just use the parent at index 0, but this form is more general
        return [parents[index].copy(genes=genes) for index, genes in enumerate(child_genes)]


# explicitly specify exports
__all__ = [
    'NPointCrossoverProcreator'
]
