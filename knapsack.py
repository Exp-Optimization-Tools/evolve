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
# this is the size of the bag (the maximum cumulative weight it can hold)
BAG_SIZE = np.random.randint(low=200, high=500, size=1)[0]


print('(scores)   V = {}'.format(VALUES))
print('(weights)  W = {}'.format(WEIGHTS))
print('(bag size) c = {}'.format(BAG_SIZE))


def evaluate(genes: np.array) -> float:
    """
    Evaluate the genes in a chromosome.

    Args:
        genes: the genes to decode and evauate

    Returns: the score. + if scored, - if overweight
    """
    # make sure the chromosome holds the contraint that the total weight is
    # less than the maximum weight
    if np.sum(genes * WEIGHTS) > BAG_SIZE:
        # return the negative distance between the current weight and max, this
        # is likely better than a static return of -1 because it gives states
        # with a closer weight to the limit higher fitness (albeit a negative
        # one). this value is always negative
        return BAG_SIZE - np.sum(genes * WEIGHTS)
    # conditions have passed so we can score the items based on their values
    return np.sum(genes * VALUES)


# MARK: Initial Population
factory = ChromosomeFactory(BinaryChromosome, SIZE,
                            evaluate=evaluate,
                            initial_state='random')
population = Population(20, factory)

print('initial population')
for individual in population.individuals:
    print('{}: {}'.format(individual, individual.fitness))
