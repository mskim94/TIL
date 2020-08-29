import numpy as np
from print_lecture import print_custom as prt


A = np.array( [[1,2,3,4,5], [6,7,8,9,10],
    [11,12,13,14,15], [-1,-2,-3,-4,-5]], 
    dtype=np.float64 )

# 1D array
v1 = A[:,1]
v2 = A[:,2]
v3 = A[:,3]

# vstack을 사용
B = np.vstack( (v1,v2,v3) )
prt(B,fmt="%0.1f")
print()

# matrix-vector product
result = B @ v1
prt(result,fmt="%0.1f")
print(result.shape)