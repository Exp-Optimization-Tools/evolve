"""This module tests the parent_selector module."""
import unittest
from numpy import array
from ..parent_selector import *


#
# MARK: Abstract Base Class
#


class ParentSelectorTestCase(unittest.TestCase):
    pass

#
# MARK: __init__()
#

class ShouldInstantiateABCParentSelector(ParentSelectorTestCase):
    def runTest(self):
        self.assertTrue(isinstance(ABCParentSelector(), ABCParentSelector))

#
# MARK: select(population)
#

class ShouldRaiseErrorOnInvalidPopulationWrongType(ParentSelectorTestCase):
    def runTest(self):
        sel = ABCParentSelector()
        with self.assertRaises(TypeError):
            sel.select('asdfasdfasdf')


class ShouldNotRaiseErrorOnValidPopulationList(ParentSelectorTestCase):
    def runTest(self):
        sel = ABCParentSelector()
        self.assertIsNone(sel.select([]))


class ShouldNotRaiseErrorOnValidPopulationArray(ParentSelectorTestCase):
    def runTest(self):
        sel = ABCParentSelector()
        self.assertIsNone(sel.select(array([])))
