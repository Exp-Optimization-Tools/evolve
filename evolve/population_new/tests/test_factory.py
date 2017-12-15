"""Test cases for the ChromosomeFactory class."""
from unittest import TestCase
import numpy as np
from ..factory import ChromosomeFactory
# from .._chromosome import Chromosome


def dummy_decode(genes: np.ndarray):
    """A dummy decoder that returns the genotype"""
    return genes


def dummy_evaluate(phenotype: np.ndarray):
    """A dummy evaluater that returns the sum of the CS"""
    return phenotype.sum()


#
# MARK: __init__()
#


class ShouldRaiseErrorOnMissingChromosomeSize(TestCase):
    def test(self):
        with self.assertRaises(TypeError):
            ChromosomeFactory()


class ShouldRaiseErrorOnMissingDecode(TestCase):
    def test(self):
        with self.assertRaises(TypeError):
            ChromosomeFactory(10)


class ShouldRaiseErrorOnMissingEvaluate(TestCase):
    def test(self):
        with self.assertRaises(TypeError):
            ChromosomeFactory(10, dummy_decode)


class ShouldRaiseErrorOnInvalidTypeChromosomeSize(TestCase):
    def test(self):
        with self.assertRaises(TypeError):
            ChromosomeFactory('asdf', dummy_decode, dummy_evaluate)


class ShouldRaiseErrorOnInvalidTypeDecode(TestCase):
    def test(self):
        with self.assertRaises(TypeError):
            ChromosomeFactory(10, 'asdf', dummy_evaluate)


class ShouldRaiseErrorOnInvalidTypeEvaluate(TestCase):
    def test(self):
        with self.assertRaises(TypeError):
            ChromosomeFactory(10, dummy_decode, 'asdf')


class ShouldRaiseErrorOnInvalidTypeInitialization(TestCase):
    def test(self):
        with self.assertRaises(TypeError):
            ChromosomeFactory(10, dummy_decode, dummy_evaluate, 6)


class ShouldCreateChromosomeFactory(TestCase):
    def test(self):
        ChromosomeFactory(10, dummy_decode, dummy_evaluate)


class ShouldCreateChromosomeFactoryInitializationString(TestCase):
    def test(self):
        ChromosomeFactory(10, dummy_decode, dummy_evaluate, 'random')


class ShouldCreateChromosomeFactoryInitializationTuple(TestCase):
    def test(self):
        ChromosomeFactory(10, dummy_decode, dummy_evaluate, (0, 1))
