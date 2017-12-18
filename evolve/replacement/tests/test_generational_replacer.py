"""A module with test code for the generational_selector module."""
from unittest import TestCase
from ..generational_replacer import *


#
# MARK: init
#


class init_ShouldInstantiate(TestCase):
    def test(self):
        GenerationalReplacer()


#
# MARK: select(population, parents, children)
#
