'''
Created on Jan 30, 2017

@author: amzvja
'''

class Node(object):

    def __init__(self, inbound_nodes=[]):
        self.inbound_nodes = inbound_nodes
        self.outbound_nodes = [] 
        self.value = None
        self.gradients = {}
        
        for n in self.inbound_nodes:
            n.outbound_nodes.append(self)
        
    def forward(self):
        raise NotImplementedError
    
    def backward(self):
        raise NotImplementedError
