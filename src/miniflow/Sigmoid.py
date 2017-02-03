'''
Created on Jan 30, 2017

@author: amzvja
'''
from miniflow.Node import Node
import numpy as np

class Sigmoid(Node):

    def __init__(self, node):
        Node.__init__(self, [node])

    def _sigmoid(self, x):
        return 1.0 / (1 + np.exp(-x))

    def forward(self):
        self.value = self._sigmoid(self.inbound_nodes[0].value)
        
    def backward(self):
        
        sig_val = self._sigmoid(self.inbound_nodes[0].value)
        # Initialize the gradients to 0.
        self.gradients = {n: np.zeros_like(n.value) for n in self.inbound_nodes}

        # Cycle through the outputs. The gradient will change depending
        # on each output, so the gradients are summed over all outputs.
        for n in self.outbound_nodes:
            # Get the partial of the cost with respect to this node.
            self.gradients[self.inbound_nodes[0]] += sig_val * (1.0 - sig_val) * n.gradients[self]
