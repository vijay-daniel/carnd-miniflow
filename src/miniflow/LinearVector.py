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
