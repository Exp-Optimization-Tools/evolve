"""This module contains the binary mutation class."""
from numpy.random import random_sample
from .mutator import Mutator


class BinaryMutator(Mutator):
    """This class performs binary mutation on chromosomes."""

    def mutate(self, individual, inplace=False):
        """Return a mutated copy of the individual."""
        # super type checks individual and in-place
        super(BinaryMutator, self).mutate(individual, inplace)
        # if it's a list, iterate over all the items
        if isinstance(individual, list):
            return [self.mutate(_ind, inplace=inplace) for _ind in individual]
        # get the indexes of bits to flip
        flip = [random_sample() < self.mutation_rate for _ in individual]
        # create a copy if not in place
        if not inplace:
            individual = individual.copy()
        # flip the alleles accordingly
        individual.alleles[flip] = 1 - individual.alleles[flip]
        return individual


# explicitly specify exports
__all__ = [
    'BinaryMutator'
]
