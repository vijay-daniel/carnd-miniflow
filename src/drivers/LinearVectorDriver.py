'''
Created on Jan 30, 2017

@author: amzvja
'''
"""
This script builds and runs a graph with miniflow.

"""

from miniflow.Input import Input
from miniflow.LinearVector import LinearVector
from miniflow.Util import topological_sort, forward_pass
import numpy as np


X, W, b = Input(), Input(), Input()

f = LinearVector(X, W, b)

X_ = np.array([[-1., -2.], [-1, -2]])
W_ = np.array([[2., -3], [2., -3]])
b_ = np.array([-3., -5])

feed_dict = {X: X_, W: W_, b: b_}

graph = topological_sort(feed_dict)
output = forward_pass(f, graph)

"""
Output should be:
[[-9., 4.],
[-9., 4.]]
"""
print(output)