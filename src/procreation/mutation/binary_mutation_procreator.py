"""This module contains the binary mutation procreator class."""
from numpy.random import random_sample
from .mutation_procreator import MutationProcreatorABC


class BinaryMutationProcreator(MutationProcreatorABC):
    """This class performs binary mutation on parents."""

    def __init__(self, mutation_rate: float):
        """
        Intanstiate a new mutations procreator abstract base class

        Args:
            mutation_rate: the mutation rate for the procreator
        """
        super(BinaryMutationProcreator, self).__init__(mutation_rate)

    def mutate(self, individual, inplace=False):
        """Return a mutated copy of the individual."""
        # super type checks individual and inplace
        super(BinaryMutationProcreator, self).mutate(individual, inplace)
        # if it's a list or array, iterate over all the items
        if isinstance(individual, list):
            return [self.mutate(_ind, inplace=inplace) for _ind in individual]
        # get the indexes of bits to flip
        flip = [random_sample() < self.mutation_rate for _ in range(individual.size)]
        # create a copy if not in place
        if not inplace:
            individual = individual.copy()
        # flip the genes accordingly
        individual.genes[flip] = 1 - individual.genes[flip]
        return individual


# explicitly specify exports
__all__ = [
    'BinaryMutationProcreator'
]
