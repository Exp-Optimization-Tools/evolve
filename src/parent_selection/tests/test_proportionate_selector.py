"""This module tests the proportionate_selector module."""
import unittest
from numpy import array
from ..proportionate_selector import *


#
# MARK: Abstract Base Class
#


class ProportionateSelectorTestCase(unittest.TestCase):
    pass

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
