import numpy as np
from print_lecture import print_custom as prt

b = np.array( [1,2,3,4], dtype=np.float64 )

# 정사각 행렬을 만드는 기능이 포함, A와 b는 다른 메모리 공간에 존재
A = np.diag(b, k=-1)

prt(A, fmt="%0.1f")