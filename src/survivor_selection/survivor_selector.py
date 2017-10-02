"""A module containing the survivor selector abstract base class."""
from typing import Union, List
from numpy import ndarray
from abc import abstractmethod
from src.population import Chromosome


class SurvivorSelectorABC:
    """An abstract base class for survivor selectors."""

    def __init__(self):
        """Intanstiate a new survivor selector abstract base class."""

    @abstractmethod
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


# explicitly specify exports
__all__ = [
    'SurvivorSelectorABC'
]
