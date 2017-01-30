'''
Created on Jan 30, 2017

@author: amzvja
'''
from miniflow.Node import Node

class Mul(Node):

    def __init__(self, *args):
        Node.__init__(self, args)
        
    def forward(self):
        result = 1
        for n in self.inbound_nodes:
            result = result * n.value
        self.value = result
            