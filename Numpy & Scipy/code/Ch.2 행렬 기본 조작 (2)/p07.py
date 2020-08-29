import numpy as np
from print_lecture import print_custom as prt

A = np.array([[1,2,3],[3,2,1]],dtype=np.float64)
B = np.array([[2,1],[1,2],[-3,3]],dtype=np.float64)

# matrix multiplication
result = np.matmul(A,B)
# 동일한 표현
#result = A @ B

prt(result, fmt="%0.1f")
