import numpy as np
from print_lecture import print_custom as prt

A = np.array( [ [1,2.5,3], [-1,-2,-1.5], [4,5.5,6] ], dtype=np.float64 )

# 같은 메모리 참조
#B = A

# 다른 메모리에 B를 복사하기위해 copy 기능 사용
B = np.copy(A)

# 수정전 A, B
prt(A, fmt="%0.1f")
print()
prt(B, fmt="%0.1f")

# A 수정
A[1,1] = 0
A[2,2] = 0

# 수정후 A, B
print()
prt(A, fmt="%0.1f")
print()
# copy를 사용하지 않으면 B는 A와 동일 메모리 참조, copy사용시 A만 변함을 확인 가능
prt(B, fmt="%0.1f")