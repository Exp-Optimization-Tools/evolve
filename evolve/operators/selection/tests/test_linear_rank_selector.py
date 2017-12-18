"""This module tests the linear_rank_selector module."""
import unittest
from numpy import array, ndarray
from evolve.population_new import ChromosomeFactory
from evolve.population_new.factory import zeros, ones, random_sample
from ..selector import Selector
from ..linear_rank_selector import *


def evaluate(genes: ndarray):
    return genes.sum()


#
# MARK: Abstract Base Class
#


class LinearRankSelectorTestCase(unittest.TestCase):
    def setUp(self):
        self.zerofactory = ChromosomeFactory(3, lambda x: x, lambda x: x.sum(), zeros)
        self.onesfactory = ChromosomeFactory(3, lambda x: x, lambda x: x.sum(), ones)
        self.randfactory = ChromosomeFactory(3, lambda x: x, lambda x: x.sum(), random_sample)
        self.zeropopulation = self.zerofactory.make_chromosomes(10)
        self.onespopulation = self.onesfactory.make_chromosomes(10)
        self.randpopulation = self.randfactory.make_chromosomes(10)
        self.one_and_zero = [self.zeropopulation[0], self.onespopulation[1]]


#
# MARK: __init__()
#


class ShouldInstantiateLinearRankSelelctor(LinearRankSelectorTestCase):
    def test(self):
        self.assertTrue(isinstance(LinearRankSelector(), Selector))
        self.assertTrue(isinstance(LinearRankSelector(), LinearRankSelector))


#
# MARK: select(population)
#


class ShouldRaiseErrorOnInvalidPopulationWrongType(LinearRankSelectorTestCase):
    def test(self):
        sel = LinearRankSelector()
        with self.assertRaises(TypeError):
            sel.select('asdfasdfasdf')


class ShouldSelectProportionately(LinearRankSelectorTestCase):
    def test(self):
        sel = LinearRankSelector()
        self.assertEqual([0, 0, 0], list(sel.select(self.zeropopulation)[0].alleles))
        self.assertEqual([1, 1, 1], list(sel.select(self.onespopulation)[0].alleles))


class ShouldSelectProportionatelySize2(LinearRankSelectorTestCase):
    def test(self):
        sel = LinearRankSelector(size=2)
        self.assertEqual([0, 0, 0], list(sel.select(self.zeropopulation)[0].alleles))
        self.assertEqual([1, 1, 1], list(sel.select(self.onespopulation)[0].alleles))
