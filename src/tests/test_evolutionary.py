"""Test cases for the Evolutionary class."""
from unittest import TestCase
from src.evolutionary import *
from src.parent_selection import *
from src.procreation import *
from src.survivor_selection import *


#
# MARK: init
#


class init_ShouldRaiseErrorOnMissingParameters0(TestCase):
    def test(self):
        with self.assertRaises(TypeError):
            Evolutionary()


class init_ShouldRaiseErrorOnMissingParameters1(TestCase):
    def test(self):
        with self.assertRaises(TypeError):
            Evolutionary(ABCParentSelector())


class init_ShouldRaiseErrorOnMissingParameters2(TestCase):
    def test(self):
        with self.assertRaises(TypeError):
            Evolutionary(ABCParentSelector(),
                         CrossoverProcreatorABC())


class init_ShouldRaiseErrorOnMissingParameters3(TestCase):
    def test(self):
        with self.assertRaises(TypeError):
            Evolutionary(ABCParentSelector(),
                         CrossoverProcreatorABC(),
                         MutationProcreatorABC(mutation_rate=1))


class init_ShouldInitializeOject(TestCase):
    def test(self):
        Evolutionary(ABCParentSelector(),
                     CrossoverProcreatorABC(),
                     MutationProcreatorABC(mutation_rate=1),
                     SurvivorSelectorABC())


class init_ShouldRaiseErrorOnInvalidType0(TestCase):
    def test(self):
        with self.assertRaises(TypeError):
            Evolutionary('asdf',
                         CrossoverProcreatorABC(),
                         MutationProcreatorABC(mutation_rate=1),
                         SurvivorSelectorABC())


class init_ShouldRaiseErrorOnInvalidType1(TestCase):
    def test(self):
        with self.assertRaises(TypeError):
            Evolutionary(ABCParentSelector(),
                         'asdf',
                         MutationProcreatorABC(mutation_rate=1),
                         SurvivorSelectorABC())


class init_ShouldRaiseErrorOnInvalidType2(TestCase):
    def test(self):
        with self.assertRaises(TypeError):
            Evolutionary(ABCParentSelector(),
                         CrossoverProcreatorABC(),
                         'asdf',
                         SurvivorSelectorABC())


class init_ShouldRaiseErrorOnInvalidType3(TestCase):
    def test(self):
        with self.assertRaises(TypeError):
            Evolutionary(ABCParentSelector(),
                         CrossoverProcreatorABC(),
                         MutationProcreatorABC(mutation_rate=1),
                         'asdf')
