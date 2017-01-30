'''
Created on Jan 30, 2017

@author: amzvja
'''
from miniflow.Add import Add
from miniflow.Input import Input
from miniflow.Linear import Linear
from miniflow.Util import topological_sort, forward_pass

"""
This script builds and runs a graph with miniflow.

"""

inputs, weights, bias = Input(), Input(), Input()

f = Linear(inputs, weights, bias)

feed_dict = {
    inputs: [6, 14, 3],
    weights: [0.5, 0.25, 1.4],
    bias: 2
}

graph = topological_sort(feed_dict)
output = forward_pass(f, graph)

print(output)