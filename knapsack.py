"""The 0-1 Knapsack Problem (Combinatorial Optimization)
This module solves the knapsack problem using evolutionary components.

## Given

*   a container of maximum capacity $c$
*   a set of items each with:
    *   a weight $w$
    *   a value $v$

## Determine

the subset of items that fits in the container such that the value of the
subset is maximized.
"""
# evolutionary is designed to be imported with a wildcard
from src import *
# evolutionary is designed around numpy!
import numpy as np
from numpy.random import seed
from random import shuffle


# setup random seed from the command line
try:
    from sys import argv
    seed(int(argv[1]))
except:
    seed(10)


# the number of items in the bag (also the size of the binary chromosome)
SIZE = 1000
# the base value for values of objects in the bag
BASE_VALUE = 100
# the value mapping for the objects
VALUES = (np.random.random_sample(size=SIZE) * BASE_VALUE).astype(int)
# the base weight for generating weights randomly
BASE_WEIGHT = 1000
# the weight mapping for the objects
WEIGHTS = (np.random.random_sample(size=SIZE) * BASE_WEIGHT).astype(int)
# the sum of all the weights (total weight of all objects)
WEIGHTS_SUM = np.sum(WEIGHTS)
# reduces the bag size to a proportion of the mean value for each object
BAG_SIZE_FACTOR = 1 / 3
# the size of the bag based on the mean weight, number of items to select from,
# and the bag size factor
BAG_SIZE = int(SIZE * WEIGHTS.mean() * BAG_SIZE_FACTOR)


print('(scores)   V = {}'.format(VALUES))
print('(weights)  W = {}'.format(WEIGHTS))
print('(bag size) c = {}'.format(BAG_SIZE))


def evaluate(genes: np.array) -> float:
    """
    Evaluate the genes in a chromosome normalize about bagsize.

    Args:
        genes: the genes to decode and evauate

    Returns: the score. + if scored, - if overweight
    """
    # make sure the chromosome holds the contraint that the total weight is
    # less than the maximum weight
    if np.sum(genes * WEIGHTS) > BAG_SIZE:
        # use the weight normalized about 1 to weight the bagsize
        return BAG_SIZE * (1 - np.sum(genes * WEIGHTS) / WEIGHTS_SUM)
    # conditions have passed so we can score the items based on their values
    return np.sum(genes * VALUES) + BAG_SIZE


# MARK: Initial Population
factory = ChromosomeFactory(BinaryChromosome, SIZE,
                            evaluate=evaluate,
                            initial_state='random')
population = factory.population(20)

print('initial population')
print(max([ind.fitness for ind in population]))
# for individual in population:
#     print('{}: {}'.format(individual, individual.fitness))





# generational
def generational_algorithm(population: list,
                           parent_selector: ABCParentSelector,
                           procreator: CrossoverProcreatorABC,
                           mutator: MutationProcreatorABC,
                           iterations: int = 2000):
    """A generalized form of the evolutionary algorithm."""
    # iterate from the size of the population up to the number of iterations
    for iteration in range(len(population), iterations):
        # randomly select some parents using the parent_selector provided
        parents = parent_selector.select(population)
        # randomly procreate using the procreator
        children = procreator.procreate(parents)
        # mutate the child using the mutator
        mutated_children = mutator.mutate(children)
        # Generational algorithm, replace parents with children
        [population.remove(parent) for parent in parents if parent in population]
        # add the mutated children to the list
        population += mutated_children


# parent_selector = TournamentSelector(size=2, replace=False, individuals_per_tournament=3)
# procreator = NPointCrossoverProcreator(crossovers=1)
# mutator = BinaryMutationProcreator(mutation_rate=0.005)
# survivor_selector = GenerationalSurvivorSelector()
# generational_algorithm(population, parent_selector, procreator, mutator)





# \mu + \mu replacement
def mu_mu_algorithm(population: list,
                    parent_selector: ABCParentSelector,
                    procreator: CrossoverProcreatorABC,
                    mutator: MutationProcreatorABC,
                    iterations: int = 2000):
    """A generalized form of the evolutionary algorithm."""
    # iterate from the size of the population up to the number of iterations
    for iteration in range(len(population), iterations):
        # randomly select some parents using the parent_selector provided
        parents = parent_selector.select(population)
        # randomly procreate using the procreator
        children = procreator.procreate(parents)
        # mutate the child using the mutator
        mutated_children = mutator.mutate(children)
        # add the mutated children to the list and replace the worst individuals
        population.sort(key=lambda ind: ind.fitness, reverse=True)
        [population.pop() for _ in range(parent_selector.size)]
        population += mutated_children


parent_selector = TournamentSelector(size=2, replace=False, individuals_per_tournament=3)
procreator = NPointCrossoverProcreator(crossovers=1)
mutator = BinaryMutationProcreator(mutation_rate=0.05)
survivor_selector = MuMuSurvivorSelector()
mu_mu_algorithm(population, parent_selector, procreator, mutator)




print('final population')
print(max([ind.fitness for ind in population]))
# for individual in population:
#     print('{}: {}'.format(individual, individual.fitness))




def evolve(population: list,
           parent_selector: ABCParentSelector,
           procreator: CrossoverProcreatorABC,
           mutator: MutationProcreatorABC,
           survivor_selector: SurvivorSelectorABC,
           iterations: int = 2000):
    """A generalized form of the evolutionary algorithm."""
    for iteration in range(len(population), iterations):
        parents = parent_selector.select(population)
        children = procreator.procreate(parents)
        mutator.mutate(children, inplace=True)
        population = survivor_selector.select(population, parents, children)
    return population
