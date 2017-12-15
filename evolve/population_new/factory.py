"""An abstract factory for generating populations of chromosomes."""
from typing import Callable, List
import numpy as np
from ._chromosome import Chromosome


class ChromosomeFactory(object):
    """A factory for generating populations of chromosomes."""

    def __init__(self,
                 num_genes: int,
                 decode: Callable,
                 evaluate: Callable,
                 initialization: str='random'):
        """
        Initialize a new chromosome factory.

        Args:
            num_genes: the number of genes in each chromosome
            decode: a method that converts the gene set to a candidate solution
            evaluate: a method that evaluates fitness of candidate solutions
            initialization: the initial state for new chromosomes
                (default 'random')
        """
        # validate types to ensure that no surprises happen later on
        if not isinstance(num_genes, int):
            raise TypeError('num_genes must be of type: int')
        if not isinstance(decode, Callable):
            raise TypeError('decode must be a callable method')
        if not isinstance(evaluate, Callable):
            raise TypeError('evaluate must be a callable method')
        if not isinstance(initialization, (tuple, str)):
            raise TypeError('initialization must be of type: tuple, str')
        # validate values to really ensure no surprises happen later on
        if num_genes <= 0:
            raise ValueError('num_genes must be >= 0')
        try:
            random_phenotype = decode(np.random.random_sample(size=num_genes))
        except Exception as err:
            raise ValueError('decode should be a method: decode(genes: np.ndarray)')
        try:
            fitness = evaluate(random_phenotype)
        except Exception as err:
            raise ValueError('evaluate should be a method: evaluate(decode(genes: np.ndarray))')
        if not isinstance(fitness, float):
            raise ValueError('evaluate should return a float')

        # TODO: validate that "initialization" is totally valid

        # type and value checks passed, assign instance members
        self.num_genes = num_genes
        self.decode = decode
        self.evaluate = evaluate
        self.initialization = initialization

    @property
    def next_individual(self) -> Chromosome:
        """Create and return a new individual."""
        # generate genes
        # TODO: generate genes according to `initialization`
        genes = None
        # build a chromosome and return it
        return Chromosome(genes, self.decode, self.evaluate)


    # def population(self, size: int) -> List[Chromosome]:
    #     """
    #     Return a population of new chromosomes of given size.
    #
    #     Args:
    #         size: the number of individuals to generate
    #     """
    #     if not isinstance(size, (int, float)) or size < 0:
    #         raise ValueError('size must be a positive number')
    #     return [self.next_individual for _ in range(int(size))]


__all__ = ['ChromosomeFactory']
