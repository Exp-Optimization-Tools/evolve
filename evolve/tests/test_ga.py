"""Test cases for the GeneticAlgorithm class."""
from unittest import TestCase
from evolve.ga import *
from evolve.operators.selection import Selector
from evolve.operators.procreation import Procreator
from evolve.operators.mutation import Mutator
from evolve.operators.replacement import Replacer


#
# MARK: init
#


class init_ShouldRaiseErrorOnMissingParameters0(TestCase):
    def test(self):
        with self.assertRaises(TypeError):
            GeneticAlgorithm()


class init_ShouldRaiseErrorOnMissingParameters1(TestCase):
    def test(self):
        with self.assertRaises(TypeError):
            GeneticAlgorithm(Selector())


class init_ShouldRaiseErrorOnMissingParameters2(TestCase):
    def test(self):
        with self.assertRaises(TypeError):
            GeneticAlgorithm(Selector(),
                             Procreator())


class init_ShouldRaiseErrorOnMissingParameters3(TestCase):
    def test(self):
        with self.assertRaises(TypeError):
            GeneticAlgorithm(Selector(),
                             Procreator(),
                             Mutator(mutation_rate=1))


class init_ShouldInitializeOject(TestCase):
    def test(self):
        GeneticAlgorithm(Selector(),
                         Procreator(),
                         Mutator(mutation_rate=1),
                         Replacer())


class init_ShouldInitializeOjectWitNoMutator(TestCase):
    def test(self):
        GeneticAlgorithm(Selector(),
                         Procreator(),
                         None,
                         Replacer())


class init_ShouldRaiseErrorOnInvalidType0(TestCase):
    def test(self):
        with self.assertRaises(TypeError):
            GeneticAlgorithm('asdf',
                             Procreator(),
                             Mutator(mutation_rate=1),
                             Replacer())


class init_ShouldRaiseErrorOnInvalidType1(TestCase):
    def test(self):
        with self.assertRaises(TypeError):
            GeneticAlgorithm(Selector(),
                             'asdf',
                             Mutator(mutation_rate=1),
                             Replacer())


class init_ShouldRaiseErrorOnInvalidType2(TestCase):
    def test(self):
        with self.assertRaises(TypeError):
            GeneticAlgorithm(Selector(),
                             Procreator(),
                             'asdf',
                             Replacer())


class init_ShouldRaiseErrorOnInvalidType3(TestCase):
    def test(self):
        with self.assertRaises(TypeError):
            GeneticAlgorithm(Selector(),
                             Procreator(),
                             Mutator(mutation_rate=1),
                             'asdf')

#
# MARK: evolve
#
