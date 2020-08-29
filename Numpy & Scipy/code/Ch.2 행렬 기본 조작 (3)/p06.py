import numpy as np

A = np.array([[1,2],[3,4]],dtype=np.float64)

b = np.array([2,4],dtype=np.float64)

C = b / A

print(C)