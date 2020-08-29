import numpy as np
from print_lecture import print_custom as prt

A = np.array([[1,2,3],[4,5,6],[7,8,9]],dtype=np.float64)

# 같은 메모리 공간, T를 사용할 경우 괄호가 없음을 주의 (property)
B = A.transpose()
#B = A.T

# 이렇게 바꾸면, 같음 메모리 공간을 나타내는 B도 바뀐다고 생각할 수 있음. 원치 않으면 copy 사용
A[0,1] = -100

prt(A, fmt="%0.1f")
print()
prt(B, fmt="%0.1f")