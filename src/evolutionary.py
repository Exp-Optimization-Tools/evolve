"""An implementation of the generalized evolutionary computation."""
from .parent_selection import ABCParentSelector
from .procreation import CrossoverProcreatorABC, MutationProcreatorABC
from .survivor_selection import SurvivorSelectorABC


class Evolutionary:
    """An implementation of the generalized evolutionary computation."""

    def __init__(self,
                 parent_selector: ABCParentSelector,
                 procreator: CrossoverProcreatorABC,
                 mutator: MutationProcreatorABC,
                 survivor_selector: SurvivorSelectorABC):
        """
        Initialize a new Evolutionary aglorithm

        Args:
            parent_selector: the selector for picking parents
            procreator: the precreator for making children
            mutator: the mutator for mutating children
            survivor_selector: the selector for picking survivors
        """
        # type check parameters
        if not isinstance(parent_selector, ABCParentSelector):
            raise TypeError('parent_selector must be type ABCParentSelector!')
        if not isinstance(procreator, CrossoverProcreatorABC):
            raise TypeError('procreator must be type CrossoverProcreatorABC!')
        if not isinstance(mutator, MutationProcreatorABC):
            raise TypeError('mutator must be type MutationProcreatorABC!')
        if not isinstance(survivor_selector, SurvivorSelectorABC):
            raise TypeError('survivor_selector must be type SurvivorSelectorABC!')
        # assign instance members
        self.parent_selector = parent_selector
        self.procreator = procreator
        self.mutator = mutator
        self.survivor_selector = survivor_selector

    def evolve(self, population: list, iterations: int = 2000):
        """
        Evolve the population for the given number of iterations.

        Args:
            population: the population to evolve
            iterations: the number of iterations to run (default 2000)
        """
        # iterate from initial population size to iterations
        for iteration in range(len(population), iterations):
            # select parents
            PARENTS = self.parent_selector.select(population)
            # procreate children
            children = self.procreator.procreate(PARENTS)
            # mutate the children
            self.mutator.mutate(children, inplace=True)
            # select survivors in the population
            population = self.survivor_selector.select(population, PARENTS, children)
        return population


# explicitly specify exports from module
__all__ = [
    'Evolutionary'
]
