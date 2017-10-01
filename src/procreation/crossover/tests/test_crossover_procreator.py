"""This module contains test code for the crossover_procreator module."""
import unittest
from population import BinaryChromosome
from ..crossover_procreator import *


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


class ShouldRaiseErrorOnNoParents(CrossoverProcreatorTestCase):
    def runTest(self):
        crossover = CrossoverProcreatorABC()
        with self.assertRaises(ValueError):
            crossover.procreate([])

class ShouldRaiseErrorOnTooFewParents(CrossoverProcreatorTestCase):
    def runTest(self):
        crossover = CrossoverProcreatorABC()
        with self.assertRaises(ValueError):
            crossover.procreate([BinaryChromosome(size=5, evaluate=arb_eval)])
