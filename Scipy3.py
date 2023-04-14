import numpy as np
from scipy.sparse.csgraph import connected_components
from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import dijkstra

arr = np.array([
  [0, 1, 2],
  [1, 0, 0],
  [2, 0, 0]
])

newarr = csr_matrix(arr)

print(connected_components(newarr))

diarray = csr_matrix(arr)
print(dijkstra(diarray,return_predecessors=True,indices=0))

from scipy.sparse.csgraph import floyd_warshall

farr = csr_matrix(arr)
print(floyd_warshall(farr,return_predecessors=True))

from scipy.sparse.csgraph  import bellman_ford
barr = csr_matrix(arr)
print(bellman_ford(barr,return_predecessors=True,indices=0))

from scipy.sparse.csgraph  import depth_first_order
darr = csr_matrix(arr)
print(depth_first_order(darr,1))

from scipy.sparse.csgraph import breadth_first_order
barr = csr_matrix(arr)
print(breadth_first_order(barr,1))
