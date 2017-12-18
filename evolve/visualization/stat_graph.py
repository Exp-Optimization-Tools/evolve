"""A graph utility for showing the progress of an elite during a GA."""
import pylab as plt
import numpy as np
from IPython import display


class StatGraph(object):
    """
    A class for graphing the stats of a population.

    Usage:
        # default for Jupyter environment (will use mean and std)
        graph = StatGraph()
        # non jupyter environment
        graph = StatGraph(is_jupyter=False)
        # minimize instead of maximize (can use any metric from numpy)
        graph = StatGraph(measures={'mean', 'max', 'min', 'std'})

        # usage in a GA callback
        ga = GeneticAlgorithm(...)
        ga(..., callback=graph.update)
    """

    def __init__(self,
                 is_jupyter: bool=True,
                 xlabel: str='Generation',
                 ylabel: str='Fitness',
                 measures: set={'mean', 'std'}):
        """
        Initialize a new elite graph.

        Args:
            is_jupyter: whether using a jupyter notebook (default True)
            xlabel: the string to display on the x axis (default 'Generation')
            ylabel: the string to display on the y axis (default 'Fitness')
            measures: a set of measures to use in the graph (default {'mean', 'std'})
        """
        if not isinstance(is_jupyter, (bool)):
            raise TypeError('is_jupyter must be of type: bool')
        if not isinstance(xlabel, str):
            raise TypeError('xlabel must be of type: str')
        if not isinstance(ylabel, str):
            raise TypeError('ylabel must be of type: str')
        if not isinstance(measures, (set, list, tuple)):
            raise TypeError('measures must be a set of numpy methods')
        # ensure each measure is valid
        for measure in measures:
            try:
                # getattr will raise and AttributeError if the measure isn't
                # a member of numpy
                # calling the attribute will raise an error if the numpy
                # method doesn't conform to the expected signature
                getattr(np, measure)([0, 1])
            except Exception:
                # catching the general exception and raising a new one to alert
                # the user of the incorrent usage of the member
                raise TypeError('measures must be a set of numpy methods')
        self.is_jupyter = is_jupyter
        self.measures = set(measures)
        self.xlabel = xlabel
        self.ylabel = ylabel
        # unwrap the numpy methods
        self.np_measures = {measure: getattr(np, measure) for measure in self.measures}
        # build a dictionary for the results to store into
        self.measurements = {measure: [] for measure in self.measures}

    def update(self, population: list, generation: int):
        """
        Add the elite individuals fitness to the the plot.

        Args:
            population: the population of individuals representing a generation
            generations: the number of generations that have passed

        Returns: None
        """
        # measure the fitness of each individual
        fitnesses = [ind.fitness for ind in population]
        # iterate over each statistic measure and take it
        for measure, totals in self.measurements.items():
            # append to the totals for this measure the value for this gen
            totals.append(self.np_measures[measure](fitnesses))
            # plot this measurements line
            plt.plot(totals)
        # add the x and y labels to the plot
        plt.xlabel(self.xlabel)
        plt.ylabel(self.ylabel)
        # add a legend to the plot
        plt.legend(self.measures)
        if self.is_jupyter:
            # clear the jupyter output to animate the plot
            display.clear_output(wait=True)
        # show the plot on the fresh canvas
        plt.show()


# export the classes manually to keep internal garbage from being exported
__all__ = [
    'StatGraph'
]
