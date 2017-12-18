"""This module contains test code for the binary_mutation_procreator module."""
from unittest import TestCase
import numpy as np
from numpy.random import seed
from evolve.population_new._chromosome import Chromosome
from ..binary_mutator import *


#
# MARK: __init__()
#


class init_ShouldRaiseErrorOnMissingParameters(TestCase):
    def runTest(self):
        with self.assertRaises(TypeError):
            mutator = BinaryMutator()


class init_ShouldCreateMutationProcreator(TestCase):
    def runTest(self):
        mutator = BinaryMutator(mutation_rate=0.01)


#
# MARK: mutate
#


class mutate_ShouldRaiseErrorOnInvalidMutateParameters(TestCase):
    def runTest(self):
        mutator = BinaryMutator(mutation_rate=0)
        with self.assertRaises(TypeError):
            mutator.mutate('asdf')


class mutate_ShouldNotMutate(TestCase):
    def runTest(self):
        mutator = BinaryMutator(mutation_rate=0)
        chrom = Chromosome(np.array([0, 0, 0]), lambda x: x, lambda x: 0)
        mutated = mutator.mutate(chrom)
        self.assertEqual([0, 0, 0], list(mutated.alleles))


class mutate_ShouldNotMutateList(TestCase):
    def runTest(self):
        mutator = BinaryMutator(mutation_rate=0)
        chroms = [
            Chromosome(np.array([0, 0, 0]), lambda x: x, lambda x: 0),
            Chromosome(np.array([0, 0, 0]), lambda x: x, lambda x: 0)
        ]
        mutated = mutator.mutate(chroms)
        self.assertEqual([0, 0, 0], list(mutated[0].alleles))
        self.assertEqual([0, 0, 0], list(mutated[1].alleles))


class mutate_ShouldMutateAll(TestCase):
    def runTest(self):
        mutator = BinaryMutator(mutation_rate=1)
        chrom = Chromosome(np.array([0, 0, 0]), lambda x: x, lambda x: 0)
        mutated = mutator.mutate(chrom)
        self.assertEqual([1, 1, 1], list(mutated.alleles))


class mutate_ShouldMutateAllList(TestCase):
    def runTest(self):
        mutator = BinaryMutator(mutation_rate=1)
        chroms = [
            Chromosome(np.array([0, 0, 0]), lambda x: x, lambda x: 0),
            Chromosome(np.array([0, 0, 0]), lambda x: x, lambda x: 0)
        ]
        mutated = mutator.mutate(chroms)
        self.assertEqual([1, 1, 1], list(mutated[0].alleles))
        self.assertEqual([1, 1, 1], list(mutated[1].alleles))


class mutate_ShouldMutateHalf(TestCase):
    def runTest(self):
        seed(10)
        mutator = BinaryMutator(mutation_rate=0.5)
        chroms = [
            Chromosome(np.array([0, 0, 0]), lambda x: x, lambda x: 0),
            Chromosome(np.array([0, 0, 0]), lambda x: x, lambda x: 0),
            Chromosome(np.array([0, 0, 0]), lambda x: x, lambda x: 0)
        ]
        mutated = mutator.mutate(chroms)
        self.assertEqual([0, 1, 0], list(mutated[0].alleles))
        self.assertEqual([0, 1, 1], list(mutated[1].alleles))
        self.assertEqual([1, 0, 1], list(mutated[2].alleles))
