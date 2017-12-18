"""This module tests the parent_selector module."""
from unittest import TestCase
from numpy import array
from ..selector import Selector


#
# MARK: __init__()
#


class ShouldInstantiateSelector(TestCase):
    def runTest(self):
        self.assertTrue(isinstance(Selector(), Selector))


class ShouldRaiseErrorOnInvalidSizeType(TestCase):
    def runTest(self):
        with self.assertRaises(TypeError):
            Selector(size='asdf')


class ShouldRaiseErrorOnInvalidSizeBelowBounds(TestCase):
    def runTest(self):
        with self.assertRaises(ValueError):
            Selector(size=-1)


class ShouldInstantiateSelectorSize0(TestCase):
    def runTest(self):
        self.assertTrue(isinstance(Selector(size=0), Selector))


class ShouldRaiseErrorOnInvalidReplaceType(TestCase):
    def runTest(self):
        with self.assertRaises(TypeError):
            Selector(replace='asdf')


class ShouldInstantiateSelectorReplaceTrue(TestCase):
    def runTest(self):
        self.assertTrue(isinstance(Selector(replace=True), Selector))


#
# MARK: select(population)
#


class ShouldRaiseErrorOnInvalidPopulationWrongType(TestCase):
    def runTest(self):
        sel = Selector()
        with self.assertRaises(TypeError):
            sel.select('asdfasdfasdf')


class ShouldNotRaiseErrorOnValidPopulationList(TestCase):
    def runTest(self):
        sel = Selector()
        self.assertIsNone(sel.select([]))


class ShouldNotRaiseErrorOnValidPopulationArray(TestCase):
    def runTest(self):
        sel = Selector()
        self.assertIsNone(sel.select(array([])))
