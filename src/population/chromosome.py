"""This module contains a class representing an abstract chromosome."""
from typing import Callable


class Chromosome:
    """This class represents a chromosome in a genetic optimization."""

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
        if not isinstance(evaluate, Callable):
            raise ValueError('`evaluate` must be a function')
        self._evaluate = evaluate

    @property
    def size(self) -> int:
        """Return the size of the chromosome."""
        return self._size

    @property
    def evaluate(self) -> Callable:
        """Return the evaluation function for the chromosome."""
        return self._evaluate


# explicitly import the appropriate parts
__all__ = [
    'Chromosome'
]
