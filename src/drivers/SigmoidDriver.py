'''
Created on Jan 30, 2017

@author: amzvja
'''
"""
This script builds and runs a graph with miniflow.

"""

from miniflow.Input import Input
from miniflow.LinearVector import LinearVector
from miniflow.Sigmoid import Sigmoid
from miniflow.Util import topological_sort, forward_pass
import numpy as np


X, W, b = Input(), Input(), Input()

f = LinearVector(X, W, b)
g = Sigmoid(f)

X_ = np.array([[-1., -2.], [-1, -2]])
W_ = np.array([[2., -3], [2., -3]])
b_ = np.array([-3., -5])

feed_dict = {X: X_, W: W_, b: b_}

graph = topological_sort(feed_dict)
output = forward_pass(g, graph)

"""
Output should be:
[[  1.23394576e-04   9.82013790e-01]
 [  1.23394576e-04   9.82013790e-01]]
"""
print(X_)
print(output)
