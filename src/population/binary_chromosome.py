"""This module contains a class representing a binary chromosome."""
from typing import Callable
from numpy import ones, zeros
from numpy.random import randint
from .chromosome import Chromosome


class BinaryChromosome(Chromosome):
    """This class represents a binary encoded chromosome."""

    # the valid initial state options for how to initialize the chromosome
    INITIAL_STATES = ['zeros', 'ones', 'random']

    def __init__(self, size: int, evaluate: Callable, initial_state='random'):
        """Initialize a new chromosome of a given size.

        Args:
            size: the size of the chromosome (default 0)
            intial_state: the initial state of the chromosome (default 'random')
                * can be 'zeros', 'ones', or 'random'
        """
        super(BinaryChromosome, self).__init__(size, evaluate)
        # setup the initial state of the chromosome
        if initial_state == self.INITIAL_STATES[0]:
            # initialize with all 0s
            self.genes = zeros(size).astype(int)
        elif initial_state == self.INITIAL_STATES[1]:
            # intializw with all 1s
            self.genes = ones(size).astype(int)
        elif initial_state == self.INITIAL_STATES[2]:
            # initialize with random values in {0, 1}
            self.genes = randint(low=0, high=2, size=size).astype(int)
        # invalid initial state, raise error
        else:
            raise ValueError('initial_state must be one of: {}'.format(self.INITIAL_STATES))

    def __repr__(self) -> str:
        """Return a string represtation of this object"""
        return str(self.genes)


# explicitly export the classes
__all__ = [
    'BinaryChromosome'
]
