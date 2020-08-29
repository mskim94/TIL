import numpy as np

A = np.array( [ [1,2,3],[4,5,6],[7,8,9] ], dtype=np.float64 )

# 강좌에서 배운 순서대로 1D화, A[0,0], A[0,1], A[0,2], A[1,0], ..., A[2,2]
# 다른 메모리 공간에 저장
b1 = A.flatten()

print(b1)

# 비슷한 기능 ravel 하지만 같은 메모리 공간 참조, flatten과 같은 형태로 하려면 np.copy() 사용
b2 = np.ravel(A)
print(b2)

# A[2,1]을 0으로 바꿔서 b1과 b2 확인
A[2,1] = 0

# b1은 그대로
print(b1)

# b2[7]이 0으로 바뀐것을 확인 가능
print(b2)