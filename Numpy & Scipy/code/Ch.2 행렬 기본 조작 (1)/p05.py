import numpy as np
from print_lecture import print_custom as prt

A = np.array( [ [1,2,3],[4,5,6],[7,8,9] ], dtype=np.float64 )

# 같은 메모리 공간 참조
b = np.diag(A, k=1)

print(b)
print()

# 한번 A를 바꿔봐서 살펴보기
A[0,1] = 0 # b[0]에 해당하는 부분

# 바뀐걸 알수있음
print(b)

# b는 현재 수정 불가 (read-only, Numpy 1.9)
#b[0] = 1