import sys
sys.path.append("..")
import layer
import numpy as np

class BPNeuronNet:
    """
    """
    def __init__( size):
        try:
            if size.shape != 1 && size.shape[0] < 2:
                raise NeuronNerStructException

            self.size = size
            # Define the Input Layer and the Output Layer
            self.input = InputLyr( self.size[0])
            self.OutputLyr = OutputLyr( self.size[-1])


        except NeuronNerStructException:
            print "The Neuron Net you input is illegal"
