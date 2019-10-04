import Feline
from MakeNoiseStrategy import TigerNoises


class Tiger(Feline.Feline):
    def __init__(self, name):
        super(Tiger, self).__init__(noise_strategy=TigerNoises(), name=name)