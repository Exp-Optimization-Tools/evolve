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
seed(10)


# MARK: Evaluation Function
# evaluation functions are specified by the developer to allow max
# customization
#

# this is the size of the chromosome (number of items in the bag)
SIZE = 10
# this is the list of values V for items in the bag
VALUES = np.random.randint(low=1, high=100, size=SIZE)
# this is the list of weights W for items in the bag
WEIGHTS = np.random.randint(low=50, high=100, size=SIZE)
WEIGHTS_SUM = np.sum(WEIGHTS)
# this is the size of the bag (the maximum cumulative weight it can hold)
BAG_SIZE = np.random.randint(low=200, high=500, size=1)[0]


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
for individual in population:
    print('{}: {}'.format(individual, individual.fitness))


def evolutionary_algorithm(population: np.ndarray,
                           parent_selector: ABCParentSelector,
                           parents_per_iteration: int = 2,
                           iterations: int = 4000):
    """A generalized form of the evolutionary algorithm."""
    # iterate from the size of the population up to the number of iterations
    for iteration in range(len(population), iterations):
        # randomly select 2 parents using the parent_selector provided
        parents = parent_selector.select(population, size=parents_per_iteration)

evolutionary_algorithm(population, TournamentSelector(3))
