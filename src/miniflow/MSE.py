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
        
        self.value = np.sum(np.square(y - a)) / y.shape[0]
