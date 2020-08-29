import numpy as np
from print_lecture import print_custom as prt

A = np.array( [ [1,2,3],[4,5,6],[7,8,9] ], dtype=np.float64 )

# k=0 생략가능
A1 = np.tril(A, k=0)
prt(A1,fmt="%0.1f")
print()

# k=0 생략가능
A2 = np.triu(A, k=0)
prt(A2,fmt="%0.1f")
print()

A3 = np.tril(A, k=-1)
prt(A3,fmt="%0.1f")
