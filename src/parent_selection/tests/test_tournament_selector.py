"""This module tests the tournament_selector module."""
import unittest
from numpy import array
from ..tournament_selector import *


#
# MARK: Abstract Base Class
#


class TournamentSelectorTestCase(unittest.TestCase):
    pass

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
