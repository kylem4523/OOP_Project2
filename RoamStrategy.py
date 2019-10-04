"""This class will serve as the Strategy template for the roam behavior. Code in this module has been taken from
https://medium.com/@sheikhsajid/design-patterns-in-python-part-1-the-strategy-pattern-54b24897233e """
import abc


class RoamStrategy(object):
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def roam(self):
        """This is a required method"""


# This is a concrete strategy for feline-type roaming.
class FelineRoam(RoamStrategy):
    def roam(self):
        print("Slinky feline-like roaming")


# This is a concrete strategy for canine-like roaming.
class CanineRoam(RoamStrategy):
    def roam(selfs):
        print("Happy canine-like bounding")
