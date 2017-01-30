'''
Created on Jan 30, 2017

@author: amzvja
'''
from miniflow.Node import Node

class Linear(Node):

    def __init__(self, inputs, weights, bias):
        Node.__init__(self, [inputs, weights, bias])
        
    def forward(self):
        inputs = self.inbound_nodes[0]
        weights = self.inbound_nodes[1]
        bias = self.inbound_nodes[2]
        
        result = 0
        for x, w in zip(inputs.value, weights.value):
            result += x * w
        self.value = result + bias.value