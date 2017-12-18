"""This module contains test code for the mutation_procreator module."""
from unittest import TestCase
import numpy as np
from evolve.population_new._chromosome import Chromosome
from ..mutator import *


#
# MARK: __init__()
#


class ShouldRaiseErrorOnMissingParameters(TestCase):
    def runTest(self):
        with self.assertRaises(TypeError):
            mutator = Mutator()


class ShouldRaiseErrorOnInvalidMutationRateWrongType(TestCase):
    def runTest(self):
        with self.assertRaises(TypeError):
            mutator = Mutator('asdf')


class ShouldRaiseErrorOnNegativeMutationRate(TestCase):
    def runTest(self):
        with self.assertRaises(ValueError):
            mutator = Mutator(-0.01)


class ShouldRaiseErrorOnAboveOneMutationRate(TestCase):
    def runTest(self):
        with self.assertRaises(ValueError):
            mutator = Mutator(1.01)


class ShouldCreateMutationProcreatorRate0(TestCase):
    def runTest(self):
        mutator = Mutator(mutation_rate=0)


class ShouldCreateMutationProcreatorRate1(TestCase):
    def runTest(self):
        mutator = Mutator(mutation_rate=1)


class ShouldCreateMutationProcreatorRateArb(TestCase):
    def runTest(self):
        mutator = Mutator(mutation_rate=0.01)


#
# MARK: mutate
#


class mutate_ShouldRaiseErrorOnMissingParameters(TestCase):
    def runTest(self):
        mutator = Mutator(mutation_rate=0.01)
        with self.assertRaises(TypeError):
            mutator.mutate()


class mutate_ShouldRaiseErrorOnInvalidParamWrongType(TestCase):
    def runTest(self):
        mutator = Mutator(mutation_rate=0.01)
        with self.assertRaises(TypeError):
            mutator.mutate('asdf')

class mutate_ShouldNotMutateRate0(TestCase):
    def runTest(self):
        mutator = Mutator(mutation_rate=0)
        chrom = Chromosome(np.array([0, 0, 0]), lambda x: x, lambda x: 0)
        mutated = mutator.mutate(chrom)
        self.assertEqual([0, 0, 0], list(mutated.alleles))


class mutate_ShouldNotMutateRate0List(TestCase):
    def runTest(self):
        mutator = Mutator(mutation_rate=0)
        chroms = [
            Chromosome(np.array([0, 0, 0]), lambda x: x, lambda x: 0),
            Chromosome(np.array([0, 0, 0]), lambda x: x, lambda x: 0)
        ]
        mutated = mutator.mutate(chroms)
        self.assertEqual([0, 0, 0], list(mutated[0].alleles))
        self.assertEqual([0, 0, 0], list(mutated[1].alleles))


class mutate_ShouldNotMutateRate1(TestCase):
    def runTest(self):
        mutator = Mutator(mutation_rate=1)
        chrom = Chromosome(np.array([0, 0, 0]), lambda x: x, lambda x: 0)
        mutated = mutator.mutate(chrom)
        self.assertEqual([0, 0, 0], list(mutated.alleles))


class mutate_ShouldRaiseErrorOnInvalidInPlaceWrongType(TestCase):
    def runTest(self):
        mutator = Mutator(mutation_rate=0.01)
        chrom = Chromosome(np.array([0, 0, 0]), lambda x: x, lambda x: 0)
        with self.assertRaises(TypeError):
            mutator.mutate(chrom, 'asdf')


class mutate_ShouldMutateInPlace(TestCase):
    def runTest(self):
        mutator = Mutator(mutation_rate=0.01)
        chrom = Chromosome(np.array([0, 0, 0]), lambda x: x, lambda x: 0)
        mutator.mutate(chrom, True)
