"""This module contains test code for the n_point_crossover module."""
import unittest
from population import BinaryChromosome
from ..n_point_crossover import *

#
# MARK: Abstract Base Class
#


class NPointCrossoverProcreatorTestCase(unittest.TestCase):
    pass

#
# MARK: __init__()
#

class ShouldRaiseErrorOnInvalidNType(NPointCrossoverProcreatorTestCase):
    def runTest(self):
        with self.assertRaises(TypeError):
            crossover = NPointCrossoverProcreator(crossovers='asdf')

class ShouldRaiseErrorOnInvalidNValue(NPointCrossoverProcreatorTestCase):
    def runTest(self):
        with self.assertRaises(ValueError):
            crossover = NPointCrossoverProcreator(crossovers=-1)

class ShouldCreateNPointCrossoverWithDefaultN(NPointCrossoverProcreatorTestCase):
    def runTest(self):
        crossover = NPointCrossoverProcreator()
        self.assertEqual(1, crossover.crossovers)

class ShouldCreateNPointCrossoverWithN0(NPointCrossoverProcreatorTestCase):
    def runTest(self):
        crossover = NPointCrossoverProcreator(crossovers=0)
        self.assertEqual(0, crossover.crossovers)

class ShouldCreateNPointCrossoverWithN3(NPointCrossoverProcreatorTestCase):
    def runTest(self):
        crossover = NPointCrossoverProcreator(crossovers=3)
        self.assertEqual(3, crossover.crossovers)

#
# MARK: procreate
#

def arb_eval(genes):
    return 0

zeros = BinaryChromosome(size=5, initial_state='zeros', evaluate=arb_eval)
ones = BinaryChromosome(size=5, initial_state='ones', evaluate=arb_eval)


class ShouldRaiseErrorOnNoParents(NPointCrossoverProcreatorTestCase):
    def runTest(self):
        crossover = NPointCrossoverProcreator()
        with self.assertRaises(ValueError):
            crossover.procreate([])

class ShouldRaiseErrorOnTooFewParents(NPointCrossoverProcreatorTestCase):
    def runTest(self):
        crossover = NPointCrossoverProcreator()
        with self.assertRaises(ValueError):
            crossover.procreate([ones])

class ShouldPerform0PointCrossover(NPointCrossoverProcreatorTestCase):
    def runTest(self):
        crossover = NPointCrossoverProcreator(crossovers=0)
        child = crossover.procreate([ones, zeros])
        self.assertEqual([1,1,1,1,1], list(child.genes))

class ShouldPerform1PointCrossover(NPointCrossoverProcreatorTestCase):
    def runTest(self):
        crossover = NPointCrossoverProcreator(crossovers=1)
        for i in range(0, 10):
            child = crossover.procreate([ones, zeros])
            self.assertTrue(child.genes.sum() >= 1)
            self.assertTrue(child.genes.sum() <= 4)

class ShouldPerform2PointCrossover(NPointCrossoverProcreatorTestCase):
    def runTest(self):
        crossover = NPointCrossoverProcreator(crossovers=2)
        for i in range(0, 10):
            child = crossover.procreate([ones, zeros])
            self.assertTrue(child.genes.sum() >= 2)
            self.assertTrue(child.genes.sum() <= 4)

class ShouldPerform3PointCrossover(NPointCrossoverProcreatorTestCase):
    def runTest(self):
        crossover = NPointCrossoverProcreator(crossovers=3)
        for i in range(0, 10):
            child = crossover.procreate([ones, zeros])
            self.assertTrue(child.genes.sum() >= 2)
            self.assertTrue(child.genes.sum() <= 3)

class ShouldPerform4PointCrossover(NPointCrossoverProcreatorTestCase):
    def runTest(self):
        crossover = NPointCrossoverProcreator(crossovers=4)
        child = crossover.procreate([ones, zeros])
        self.assertEqual([1,0,1,0,1], list(child.genes))

class ShouldRaiseErrorOn5PointCrossover(NPointCrossoverProcreatorTestCase):
    def runTest(self):
        crossover = NPointCrossoverProcreator(crossovers=5)
        with self.assertRaises(ValueError):
            crossover.procreate([ones, zeros])
