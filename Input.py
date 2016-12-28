import Neuron


class Input(Neuron):
    def __init__(self):
        Neuron.__init__(self)

    def forward(self, value=None):
        if value is not None:
            self.value = value
