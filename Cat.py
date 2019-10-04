import Feline
from MakeNoiseStrategy import CatNoises


class Cat(Feline.Feline):
    def __init__(self, name):
        super(Cat, self).__init__(noise_strategy=CatNoises(), name=name)
