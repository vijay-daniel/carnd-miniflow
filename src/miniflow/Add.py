'''
Created on Jan 30, 2017

@author: amzvja
'''
from miniflow.Node import Node

class Add(Node):

    def __init__(self, x, y):
        Node.__init__(self, [x, y])
        
    def forward(self):
        result = 0
        for n in self.inbound_nodes:
            result = result + n.value
        self.value = result
            