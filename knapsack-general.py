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

# print('initial population')
# print(max([ind.fitness for ind in population]))
# for individual in population:
#     print('{}: {}'.format(individual, individual.fitness))

# generational replacement
parent_selector = TournamentSelector(size=2, replace=False, individuals_per_tournament=3)
procreator = NPointCrossoverProcreator(crossovers=1)
mutator = BinaryMutationProcreator(mutation_rate=0.005)
survivor_selector = GenerationalSurvivorSelector()
generational = Evolutionary(parent_selector, procreator, mutator, survivor_selector)
gen_pop = generational.evolve(population, iterations=2000)

# (mu, mu) replacement
parent_selector = TournamentSelector(size=2, replace=False, individuals_per_tournament=3)
procreator = NPointCrossoverProcreator(crossovers=1)
mutator = BinaryMutationProcreator(mutation_rate=0.05)
survivor_selector = MuMuSurvivorSelector(mu=parent_selector.size)
mu_mu = Evolutionary(parent_selector, procreator, mutator, survivor_selector)
mu_mu_pop = mu_mu.evolve(population, iterations=2000)
