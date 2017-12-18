"""Test cases for the chromosome class."""
from unittest import TestCase
import numpy as np
from .._chromosome import Chromosome


def dummy_decode(genes: np.ndarray):
    """A dummy decoder that returns the genotype"""
    return genes


def dummy_evaluate(phenotype: np.ndarray):
    """A dummy evaluater that returns the sum of the CS"""
    return phenotype.sum()


#
# MARK: init
#


class init_ShouldRaiseErrorNoGenes(TestCase):
    def test(self):
        with self.assertRaises(TypeError):
            Chromosome()


class init_ShouldRaiseErrorNoDecode(TestCase):
    def test(self):
        with self.assertRaises(TypeError):
            Chromosome(np.array([0]))


class init_ShouldRaiseErrorNoEvalaute(TestCase):
    def test(self):
        with self.assertRaises(TypeError):
            Chromosome(np.array([0]), dummy_decode)


class init_ShouldCreateInstance(TestCase):
    def test(self):
        alleles = np.array([1, 1, 1])
        inst = Chromosome(alleles, dummy_decode, dummy_evaluate)
        self.assertIsInstance(inst, Chromosome)
        self.assertTrue(np.array_equiv(np.array([0, 1, 2]), inst.genes))
        self.assertTrue(np.array_equiv(alleles, inst.alleles))
        self.assertTrue(np.array_equiv(alleles, inst.phenotype))
        self.assertTrue(np.array_equiv(3, inst.fitness))


def arb_chromosome():
    """Return a simple arbitrary chromosome"""
    alleles = np.array([1, 1, 1])
    return Chromosome(alleles, dummy_decode, dummy_evaluate)


#
# MARK: repr
#


class repr_ShouldReturnRepresentation(TestCase):
    def test(self):
        arb = arb_chromosome()
        _repr = 'Chromosome(alleles=[ 1.  1.  1.], decode=dummy_decode, evaluate=dummy_evaluate)'
        self.assertEqual(_repr, repr(arb))


#
# MARK: str
#


class str_ShouldReturnRepresentation(TestCase):
    def test(self):
        arb = arb_chromosome()
        _str = '3.0'
        self.assertEqual(_str, str(arb))


#
# MARK: len
#


class len_ShouldReturnLength(TestCase):
    def test(self):
        arb = arb_chromosome()
        self.assertEqual(3, len(arb))


#
# MARK: comparisons
#


class lt_ShouldCompare(TestCase):
    def test(self):
        a = Chromosome(np.array([1, 1, 1]), dummy_decode, dummy_evaluate)
        b = Chromosome(np.array([2, 2, 2]), dummy_decode, dummy_evaluate)
        self.assertTrue(a < b)
        self.assertFalse(b < a)


class lte_ShouldCompare(TestCase):
    def test(self):
        a = Chromosome(np.array([1, 1, 1]), dummy_decode, dummy_evaluate)
        b = Chromosome(np.array([2, 2, 2]), dummy_decode, dummy_evaluate)
        self.assertTrue(a <= b)
        self.assertFalse(b <= a)
        c = Chromosome(np.array([1, 1, 1]), dummy_decode, dummy_evaluate)
        self.assertTrue(a <= c)
        self.assertTrue(c <= a)


class gt_ShouldCompare(TestCase):
    def test(self):
        a = Chromosome(np.array([1, 1, 1]), dummy_decode, dummy_evaluate)
        b = Chromosome(np.array([2, 2, 2]), dummy_decode, dummy_evaluate)
        self.assertFalse(a > b)
        self.assertTrue(b > a)


class gte_ShouldCompare(TestCase):
    def test(self):
        a = Chromosome(np.array([1, 1, 1]), dummy_decode, dummy_evaluate)
        b = Chromosome(np.array([2, 2, 2]), dummy_decode, dummy_evaluate)
        self.assertFalse(a >= b)
        self.assertTrue(b >= a)
        c = Chromosome(np.array([1, 1, 1]), dummy_decode, dummy_evaluate)
        self.assertTrue(a >= c)
        self.assertTrue(c >= a)


