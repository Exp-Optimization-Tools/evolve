"""Test cases for the ChromosomeFactory class."""
from unittest import TestCase
import numpy as np
from ..factory import ChromosomeFactory
from ..factory import zeros, ones, random_sample, uniform_binary
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


class ShouldRaiseErrorOnInvalidValueChromosomeSizeNegative(TestCase):
    def test(self):
        with self.assertRaises(ValueError):
            ChromosomeFactory(-1, dummy_decode, dummy_evaluate)


class ShouldRaiseErrorOnInvalidValueChromosomeSizeZero(TestCase):
    def test(self):
        with self.assertRaises(ValueError):
            ChromosomeFactory(0, dummy_decode, dummy_evaluate)


class ShouldRaiseErrorOnInvalidTypeDecode(TestCase):
    def test(self):
        with self.assertRaises(TypeError):
            ChromosomeFactory(10, 'asdf', dummy_evaluate)


def invalid_method():
    pass


def invalid_evaluate_return_type(genes):
    return 'asdf'


class ShouldRaiseErrorOnInvalidValueDecode(TestCase):
    def test(self):
        with self.assertRaises(ValueError):
            ChromosomeFactory(10, invalid_method, dummy_evaluate)


class ShouldRaiseErrorOnInvalidTypeEvaluate(TestCase):
    def test(self):
        with self.assertRaises(TypeError):
            ChromosomeFactory(10, dummy_decode, 'asdf')


class ShouldRaiseErrorOnInvalidValueEvaluate(TestCase):
    def test(self):
        with self.assertRaises(ValueError):
            ChromosomeFactory(10, dummy_decode, invalid_method)


class ShouldRaiseErrorOnInvalidValueEvaluateReturn(TestCase):
    def test(self):
        with self.assertRaises(ValueError):
            ChromosomeFactory(10, dummy_decode, invalid_evaluate_return_type)


class ShouldRaiseErrorOnInvalidTypeInitialization(TestCase):
    def test(self):
        with self.assertRaises(TypeError):
            ChromosomeFactory(10, dummy_decode, dummy_evaluate, 6)


class ShouldCreateChromosomeFactory(TestCase):
    def test(self):
        ChromosomeFactory(10, dummy_decode, dummy_evaluate)


#
# MARK: next_individual
#


class ShouldCreateChromosomeFromFactoryUniformBinary(TestCase):
    def test(self):
        np.random.seed(15)
        factory = ChromosomeFactory(5, dummy_decode, dummy_evaluate, uniform_binary)
        actual = factory.next_chromosome.alleles
        expected = np.array([0, 0, 1, 1, 1])
        print(actual)
        self.assertTrue(np.array_equiv(expected, actual))


class ShouldCreateChromosomeFromFactoryRandomSample(TestCase):
    def test(self):
        np.random.seed(1)
        factory = ChromosomeFactory(5, dummy_decode, dummy_evaluate)
        actual = factory.next_chromosome.alleles
        expected = np.array([0.09233859,
                             0.18626021,
                             0.34556073,
                             0.39676747,
                             0.53881673])
        actual = np.around(1000 * actual)
        expected = np.around(1000 * expected)
        self.assertTrue(np.array_equiv(expected, actual))


class ShouldCreateZerosChromosomeFromFactory(TestCase):
    def test(self):
        np.random.seed(2)
        factory = ChromosomeFactory(5, dummy_decode, dummy_evaluate, zeros)


class ShouldCreateOnesChromosomeFromFactory(TestCase):
    def test(self):
        np.random.seed(3)
        factory = ChromosomeFactory(5, dummy_decode, dummy_evaluate, ones)
