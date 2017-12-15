"""An abstract factory for generating populations of chromosomes."""
from typing import Callable, List
import numpy as np
from ._chromosome import Chromosome


def zeros(num_genes: int) -> np.ndarray:
    """Return a vector of num_genes zeros."""
    return np.zeros(num_genes)


def ones(num_genes: int) -> np.ndarray:
    """Return a vector of num_genes ones."""
    return np.ones(num_genes)


def uniform_binary(num_genes: int) -> np.ndarray:
    """Return a vector of num_genes ones."""
    return np.random.randint(low=0, high=2, size=num_genes)


def random_sample(num_genes: int) -> np.ndarray:
    """Return a vector of num_genes random scalars."""
    return np.random.random_sample(size=num_genes)


class ChromosomeFactory(object):
    """A factory for generating populations of chromosomes."""

    def __init__(self,
                 num_genes: int,
                 decode: Callable,
                 evaluate: Callable,
                 random_alleles: Callable=random_sample) -> None:
        """
        Initialize a new chromosome factory.

        Args:
            num_genes: the number of genes in each chromosome
            decode: a method that converts the gene set to a candidate solution
            evaluate: a method that evaluates fitness of candidate solutions
            random_alleles: a method that generates random allele sets
                (default random_sample)
        """
        # validate types to ensure that no surprises happen later on
        if not isinstance(num_genes, int):
            raise TypeError('num_genes must be of type: int')
        if not isinstance(decode, Callable):
            raise TypeError('decode must be a callable method')
        if not isinstance(evaluate, Callable):
            raise TypeError('evaluate must be a callable method')
        if not isinstance(random_alleles, Callable):
            raise TypeError('initialization must be a callable method')
        # validate values to really ensure no surprises happen later on
        if num_genes <= 0:
            raise ValueError('num_genes must be >= 0')
        try:
            alleles = random_alleles(num_genes)
        except Exception as err:
            raise ValueError('random_alleles should be a method: random_alleles(num_genes: int) -> np.ndarray')
        try:
            random_phenotype = decode(alleles)
        except Exception as err:
            raise ValueError('decode should be a method: decode(alleles: np.ndarray)')
        try:
            fitness = float(evaluate(random_phenotype))
        except Exception as err:
            raise ValueError('evaluate should be a method: evaluate(decode(genes: np.ndarray)) -> float')
        if not isinstance(fitness, float):
            raise ValueError('evaluate should return a float')
        # type and value checks passed, assign instance members
        self.num_genes = num_genes
        self.decode = decode
        self.evaluate = evaluate
        self.random_alleles = random_alleles

    @property
    def next_chromosome(self) -> Chromosome:
        """Create and return a new chromosome."""
        # generate num_genes alleles using the random_alleles method
        alleles = self.random_alleles(self.num_genes)
        # build a chromosome and return it
        return Chromosome(alleles, self.decode, self.evaluate)

    def make_chromosomes(self, size: int) -> List[Chromosome]:
        """
        Return a population of new chromosomes of given size.

        Args:
            size: the number of individuals to generate

        Returns: a list of new chromosomes
        """
        # validate that the size parameter is valid
        if not isinstance(size, int) or size < 0:
            raise ValueError('size must be a positive int')
        # iterate over the size producing chromosomes and return them in a list
        return [self.next_chromosome for _ in range(size)]


__all__ = [
    'zeros',
    'ones',
    'uniform_binary',
    'random_sample',
    'ChromosomeFactory'
]