class equal_ShouldCompare(TestCase):
    def test(self):
        a = Chromosome(np.array([1, 1, 1]), dummy_decode, dummy_evaluate)
        b = Chromosome(np.array([2, 2, 2]), dummy_decode, dummy_evaluate)
        self.assertFalse(a == b)
        c = Chromosome(np.array([1, 1, 1]), dummy_decode, dummy_evaluate)
        self.assertTrue(c == a)


class not_equal_ShouldCompare(TestCase):
    def test(self):
        a = Chromosome(np.array([1, 1, 1]), dummy_decode, dummy_evaluate)
        b = Chromosome(np.array([2, 2, 2]), dummy_decode, dummy_evaluate)
        self.assertTrue(a != b)
        c = Chromosome(np.array([1, 1, 1]), dummy_decode, dummy_evaluate)
        self.assertFalse(c != a)


#
# MARK: subscript functionality
#


class subscript_ShouldFetch(TestCase):
    def test(self):
        arb = arb_chromosome()
        self.assertEqual(1, arb[0])
        self.assertEqual(1, arb[0])
        self.assertEqual(1, arb[0])
        self.assertEqual(1, arb[-1])
        self.assertEqual(1, arb[-2])
        with self.assertRaises(IndexError):
            arb[4]
        with self.assertRaises(IndexError):
            arb[-4]
        self.assertTrue(np.array_equiv(np.array([1, 1, 1]), arb[0:3]))


class subscript_ShouldIterate(TestCase):
    def test(self):
        arb = arb_chromosome()
        for allele in arb:
            self.assertEqual(1, allele)


#
# MARK: in keyword functionality (contains)
#


class key_in_ShouldReturn(TestCase):
    def test(self):
        arb = arb_chromosome()
        self.assertNotIn(-1, arb)
        self.assertIn(0, arb)
        self.assertIn(1, arb)
        self.assertIn(2, arb)
        self.assertNotIn(3, arb)


#
# MARK: class variables
#


class is_phenotype_cache_enabled_ShouldToggle(TestCase):
    def test(self):
        Chromosome.is_phenotype_cache_enabled = True
        self.assertTrue(Chromosome.is_phenotype_cache_enabled)
        arb = arb_chromosome()
        self.assertTrue(arb.is_phenotype_cache_enabled)
        Chromosome.is_phenotype_cache_enabled = False
        self.assertFalse(arb.is_phenotype_cache_enabled)


class _phenotype_cache_ShouldUse(TestCase):
    def test(self):
        Chromosome.is_phenotype_cache_enabled = True
        arb = arb_chromosome()
        self.assertIsNone(arb._phenotype_cache)
        _ = arb.phenotype
        phenotype = np.array([1, 1, 1])
        self.assertTrue(np.array_equiv(phenotype,
                                       arb._phenotype_cache))


class _phenotype_cache_ShouldIgnore(TestCase):
    def test(self):
        Chromosome.is_phenotype_cache_enabled = False
        arb = arb_chromosome()
        self.assertIsNone(arb._phenotype_cache)
        _ = arb.phenotype
        self.assertIsNone(arb._phenotype_cache)


class _fitness_cache_ShouldUse(TestCase):
    def test(self):
        Chromosome.is_fitness_cache_enabled = True
        arb = arb_chromosome()
        self.assertIsNone(arb._fitness_cache)
        _ = arb.fitness
        fitness = 3
        self.assertEqual(fitness, arb._fitness_cache)


class _fitness_cache_ShouldIgnore(TestCase):
    def test(self):
        Chromosome.is_fitness_cache_enabled = False
        arb = arb_chromosome()
        self.assertIsNone(arb._fitness_cache)
        _ = arb.fitness
        self.assertIsNone(arb._fitness_cache)


class is_fitness_cache_enabled_ShouldToggle(TestCase):
    def test(self):
        Chromosome.is_fitness_cache_enabled = True
        self.assertTrue(Chromosome.is_fitness_cache_enabled)
        arb = arb_chromosome()
        self.assertTrue(arb.is_fitness_cache_enabled)
        Chromosome.is_fitness_cache_enabled = False
        self.assertFalse(arb.is_fitness_cache_enabled)
