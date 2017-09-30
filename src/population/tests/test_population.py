"""This module contains test code for the population module."""
import unittest
from ..chromosome import Chromosome
from ..binary_chromosome import BinaryChromosome
from ..chromosome_factory import ChromosomeFactory
from ..population import *


def arb_eval(genes):
    return 1


#
# MARK: Abstract Base Class
#


class PopulationTestCase(unittest.TestCase):
    pass

#
# MARK: __init__()
#

class ShouldRaiseErrorOnNoParameters(PopulationTestCase):
    def runTest(self):
        with self.assertRaises(TypeError):
            Population()


class ShouldRaiseErrorOnMissingFactory(PopulationTestCase):
    def runTest(self):
        with self.assertRaises(TypeError):
            Population(0)


class ShouldRaiseErrorOnInvalidFactoryWrongType(PopulationTestCase):
    def runTest(self):
        with self.assertRaises(TypeError):
            Population(0, None)


class ShouldRaiseErrorOnInvalidSizeWrongType(PopulationTestCase):
    def runTest(self):
        with self.assertRaises(TypeError):
            factory = ChromosomeFactory(Chromosome, 10, arb_eval)
            Population(None, factory)


class ShouldRaiseErrorOnInvalidSize(PopulationTestCase):
    def runTest(self):
        with self.assertRaises(ValueError):
            factory = ChromosomeFactory(Chromosome, 10, arb_eval)
            Population(-1, factory)


class ShouldCreatePopulation(PopulationTestCase):
    def runTest(self):
        factory = ChromosomeFactory(BinaryChromosome, 2, arb_eval, 'ones')
        pop = Population(10, factory)
        self.assertTrue(isinstance(pop.individuals, list))
        self.assertEqual(len(pop.individuals), 10)
        self.assertEqual(list(pop.individuals[0].genes), [1,1])
