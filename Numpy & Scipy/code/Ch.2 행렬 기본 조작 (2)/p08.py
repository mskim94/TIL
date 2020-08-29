import numpy as np
from print_lecture import print_custom as prt

A = np.array([[1,2,1],[2,1,3],[1,3,1]],dtype=np.float64)
u = np.array([5,1,3],dtype=np.float64)

result = np.matmul(A , u)
# 동일한 표현
#result = A @ u

prt(result, fmt="%0.1f")
