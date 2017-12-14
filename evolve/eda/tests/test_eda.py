"""Test cases for the eda module."""
from unittest import TestCase
from ..eda import EstimationOfDistributionAlgorithm


class ShouldCreateEDA(TestCase):
    def test(self):
        self.assertIsInstance(EstimationOfDistributionAlgorithm(),
                              EstimationOfDistributionAlgorithm)


class ShouldRaiseErrorPopulationSizeType(TestCase):
    def test(self):
        with self.assertRaises(TypeError):
            EstimationOfDistributionAlgorithm(population_size='asdf')


class ShouldRaiseErrorNumElitesType(TestCase):
    def test(self):
        with self.assertRaises(TypeError):
            EstimationOfDistributionAlgorithm(num_elites='asdf')


class ShouldRaiseErrorEstimationSizeType(TestCase):
    def test(self):
        with self.assertRaises(TypeError):
            EstimationOfDistributionAlgorithm(estimation_size='asdf')


class ShouldRaiseErrorPopulationSizeNegative(TestCase):
    def test(self):
        with self.assertRaises(ValueError):
            EstimationOfDistributionAlgorithm(population_size=-1)


class ShouldRaiseErrorNumElitesNegative(TestCase):
    def test(self):
        with self.assertRaises(ValueError):
            EstimationOfDistributionAlgorithm(num_elites=-1)


class ShouldRaiseErrorEstimationSizeBelowZero(TestCase):
    def test(self):
        with self.assertRaises(ValueError):
            EstimationOfDistributionAlgorithm(estimation_size=-1)


class ShouldRaiseErrorEstimationSizeAboveOne(TestCase):
    def test(self):
        with self.assertRaises(ValueError):
            EstimationOfDistributionAlgorithm(estimation_size=2)


class ShouldCreateEDAWithEstimationSizeOfZero(TestCase):
    def test(self):
        EstimationOfDistributionAlgorithm(estimation_size=0)


class ShouldCreateEDAWithEstimationSizeOfOne(TestCase):
    def test(self):
        EstimationOfDistributionAlgorithm(estimation_size=1)


class ShouldRaiseErrorPopulationSizeEqualNumElites(TestCase):
    def test(self):
        with self.assertRaises(ValueError):
            EstimationOfDistributionAlgorithm(population_size=5, num_elites=5)


class ShouldRaiseErrorPopulationSizeBelowNumElites(TestCase):
    def test(self):
        with self.assertRaises(ValueError):
            EstimationOfDistributionAlgorithm(population_size=5, num_elites=10)
