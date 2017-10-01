"""This module contains the mutation procreator abstract base class."""
from abc import abstractmethod


class MutationProcreatorABC:
    """This class is an abstract base class for mutation procreators."""

    def __init__(self, mutation_rate: float):
        """
        Intanstiate a new mutations procreator abstract base class

        Args:
            mutation_rate: the mutation rate for the procreator
        """
        if not isinstance(mutation_rate, (float, int)):
            raise TypeError('mutation_rate should be of type: float, int')
        self.mutation_rate = mutation_rate

    @abstractmethod
    def mutate(self, individual):
        """Return a mutated copy of the individual."""
        return individual


# explicitly specify exports
__all__ = [
    'MutationProcreatorABC'
]
