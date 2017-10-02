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


class ShouldRaiseErrorOnInvalidSizeType(ParentSelectorTestCase):
    def runTest(self):
        with self.assertRaises(TypeError):
            ABCParentSelector(size='asdf')


class ShouldRaiseErrorOnInvalidSizeBelowBounds(ParentSelectorTestCase):
    def runTest(self):
        with self.assertRaises(ValueError):
            ABCParentSelector(size=-1)


class ShouldInstantiateABCParentSelectorSize0(ParentSelectorTestCase):
    def runTest(self):
        self.assertTrue(isinstance(ABCParentSelector(size=0), ABCParentSelector))


class ShouldRaiseErrorOnInvalidReplaceType(ParentSelectorTestCase):
    def runTest(self):
        with self.assertRaises(TypeError):
            ABCParentSelector(replace='asdf')


class ShouldInstantiateABCParentSelectorReplaceTrue(ParentSelectorTestCase):
    def runTest(self):
        self.assertTrue(isinstance(ABCParentSelector(replace=True), ABCParentSelector))


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
