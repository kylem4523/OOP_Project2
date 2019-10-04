import Canine
from MakeNoiseStrategy import DogNoises


class Dog(Canine.Canine):
    # Dog class that uses Make Noise Strategy to implement correct noise behavior
    def __init__(self, name):
        super(Dog, self).__init__(noise_strategy=DogNoises(), name=name)
