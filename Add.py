import Neuron


class Add(Neuron):
    def __init__(self, [x, y]):
        Neuron.__init__(self, [x, y])

    def forward(self):
        raise NotImplemented
