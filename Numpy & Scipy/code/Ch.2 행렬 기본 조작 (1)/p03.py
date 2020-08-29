import numpy as np
from print_lecture import print_custom as prt

A = np.array( [ [1,2.5,3], [-1,-2,-1.5] ], dtype=np.float64 )

# 벡터 (1D array) 로 변환, A는 변화 없음
B = np.reshape( A, 6 )
prt(B, fmt="%0.2f")
print(B.shape) # shape을 찍어보면 (6,)로 된걸 알 수 있음
print()

# A는 그대로임을 확인
prt(A, fmt="%0.2f")
print(A.shape)
print()

# (3,2) 행렬로 변환
B = np.reshape( A, (3,2) )
prt(B, fmt="%0.2f")
print(B.shape) # shape을 찍어보면 (6,)로 된걸 알 수 있음
print()

# 같은 메모리 공간을 참조하고 있음을 테스트
A[0,2] = 0 # 원래 3에 해당하는 부분
prt(A, fmt="%0.2f")
print()

# 해당 부분의 B도 변함을 알 수 있음
prt(B, fmt="%0.2f")
print()