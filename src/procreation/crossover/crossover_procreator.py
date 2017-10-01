"""This module contains the crossover procreator abstract base class."""


class CrossoverProcreatorABC:
    """This class is an abstract base class for crossover procreators."""

    def procreate(self, parents: list) -> list:
        """
        Args:
            parents: the list of parents to select from
            crossovers: the number of crossovers to perform
        """
        # verify that there are at least 2 parents
        if len(parents) < 2:
            raise ValueError('crossovers must have at least 2 parents')


# explicitly specify exports
__all__ = [
    'CrossoverProcreatorABC'
]
