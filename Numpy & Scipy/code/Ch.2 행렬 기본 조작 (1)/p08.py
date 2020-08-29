import numpy as np
from print_lecture import print_custom as prt

A = np.array( [ [1,2,3],[4,5,6],[7,8,9] ], dtype=np.float64 )

# k가 아니라 offset임을 주의 offset=0은 생략 가능
val = np.trace(A, offset=0)
print(val)

# val에 덮어씌워서 offset=-1의 trace값 저장하기
val = np.trace(A, offset=-1)
print(val)