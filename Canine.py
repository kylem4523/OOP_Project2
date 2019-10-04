import Animal
from RoamStrategy import CanineRoam


class Canine(Animal.Animal):
    # Intermediate Animal Class that uses the Roam Strategy pattern to select the appropriate
    # roaming behavior for all canines.
    def __init__(self, *args, **kwargs):
        super(Canine, self).__init__(roam_strategy=CanineRoam(), *args, **kwargs)
