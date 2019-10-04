"""This class will serve as the Strategy template for making noises Code in this module has been taken from
https://medium.com/@sheikhsajid/design-patterns-in-python-part-1-the-strategy-pattern-54b24897233e """
import abc
from random import choice


# This is the abstract Noise Strategy Master Class
class MakeNoiseStrategy(object):
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def make_noise(self):
        """This is a required method that will be overridden in the lowest sub-class"""


# This is a concrete strategy for making cat noises.
class CatNoises(MakeNoiseStrategy):
    def make_noise(self):
        cat_noises = ["Hiss", "Meow", "Purr"]
        print(choice(cat_noises))


# This is a concrete strategy for making tiger noises.
class TigerNoises(MakeNoiseStrategy):
    def make_noise(self):
        tiger_noises = ["Growl", "Huff"]
        print(choice(tiger_noises))


# This is a concrete strategy for making dog noises.
class DogNoises(MakeNoiseStrategy):
    def make_noise(self):
        dog_noises = ["Woof", "Bark"]
        print(choice(dog_noises))


# This is a concrete strategy for making wolf noises.
class WolfNoises(MakeNoiseStrategy):
    def make_noise(self):
        wolf_noises = ["Awoooooooo", "Growl"]
        print(choice(wolf_noises))
