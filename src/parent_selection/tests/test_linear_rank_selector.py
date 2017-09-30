"""This module tests the linear_rank_selector module."""
import unittest
from numpy import array
from ..linear_rank_selector import *


#
# MARK: Abstract Base Class
#


class LinearRankSelectorTestCase(unittest.TestCase):
    pass

#
# MARK: __init__()
#

class ShouldInstantiateABCParentSelector(LinearRankSelectorTestCase):
    def runTest(self):
        self.assertTrue(isinstance(LinearRankSelector(), LinearRankSelector))

#
# MARK: select(population)
#

class ShouldRaiseErrorOnInvalidPopulationWrongType(LinearRankSelectorTestCase):
    def runTest(self):
        sel = LinearRankSelector()
        with self.assertRaises(TypeError):
            sel.select('asdfasdfasdf')
