"""This module contains a class to represent a population."""
from .chromosome_factory import ChromosomeFactory


class Population:
    """A class for generating, selecting from, and updating a population."""

    def __init__(self, size: int, factory: ChromosomeFactory):
        """
        Create a new population.

        Args:
            size: the size of the population
            factory: the ChromosomeFactory to use for generating individuals
        """
        if not isinstance(factory, ChromosomeFactory):
            raise TypeError('factory must be of type ChromosomeFactory')
        if not isinstance(size, (float, int)):
            raise TypeError('size must be a numeric like: float, int')
        if size < 0:
            raise ValueError('size must be greater than or equal to 0')
        # set the internal list of individuals from the factory
        self.individuals = factory.population(size)


# explicitly specify the export classes
__all__ = [
    'Population'
]
