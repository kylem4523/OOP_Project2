# Abstract super class from which all animals will be composed of
class Animal(object):
    # This constructor uses noise strategy and roam strategy to implement the correct
    # behavior at run-time for all animals
    def __init__(self, noise_strategy, roam_strategy, name, *args, **kwargs):
        self._noise_strategy = noise_strategy
        self._roam_strategy = roam_strategy
        self.name = name

    def sleep(self):
        print("Sleeping")

    def wake_up(self):
        print("Waking Up")

    def eat(self):
        print("Eating")

    def get_name(self):
        return self.name

    # This method will make use of the strategy pattern in order to get the
    # correct run-time behavior for making animal noises.
    def make_noise_strategy(self):
        self._noise_strategy.make_noise()

    # This method will make use of the strategy pattern in order to get the
    # correct run-time behavior for roaming.
    def roam_strategy(self):
        self._roam_strategy.roam()