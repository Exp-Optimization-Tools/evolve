"""This module contains test cases for the ChromosomeFactory class."""
import unittest
from ..chromosome import Chromosome
from ..binary_chromosome import BinaryChromosome
from ..chromosome_factory import *


def arb_eval(genes):
    return 1


#
# MARK: Abstract Base Class
#


class ChromosomeFactoryTestCase(unittest.TestCase):
    pass

#
# MARK: __init__()
#

class ShouldRaiseErrorOnNoParameters(ChromosomeFactoryTestCase):
    def runTest(self):
        with self.assertRaises(TypeError):
            ChromosomeFactory()


class ShouldRaiseErrorOnMissingChromosomeSize(ChromosomeFactoryTestCase):
    def runTest(self):
        with self.assertRaises(TypeError):
            ChromosomeFactory(Chromosome)


class ShouldRaiseErrorOnMissingEvaluation(ChromosomeFactoryTestCase):
    def runTest(self):
        with self.assertRaises(TypeError):
            ChromosomeFactory(Chromosome, 10)


class ShouldCreateChromosomeFactory(ChromosomeFactoryTestCase):
    def runTest(self):
        try:
            ChromosomeFactory(Chromosome, 10, arb_eval)
        except Exception:
            self.fail('ChromosomeFactory raised unexpected error!')


#
# MARK: next_individual
#


class ShouldCreateChromosomeFromFactory(ChromosomeFactoryTestCase):
    def runTest(self):
        try:
            factory = ChromosomeFactory(Chromosome, 10, arb_eval)
            self.assertTrue(isinstance(factory.next_individual, Chromosome))
        except Exception:
            self.fail('ChromosomeFactory raised unexpected error!')


class ShouldCreateBinaryChromosomeFromFactory(ChromosomeFactoryTestCase):
    def runTest(self):
        try:
            factory = ChromosomeFactory(BinaryChromosome, 5, arb_eval, 'zeros')
            self.assertTrue(isinstance(factory.next_individual, BinaryChromosome))
            self.assertEqual(list(factory.next_individual.genes), [0,0,0,0,0])
        except Exception:
            self.fail('ChromosomeFactory raised unexpected error!')


#
# MARK: population
#


class ShouldCreateChromosomePopulationFromFactory(ChromosomeFactoryTestCase):
    def runTest(self):
        try:
            factory = ChromosomeFactory(Chromosome, 10, arb_eval)
            pop = factory.population(10)
            self.assertTrue(isinstance(pop, list))
            self.assertTrue(isinstance(pop[0], Chromosome))
            self.assertTrue(isinstance(pop[9], Chromosome))
        except Exception:
            self.fail('ChromosomeFactory raised unexpected error!')


class ShouldCreateBinaryChromosomePopulationFromFactory(ChromosomeFactoryTestCase):
    def runTest(self):
        try:
            factory = ChromosomeFactory(BinaryChromosome, 5, arb_eval, 'ones')
            pop = factory.population(10)
            self.assertTrue(isinstance(pop, list))
            self.assertTrue(isinstance(pop[0], BinaryChromosome))
            self.assertTrue(isinstance(pop[9], BinaryChromosome))
            self.assertEqual(list(pop[0].genes), [1,1,1,1,1])
        except Exception:
            self.fail('ChromosomeFactory raised unexpected error!')
