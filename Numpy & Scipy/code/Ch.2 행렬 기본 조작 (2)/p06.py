import numpy as np
from print_lecture import print_custom as prt

A = np.array([[1,2,1],[2,1,3],[1,3,1]],dtype=np.float64)
r = 5.0

# A * r도 동일
result = r * A

prt(result, fmt="%0.1f")
