"""This module tests the proportionate_selector module."""
import unittest
from numpy import array, ndarray
from ..proportionate_selector import *
from population import BinaryChromosome, ChromosomeFactory


def evaluate(genes: ndarray):
    return 1


#
# MARK: Abstract Base Class
#


class ProportionateSelectorTestCase(unittest.TestCase):
    def setUp(self):
        self.factory = ChromosomeFactory(BinaryChromosome, 5,
                                        evaluate=evaluate,
                                        initial_state='zeros')
        self.population = self.factory.population(10)

#
# MARK: __init__()
#

class ShouldInstantiateABCParentSelector(ProportionateSelectorTestCase):
    def runTest(self):
        self.assertTrue(isinstance(ProportionateSelector(), ProportionateSelector))

#
# MARK: select(population)
#

class ShouldRaiseErrorOnInvalidPopulationWrongType(ProportionateSelectorTestCase):
    def runTest(self):
        sel = ProportionateSelector()
        with self.assertRaises(TypeError):
            sel.select('asdfasdfasdf')

class ShouldSelectProportionately(ProportionateSelectorTestCase):
    def runTest(self):
        sel = ProportionateSelector()
        self.assertEqual([0,0,0,0,0], list(sel.select(self.population).genes))
        self.assertEqual([0,0,0,0,0], list(sel.select(self.population, size=2)[0].genes))
