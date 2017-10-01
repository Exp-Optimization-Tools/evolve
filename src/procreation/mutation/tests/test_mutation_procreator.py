"""This module contains test code for the mutation_procreator module."""
import unittest
from population import BinaryChromosome
from ..mutation_procreator import *


#
# MARK: Abstract Base Class
#


class MutationProcreatorTestCase(unittest.TestCase):
    pass


#
# MARK: __init__()
#


class ShouldRaiseErrorOnMissingParameters(MutationProcreatorTestCase):
    def runTest(self):
        with self.assertRaises(TypeError):
            mutator = MutationProcreatorABC()


class ShouldCreateMutationProcreator(MutationProcreatorTestCase):
    def runTest(self):
        mutator = MutationProcreatorABC(mutation_rate=0.01)


#
# MARK: mutate
#


def arb_eval(genes):
    return 0


class ShouldNotMutate(MutationProcreatorTestCase):
    def runTest(self):
        mutator = MutationProcreatorABC(mutation_rate=0)
        mutated = mutator.mutate(BinaryChromosome(size=5,
                                                  evaluate=arb_eval,
                                                  initial_state='zeros'))
        self.assertEqual([0,0,0,0,0], list(mutated.genes))
