"""This module contains a class representing an abstract chromosome."""
from typing import Callable
import numpy as np


class Chromosome:
    """
    This class represents a chromosome in a genetic optimization.

    Once created, the evaluation function and size of the chromosome are
    immutable. This is to ensure that chromosomes aren't mutated to an illegal
    state accidentally by the external api. _size and _evaluate should not be
    accessed, or updated by external code.
    """

    def __init__(self, size: int, evaluate: Callable):
        """
        Initialize a new chromosome of a given size.

        Args:
            size: the size of the chromosome (default 0)
            evaluate: the evaluation function for the fitness (default None)
        """
        # check the validity of the size parameter
        if not isinstance(size, (int, float)):
            raise ValueError('size should be a numeric value like: int, float')
        elif size < 0:
            raise ValueError('cannot create chromosome with a negative size')
        self._size = size
        # validate the evaluation function
        if not callable(evaluate):
            raise ValueError('evaluate must be a callable (method/function)')
        self._evaluate = evaluate
        # setup the genes instance variable
        self.genes = None

    @property
    def size(self) -> int:
        """Return the size of the chromosome."""
        return self._size

    @property
    def evaluate(self) -> Callable[[np.array], float]:
        """Return the evaluation function for the chromosome."""
        return self._evaluate

    @property
    def fitness(self) -> float:
        """Return the fitness of the gene from the evaluation function."""
        return self._evaluate(self.genes)


# explicitly export the classes
__all__ = [
    'Chromosome'
]
