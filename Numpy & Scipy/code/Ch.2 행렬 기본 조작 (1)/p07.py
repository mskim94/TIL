import numpy as np
from print_lecture import print_custom as prt

M = np.array( [[1,3],[2,4]], dtype=np.float64 )

# k=0 생략 가능
A = np.diagflat( M, k=0 )

prt(A, fmt="%0.1f")