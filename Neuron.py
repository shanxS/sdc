class Neuron:
    def __init__(self, inbound_neurons=[]):
        # inbound nodes
        self.inbound_neurons = inbound_neurons
        # outbound
        self.outboudn_neurons = []

        # for each inbound node add this node as outbound
        for n in self.inbound_nodes:
            n.outboudn_neurons.append(self)

        self.value = None

    def forward(self):
        raise NotImplemented

    def backward(self):
        raise NotImplemented
