"""A module containing an implementation of generational replacement."""
from typing import Union, List
from numpy import ndarray
from src.population import Chromosome
from .survivor_selector import SurvivorSelectorABC


class GenerationalSurvivorSelector(SurvivorSelectorABC):
    """A class for selecting survivors generationally."""

    def select(self,
               population: Union[List[Chromosome], ndarray],
               parents: Union[List[Chromosome], ndarray],
               children: Union[List[Chromosome], ndarray]) -> List[Chromosome]:
        """Return a population with the children replacing the parents.

        Args:
            population: the population to mutate
            parents: the population of parents that were selected
            children: the population of children that were generated

        Returns: A population with the some distribution of replacement
        """
        # iterate over all the parents removing each from the population
        [population.remove(parent) for parent in parents if parent in population]
        # replace the parents with the new children
        population += children


# explicitly specify exports
__all__ = [
    'GenerationalSurvivorSelector'
]
