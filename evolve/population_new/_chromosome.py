"""A general form for candidate solutions (chromosomes)."""
import numpy as np
from typing import Callable


class Chromosome(object):
    """A simple representation of candidate solution as a vector of numbers."""

    # class toggle for whether to use the phenotype (candidate solution) cache
    is_phenotype_cache_enabled = True

    # class toggle for whether to use the fitness cache
    is_fitness_cache_enabled = True

    # the private representation template string for the class (repr)
    _template = '{}(alleles={}, decode={}, evaluate={})'

    def __init__(self,
                 alleles: np.ndarray,
                 decode: Callable,
                 evaluate: Callable) -> None:
        """
        Initialize a new candidate solution.

        Args:
            alleles: the vector of values for the chromosome
                * the genes derive from the index of the alleles
            decode: a method that converts the gene set to a candidate solution
            evaluate: a method that evaluates fitness of candidate solutions
        """
        # Ignore all type checking, this module is private to the framework
        self.alleles = alleles
        self.decode = decode
        self.evaluate = evaluate
        # setup the cache objects
        self._phenotype_cache = None
        self._fitness_cache = None

    def __repr__(self) -> str:
        """Return a string representation of this object that can execute."""
        return self._template.format(self.__class__.__name__,
                                     self.alleles,
                                     self.decode.__name__,
                                     self.evaluate.__name__)

    def __str__(self) -> str:
        """Return a string representation of this object for a human."""
        return str(self.fitness)

    def __contains__(self, gene: int) -> bool:
        """
        Return a boolean determining in the gene is present in this chromosome.

        Args:
            gene: the gene to check for presence of
                Note: this does NOT check for alleles (values)

        Returns: true if gene is in the gene set, false otherwise
        """
        return gene in self.genes

    def __getitem__(self, gene: int) -> any:
        """
        Return the allele at the given gene.

        Args:
            gene: the gene of the allele to get (index in gene set)

        Returns: the allele at the given gene index
        """
        return self.alleles[gene]

    def __len__(self) -> int:
        """Return the length of this chromosome."""
        return len(self.alleles)

    def __lt__(self, other) -> bool:
        """
        Return a boolean determining if this instance is < another.

        Args:
            other: the other chromosome to compare against

        Returns: true if self has a fitness < other
        """
        return self.fitness < other.fitness

    def __le__(self, other) -> bool:
        """
        Return a boolean determining if this instance is <= another.

        Args:
            other: the other chromosome to compare against

        Returns: true if self has a fitness <= other
        """
        return self.fitness <= other.fitness

    def __eq__(self, other) -> bool:
        """
        Return a boolean determining if this instance is == another.

        Args:
            other: the other chromosome to compare against

        Returns: true if self has a fitness == other
        """
        return self.fitness == other.fitness

    @property
    def genes(self) -> np.ndarray:
        """Return the gene set for the chromosome (the index of alleles)."""
        return np.arange(len(self.alleles))

    @property
    def phenotype(self) -> any:
        """Return the candidate solution of this chromosome (the phenotype)."""
        # check if caching candidate solutions is enabled
        if self.is_phenotype_cache_enabled:
            # check if the cache was initialized yet
            if self._phenotype_cache is None:
                # initialize the cache by decoding
                self._phenotype_cache = self.decode(self.alleles)
            # return the cached candidate solution
            return self._phenotype_cache
        # ignore all cache features, decode and return the CS
        return self.decode(self.alleles)

    @property
    def fitness(self) -> float:
        """Evaluate and return a fitness for the chromosome."""
        # check if caching fitness is enabled
        if self.is_fitness_cache_enabled:
            # check if the cache was initialized yet
            if self._fitness_cache is None:
                # initialize the cache by decoding
                self._fitness_cache = self.evaluate(self.phenotype)
            # return the cached candidate solution
            return self._fitness_cache
        # ignore all cache features, evaluate the candidate solution and return
        return self.evaluate(self.phenotype)


# explicitly specify the exports from this file
__all__ = ['Chromosome']
