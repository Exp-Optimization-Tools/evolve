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


class ShouldCreateChromosomeFactoryInitializationString(TestCase):
    def test(self):
        ChromosomeFactory(10, dummy_decode, dummy_evaluate, 'random')


class ShouldCreateChromosomeFactoryInitializationTuple(TestCase):
    def test(self):
        ChromosomeFactory(10, dummy_decode, dummy_evaluate, (0, 1))


#
# MARK: next_individual
#


# class ShouldCreateChromosomeFromFactory(ChromosomeFactoryTestCase):
#     def test(self):
#         factory = ChromosomeFactory(5, dummy_decode, dummy_evaluate)
#
#
# class ShouldCreateBinaryChromosomeFromFactory(ChromosomeFactoryTestCase):
#     def test(self):
#         factory = ChromosomeFactory(5, dummy_decode, dummy_evaluate, 'zeros')
#
#
# class ShouldCreateBinaryChromosomeFromFactory(ChromosomeFactoryTestCase):
#     def test(self):
#         factory = ChromosomeFactory(5, dummy_decode, dummy_evaluate, 'ones')
#
#
# class ShouldCreateRealCodedChromosomeFromFactory(ChromosomeFactoryTestCase):
#     def test(self):
#         factory = ChromosomeFactory(5, dummy_decode, dummy_evaluate, (1, 2))
#         self.assertTrue(isinstance(factory.next_individual, RealCodedChromosome))
#         for gene in factory.next_individual.genes:
#             self.assertTrue(gene >= 1)
#             self.assertTrue(gene <= 2)
