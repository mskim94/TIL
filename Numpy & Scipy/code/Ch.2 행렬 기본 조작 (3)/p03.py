import numpy as np

b1 = (-1)*np.ones((4,), dtype=np.float64)
b2 = 2*np.ones((5,), dtype=np.float64)
b3 = np.ones((4,), dtype=np.float64)

A = np.diag(b1,k=-1) + np.diag(b2) + np.diag(b3,k=1)

print(A)