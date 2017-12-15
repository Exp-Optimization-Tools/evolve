"""An abstract factory for generating populations of chromosomes."""
from typing import Callable


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
        if not isinstance(num_genes, int):
            raise TypeError('num_genes must be of type: int')
        if not isinstance(decode, Callable):
            raise TypeError('decode must be a callable method')
        if not isinstance(evaluate, Callable):
            raise TypeError('evaluate must be a callable method')
        if not isinstance(initialization, (tuple, str)):
            raise TypeError('initialization must be of type: tuple, str')
        # type and value checks passed, assign instance members
        self.num_genes = num_genes
        self.decode = decode
        self.evaluate = evaluate
        self.initialization = initialization


__all__ = ['ChromosomeFactory']
