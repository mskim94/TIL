import numpy as np

A = np.array([[1,2],[3,4]],dtype=np.float64)

B = np.array([[5,6],[7,8]],dtype=np.float64)

# matrix multiplication과 관계 없음
C = B*A
print(C)
print()

# 역행렬과 관계없음
C = B/A
print(C)