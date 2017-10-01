"""This module contains the mutation procreator abstract base class."""
from typing import Union, List
from src.population import Chromosome
from abc import abstractmethod


class MutationProcreatorABC:
    """This class is an abstract base class for mutation procreators."""

    def __init__(self, mutation_rate: float):
        """
        Intanstiate a new mutations procreator abstract base class

        Args:
            mutation_rate: the mutation rate for the procreator
        """
        # make sure the mutation rate is a number
        if not isinstance(mutation_rate, (float, int)):
            raise TypeError('mutation_rate should be of type: float, int')
        # make sure the mutation rate is a P in [0,1]
        if mutation_rate < 0 or mutation_rate > 1:
            raise ValueError('mutation_rate should be a probability in [0, 1]')
        # assign the mutation rate to self
        self.mutation_rate = mutation_rate

    @abstractmethod
    def mutate(self,
               individual: Union[Chromosome, List[Chromosome]],
               inplace: bool = False) -> Union[Chromosome, List[Chromosome]]:
        """
        Return a mutated copy of the individual.

        Args:
            individual: an individual or list of individuals to mutate
            inplace: whether to perform the operation in place

        Returns: a mutated individual (or list of them)
        """
        # make sure individual is a chromosome or list of them
        if not isinstance(individual, (Chromosome, list)):
            raise TypeError('can only mutate subclasses of Chromosome (and lists of them)')
        # make sure inplace is a boolean value
        if not isinstance(inplace, bool):
            raise TypeError('inplace must be a boolean value')
        # do nothing, return the input
        return individual


# explicitly specify exports
__all__ = [
    'MutationProcreatorABC'
]
