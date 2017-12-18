"""This module contains the binary mutation class."""
from numpy.random import random_sample
from .mutator import Mutator


class BinaryMutationProcreator(Mutator):
    """This class performs binary mutation on chromosomes."""

    def mutate(self, individual, inplace=False):
        """Return a mutated copy of the individual."""
        # super type checks individual and in-place
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
