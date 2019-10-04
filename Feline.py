import Animal
from RoamStrategy import FelineRoam


class Feline(Animal.Animal):
    # Intermediate Animal Class that uses the Roam Strategy pattern to select the appropriate
    # roaming behavior for all felines.
    def __init__(self, *args, **kwargs):
        super(Feline, self).__init__(roam_strategy=FelineRoam(), *args, **kwargs)
