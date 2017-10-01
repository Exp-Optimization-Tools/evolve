"""This module contains the binary mutation procreator class."""
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

    def mutate(self, individual):
        """Return a mutated copy of the individual."""
        return super(BinaryMutationProcreator, self).mutate(individual)


# explicitly specify exports
__all__ = [
    'BinaryMutationProcreator'
]
