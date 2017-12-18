"""A module with test code for the survivor_selector module."""
from unittest import TestCase
from numpy import array
from ..replacer import *


#
# MARK: init
#


class init_ShouldInstantiate(TestCase):
    def test(self):
        Replacer()


#
# MARK: select(population, parents, children)
#


class select_ShouldRaiseErrorMissingParameters0(TestCase):
    def test(self):
        sel = Replacer()
        with self.assertRaises(TypeError):
            sel.select([])


class select_ShouldRaiseErrorMissingParameters1(TestCase):
    def test(self):
        sel = Replacer()
        with self.assertRaises(TypeError):
            sel.select([], [])


class select_ShouldSelect0(TestCase):
    def test(self):
        sel = Replacer()
        sel.select([], [], [])


class select_ShouldRaiseErrorInvalidParameter0(TestCase):
    def test(self):
        sel = Replacer()
        with self.assertRaises(TypeError):
            sel.select('asdf', [], [])


class select_ShouldRaiseErrorInvalidParameter1(TestCase):
    def test(self):
        sel = Replacer()
        with self.assertRaises(TypeError):
            sel.select([], 'asdf', [])


class select_ShouldRaiseErrorInvalidParameter2(TestCase):
    def test(self):
        sel = Replacer()
        with self.assertRaises(TypeError):
            sel.select([], [], 'asdf')
