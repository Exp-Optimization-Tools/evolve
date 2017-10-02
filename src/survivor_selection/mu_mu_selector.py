"""A module containing an implementation of Mu Mu replacement."""
from .survivor_selector import SurvivorSelectorABC


class MuMuSurvivorSelector(SurvivorSelectorABC):
    """A class for selecting survivors using (u,u) replacement."""


# explicitly specify exports
__all__ = [
    'MuMuSurvivorSelector'
]
