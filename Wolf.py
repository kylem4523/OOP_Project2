import Canine
from MakeNoiseStrategy import WolfNoises


class Wolf(Canine.Canine):
    # Wolf class that uses Noise Strategy to implement correct noise behavior
    def __init__(self, name):
        super(Wolf, self).__init__(noise_strategy=WolfNoises(), name=name)

