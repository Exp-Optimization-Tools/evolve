"""This module tests the tournament_selector module."""
import unittest
from numpy import array, ndarray
from population import BinaryChromosome, ChromosomeFactory
from ..tournament_selector import *


def evaluate(genes: ndarray):
    return genes.sum()


#
# MARK: Abstract Base Class
#


class TournamentSelectorTestCase(unittest.TestCase):
    def setUp(self):
        self.zerofactory = ChromosomeFactory(BinaryChromosome, 5,
                                             evaluate=evaluate,
                                             initial_state='zeros')
        self.onesfactory = ChromosomeFactory(BinaryChromosome, 5,
                                             evaluate=evaluate,
                                             initial_state='ones')
        self.randfactory = ChromosomeFactory(BinaryChromosome, 5,
                                             evaluate=evaluate,
                                             initial_state='random')
        self.zeropopulation = self.zerofactory.population(10)
        self.onespopulation = self.onesfactory.population(10)
        self.randpopulation = self.randfactory.population(10)
        self.one_and_zero = [self.zeropopulation[0], self.onespopulation[1]]

#
# MARK: __init__()
#

class ShouldInstantiateABCParentSelector(TournamentSelectorTestCase):
    def runTest(self):
        self.assertTrue(isinstance(TournamentSelector(), TournamentSelector))

#
# MARK: select(population)
#

class ShouldRaiseErrorOnInvalidPopulationWrongType(TournamentSelectorTestCase):
    def runTest(self):
        sel = TournamentSelector()
        with self.assertRaises(TypeError):
            sel.select('asdfasdfasdf')

class ShouldSelectProportionately(TournamentSelectorTestCase):
    def runTest(self):
        sel = TournamentSelector()
        self.assertEqual([0,0,0,0,0], list(sel.select(self.zeropopulation, k=3).genes))
        self.assertEqual([0,0,0,0,0], list(sel.select(self.zeropopulation, k=3, size=2)[0].genes))
        self.assertEqual([1,1,1,1,1], list(sel.select(self.onespopulation, k=3).genes))
        self.assertEqual([1,1,1,1,1], list(sel.select(self.onespopulation, k=3, size=2)[0].genes))

# class ShouldSelectProportionatelyOneAndZero(TournamentSelectorTestCase):
#     def runTest(self):
#         sel = TournamentSelector()
#         print(sel.select(self.one_and_zero, k=3))
