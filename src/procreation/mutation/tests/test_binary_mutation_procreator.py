"""This module contains test code for the binary_mutation_procreator module."""
import unittest
from population import BinaryChromosome
from ..binary_mutation_procreator import *


#
# MARK: Abstract Base Class
#


class BinaryMutationProcreatorTestCase(unittest.TestCase):
    pass


#
# MARK: __init__()
#


class ShouldRaiseErrorOnMissingParameters(BinaryMutationProcreatorTestCase):
    def runTest(self):
        with self.assertRaises(TypeError):
            mutator = BinaryMutationProcreator()


class ShouldCreateMutationProcreator(BinaryMutationProcreatorTestCase):
    def runTest(self):
        mutator = BinaryMutationProcreator(mutation_rate=0.01)


#
# MARK: mutate
#


def arb_eval(genes):
    return 0


class ShouldNotMutate(BinaryMutationProcreatorTestCase):
    def runTest(self):
        mutator = BinaryMutationProcreator(mutation_rate=0)
        mutated = mutator.mutate(BinaryChromosome(size=5,
                                                  evaluate=arb_eval,
                                                  initial_state='zeros'))
        self.assertEqual([0,0,0,0,0], list(mutated.genes))


class ShouldMutateAll(BinaryMutationProcreatorTestCase):
    def runTest(self):
        mutator = BinaryMutationProcreator(mutation_rate=1)
        mutated = mutator.mutate(BinaryChromosome(size=5,
                                                  evaluate=arb_eval,
                                                  initial_state='zeros'))
        self.assertEqual([1,1,1,1,1], list(mutated.genes))


class ShouldMutateHalf(BinaryMutationProcreatorTestCase):
    def runTest(self):
        SIZE = 5
        TRIALS = 20
        bits = 0
        for trial in range(TRIALS):
            mutator = BinaryMutationProcreator(mutation_rate=0.5)
            mutated = mutator.mutate(BinaryChromosome(size=SIZE,
                                                      evaluate=arb_eval,
                                                      initial_state='zeros'))
            bits += mutated.genes.sum()
        rate = bits / (SIZE * TRIALS)
        self.assertTrue(rate >= 0.4 and rate <= 0.6)
