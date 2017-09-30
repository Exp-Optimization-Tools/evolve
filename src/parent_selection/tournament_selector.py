"""This module contains a class for tournament parent selection."""
from .parent_selector import ABCParentSelector


class TournamentSelector(ABCParentSelector):
    """A class for performing tournament parent selection."""
