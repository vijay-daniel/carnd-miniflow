'''
Created on Jan 30, 2017

@author: amzvja
'''
from miniflow.Node import Node
import numpy as np

class LinearVector(Node):

    def __init__(self, X, W, b):
        Node.__init__(self, [X, W, b])
        
    def forward(self):
        X = self.inbound_nodes[0]
        W = self.inbound_nodes[1]
        b = self.inbound_nodes[2]
        
        self.value = np.dot(X.value, W.value) + b.value
        
        
    def backward(self):
        """
        Calculates the gradient based on the output values.
        """
        # Initialize a partial for each of the inbound_nodes.
        self.gradients = {n: np.zeros_like(n.value) for n in self.inbound_nodes}
        # Cycle through the outputs. The gradient will change depending
        # on each output, so the gradients are summed over all outputs.
        for n in self.outbound_nodes:
            # Get the partial of the cost with respect to this node.
            grad_cost = n.gradients[self]
            # Set the partial of the loss with respect to this node's inputs.
            self.gradients[self.inbound_nodes[0]] += np.dot(grad_cost, self.inbound_nodes[1].value.T)
            # Set the partial of the loss with respect to this node's weights.
            self.gradients[self.inbound_nodes[1]] += np.dot(self.inbound_nodes[0].value.T, grad_cost)
            # Set the partial of the loss with respect to this node's bias.
            self.gradients[self.inbound_nodes[2]] += np.sum(grad_cost, axis=0, keepdims=False)
            print("Grad cost: ", grad_cost, ", Shape: ", grad_cost.shape)
            print("W: ", self.inbound_nodes[1].value, ", Shape: ", self.inbound_nodes[1].value.shape)
            print("X: ", self.inbound_nodes[0].value, ", Shape: ", self.inbound_nodes[0].value.shape)
        

        print("Linear: ", self.gradients)
