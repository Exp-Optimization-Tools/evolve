"""A module containing an implementation of generational replacement."""
from typing import List
from evolve.population import Chromosome
from .replacer import Replacer


class GenerationalReplacer(Replacer):
    """A class for selecting survivors by generation."""

    def select(self,
               population: List[Chromosome],
               parents: List[Chromosome],
               children: List[Chromosome],
               **kwargs) -> List[Chromosome]:
        """Return a population with the children replacing the parents.

        Args:
            population: the population to mutate
            parents: the population of parents that were selected
            children: the population of children that were generated
            kwargs: the general base accepts more key word arguments (like
                    maximize, etc.) ignore them here

        Returns: A population with the some distribution of replacement
        """
        # iterate over all the parents removing each from the population
        for parent in parents:
            if parent in population:
                population.remove(parent)
        # replace the parents with the new children
        population += children


# explicitly specify exports
__all__ = [
    'GenerationalReplacer'
]
