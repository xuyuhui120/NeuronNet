import numpy as np

class NeuronLyr(object):
    """The Layer model of Neuron Net

    """
    def __init__(self, num, val = []):
        super(Neuron, self).__init__()
        # The count of Neurons
        self.num = num
        # The value of the neurons
        self.val = val

class InputLyr(NeuronLyr):
    """Input Layer Model

    """
    def __init__(self, num, val):
        super().__init__(num, val)


class OutputLyr(NeuronLyr):
    """Output Layer Model

    """
    def __init__(self, num, val, weight):
        super().__init__(num, val)
        self.weight = weight

class OutputLyr(NeuronLyr):
    """Hidden Layer Model

    """
    def __init__(self, num, val, weight):
        super().__init__(num, val)
        self.weight = weight

