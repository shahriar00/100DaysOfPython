import  numpy as np
from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import connected_components


arr = np.array([[3,0,0],[0,1,1]])
mat = csr_matrix(arr)
mat.eliminate_zeros()
print(mat)

newarr = csr_matrix(arr)
print(connected_components((newarr)))