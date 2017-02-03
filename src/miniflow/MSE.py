'''
Created on Jan 30, 2017

@author: amzvja
'''
from miniflow.Node import Node
import numpy as np

class MSE(Node):

    def __init__(self, y, a):
        Node.__init__(self, [y, a])
        
    def forward(self):
        y = self.inbound_nodes[0].value.reshape(-1, 1)
        a = self.inbound_nodes[1].value.reshape(-1, 1)
        
        self.m = y.shape[0]
        self.diff = y - a
        self.value = np.mean(self.diff ** 2)

    def backward(self):
        self.gradients[self.inbound_nodes[0]] = (2.0 / self.m) * self.diff
        self.gradients[self.inbound_nodes[1]] = (-2.0 / self.m) * self.diff
        
        print("MSE: ", self.gradients)