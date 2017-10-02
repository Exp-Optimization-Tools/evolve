"""A module containing an implementation of generational replacement."""
from .survivor_selector import SurvivorSelectorABC


class GenerationalSurvivorSelector(SurvivorSelectorABC):
    """A class for selecting survivors generationally."""


# explicitly specify exports
__all__ = [
    'GenerationalSurvivorSelector'
]
