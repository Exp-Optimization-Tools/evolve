"""A generalized estimation of distribution algorithm."""


class EstimationOfDistributionAlgorithm(object):
    """A general estimation of distribution algorithm."""

    def __init__(self, population_size=20, num_elites=0, estimation_size=0.5):
        """
        Initialize a new Estimation of Distribution Algorithm.

        Args:
            population_size: the size of the population to evolve (default 20)
            num_elites: the number of elites to keep per generation (default 0)
            estimation_size: the percentage of top individuals to estimate the
                distribution of (default 0.5 (50%))
        """
        if not isinstance(population_size, (float, int)):
            raise TypeError('population_size must be of type: float, int')
        if not isinstance(num_elites, (float, int)):
            raise TypeError('num_elites must be of type: float, int')
        if not isinstance(estimation_size, (float, int)):
            raise TypeError('top_percentage must be of type: float, int')
        if population_size < 0:
            raise ValueError('population size must be positive')
        if num_elites < 0:
            raise ValueError('num_elites must be greater than or equal to 0')
        if estimation_size < 0 or estimation_size > 1:
            raise ValueError('estimation_size must be in the range [0, 1]')
        if num_elites >= population_size:
            raise ValueError('population_size must be greater than num_elites')
        self.population_size = int(population_size)
        self.num_elites = float(num_elites)
        self.estimation_size = float(estimation_size)

    # def _generate_population(self):
    #     """Generate and return a population."""
    #
    # def __call__(self):
    #     """Evolve a population."""
