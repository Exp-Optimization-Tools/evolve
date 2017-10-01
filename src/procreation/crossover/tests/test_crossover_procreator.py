"""This module contains test code for the crossover_procreator module."""
import unittest
from population import BinaryChromosome
from ..crossover_procreator import *
# random seed
from numpy.random import seed
seed(10)

#
# MARK: Abstract Base Class
#


class CrossoverProcreatorTestCase(unittest.TestCase):
    pass


#
# MARK: __init__()
#

class ShouldCreateCrossoverProcreator(CrossoverProcreatorTestCase):
    def runTest(self):
        crossover = CrossoverProcreatorABC()


#
# MARK: procreate
#


def arb_eval(genes):
    return 0


class procreate_ShouldRaiseErrorOnMissingParams(CrossoverProcreatorTestCase):
    def runTest(self):
        crossover = CrossoverProcreatorABC()
        with self.assertRaises(TypeError):
            crossover.procreate()


class procreate_ShouldRaiseErrorOnInvalidParamType(CrossoverProcreatorTestCase):
    def runTest(self):
        crossover = CrossoverProcreatorABC()
        with self.assertRaises(TypeError):
            crossover.procreate('asdfasdf')


class procreate_ShouldRaiseErrorOnNoParents(CrossoverProcreatorTestCase):
    def runTest(self):
        crossover = CrossoverProcreatorABC()
        with self.assertRaises(ValueError):
            crossover.procreate([])


class procreate_ShouldRaiseErrorOnTooFewParents(CrossoverProcreatorTestCase):
    def runTest(self):
        crossover = CrossoverProcreatorABC()
        with self.assertRaises(ValueError):
            crossover.procreate([BinaryChromosome(size=5, evaluate=arb_eval)])


class procreate_ShouldReturnParents(CrossoverProcreatorTestCase):
    def runTest(self):
        crossover = CrossoverProcreatorABC()
        parents = [
            BinaryChromosome(size=5, evaluate=arb_eval, initial_state='zeros'),
            BinaryChromosome(size=5, evaluate=arb_eval, initial_state='zeros')
        ]
        children = crossover.procreate(parents)
        self.assertEqual(parents, children)
