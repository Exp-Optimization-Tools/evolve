"""This package contains classes for selecting parents from a population."""
from .parent_selector import ABCParentSelector
from .proportionate_selector import ProportionateSelector
from .linear_rank_selector import LinearRankSelector
from .tournament_selector import TournamentSelector
# TODO: move the replacement boolean to an instance method to allow for more
#       customization without impacting generality of the algorithm at the
#       frontend of the API
