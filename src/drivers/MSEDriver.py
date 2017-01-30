'''
Created on Jan 30, 2017

@author: amzvja
'''
from miniflow.Input import Input
from miniflow.MSE import MSE
from miniflow.Util import topological_sort, forward_pass_on_graph
import numpy as np

"""
This script builds and runs a graph with miniflow.

"""

y, a = Input(), Input()
cost = MSE(y, a)

y_ = np.array([1, 2, 3])
a_ = np.array([4.5, 5, 10])

feed_dict = {y: y_, a: a_}
graph = topological_sort(feed_dict)
# forward pass
forward_pass_on_graph(graph)

"""
Expected output

23.4166666667
"""
print(cost.value)
