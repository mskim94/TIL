import numpy as np

A = np.array([[1,2,3,4,5],[6,7,8,9,10],
    [11,12,13,14,15],[-1,-2,-3,-4,-5]],dtype=np.float64)

# 파이썬의 기본 1D array (list)
idx = [1,2,0,3]
result = A[idx,:]
print(result)
print()

# 편의를 위해서 result에 계속 덮어 씌워서 테스트

idx = [2,1]
result = A[idx,:]
print(result)
print()

idx = [4,1,2]
result = A[:,idx]
print(result)
print()

idx_r = [2,3,0]
idx_c = [2,1,3]
result = A[:,idx_c][idx_r,:]
print(result)