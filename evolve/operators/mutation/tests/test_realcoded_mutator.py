"""Test cases for the RealCodedMutator class."""
from unittest import TestCase
import numpy as np
from numpy.random import seed
from evolve.population_new._chromosome import Chromosome
from ..realcoded_mutator import *


#
# MARK: __init__()
#


class init_ShouldRaiseErrorOnMissingParameters(TestCase):
    def test(self):
        with self.assertRaises(TypeError):
            mutator = RealCodedMutator()


class init_ShouldCreateMutationProcreator(TestCase):
    def test(self):
        mutator = RealCodedMutator(mutation_rate=0.01)


#
# MARK: mutate
#


class mutate_ShouldRaiseErrorOnInvalidMutateParameters(TestCase):
    def test(self):
        mutator = RealCodedMutator(mutation_rate=0)
        with self.assertRaises(TypeError):
            mutator.mutate('asdf')


class mutate_ShouldNotMutate(TestCase):
    def test(self):
        mutator = RealCodedMutator(mutation_rate=0)
        chrom = Chromosome(np.array([0, 0, 0]), lambda x: x, lambda x: 0)
        mutated = mutator.mutate(chrom)
        self.assertEqual([0, 0, 0], list(mutated.alleles))


class mutate_ShouldNotMutateList(TestCase):
    def test(self):
        mutator = RealCodedMutator(mutation_rate=0)
        choms = [
            Chromosome(np.array([0, 0, 0]), lambda x: x, lambda x: 0),
            Chromosome(np.array([0, 0, 0]), lambda x: x, lambda x: 0)
        ]
        mutated = mutator.mutate(choms)
        self.assertEqual([0, 0, 0], list(mutated[0].alleles))
        self.assertEqual([0, 0, 0], list(mutated[1].alleles))


class mutate_ShouldMutateAll(TestCase):
    def test(self):
        mutator = RealCodedMutator(mutation_rate=1)
        chrom = Chromosome(np.array([0, 0, 0]), lambda x: x, lambda x: 0)
        mutated = mutator.mutate(chrom)
        expected = [0.14217004760152696, 0.37334076005146921, 0.67413361506634528]
        self.assertEqual(expected, list(mutated.alleles))


class mutate_ShouldMutateAllRange(TestCase):
    def test(self):
        mutator = RealCodedMutator(mutation_rate=1, random_state=(5, 6))
        chrom = Chromosome(np.array([0, 0, 0]), lambda x: x, lambda x: 0)
        mutated = mutator.mutate(chrom)
        for gene in mutated.alleles:
            self.assertTrue(gene >= 5)
            self.assertTrue(gene <= 6)


class mutate_ShouldMutateAllList(TestCase):
    def test(self):
        mutator = RealCodedMutator(mutation_rate=1)
        choms = [
            Chromosome(np.array([0, 0, 0]), lambda x: x, lambda x: 0),
            Chromosome(np.array([0, 0, 0]), lambda x: x, lambda x: 0)
        ]
        mutated = mutator.mutate(choms)
        self.assertIsInstance(mutated, list)
        c0 = [0.51313824255439089, 0.65039718193146723, 0.60103895340454438]
        self.assertEqual(c0, list(mutated[0].alleles))
        c1 = [0.31923608898854527, 0.090459349270907374, 0.30070005663620336]
        self.assertEqual(c1, list(mutated[1].alleles))


class mutate_ShouldMutateHalf(TestCase):
    def test(self):
        seed(10)
        mutator = RealCodedMutator(mutation_rate=0.5)
        chroms = [
            Chromosome(np.array([0, 0, 0]), lambda x: x, lambda x: 0),
            Chromosome(np.array([1, 1, 1]), lambda x: x, lambda x: 0),
            Chromosome(np.array([1, 1, 1]), lambda x: x, lambda x: 0)
        ]
        mutated = mutator.mutate(chroms)
        c0 = [0.0, 0.74880388253861185, 0.0]
        self.assertEqual(c0, list(mutated[0].alleles))
        c1 = [0.76053071219895874, 0.16911083656253545, 0.088339814174010267]
        self.assertEqual(c1, list(mutated[1].alleles))
        c2 = [1, 1, 0.51219226338577661]
        self.assertEqual(c2, list(mutated[2].alleles))
