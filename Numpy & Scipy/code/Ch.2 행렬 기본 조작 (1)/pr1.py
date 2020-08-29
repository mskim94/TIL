import numpy as np
from print_lecture import print_custom as prt

A = np.genfromtxt('pr1_inp1.txt',dtype=np.float64, delimiter=',')

# = 기호
B1 = A

# copy
B2 = np.copy(A)

# 7에 해당하는 부분 0으로
A[1,1] = 0

# B1은 A와 같은 메모리 공간 참조함을 알 수 있음. B2는 아님.
prt(B1,fmt="%0.1f")
print()
prt(B2,fmt="%0.1f")
print()

# reshape (5,3) 으로
A = np.reshape(A, (5,3))
prt(A,fmt="%0.1f")
print()

# 밴드 포함 upper triangular
Bt = np.triu(A, k=0)
prt(Bt,fmt="%0.1f")
print()

# Bt를 1D array화 하여 정사각 행렬 생성
result = np.diagflat(Bt,k=0)
prt(result,fmt="%0.1f")
print()

# trace
val = np.trace(result,offset=0)
print(val)
