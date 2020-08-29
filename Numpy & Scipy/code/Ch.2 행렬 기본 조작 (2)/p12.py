import numpy as np
from print_lecture import print_custom as prt


A = np.array( [[1,2,3,4,5], [6,7,8,9,10],
    [11,12,13,14,15], [-1,-2,-3,-4,-5]], 
    dtype=np.float64 )

sub_A = A[1:3,1:4]
prt(sub_A, fmt="%0.2f")
print()

# 편이를 위해 sub_A를 계속 덮어씌워서 사용

sub_A = A[0:5,2:6]
# 아래는 위와 동일한 표현
#sub_A = A[:,2:]
prt(sub_A, fmt="%0.2f")
print()

# 2D array, shape=(1,3)
sub_A = A[1:2,1:4]
prt(sub_A, fmt="%0.2f")
print(sub_A.shape)
print()

# 이렇게 땡땡 기호가 한쪽이 없으면 무조건 1D array
sub_A = A[1,1:4]
prt(sub_A, fmt="%0.2f")
print(sub_A.shape)
print()

# 2D array, shape=(3,1)
sub_A = A[1:,1:2]
prt(sub_A, fmt="%0.2f")
print(sub_A.shape)
print()

# 이렇게 땡땡 기호가 한쪽이 없으면 무조건 1D array
sub_A = A[1:,1]
prt(sub_A, fmt="%0.2f")
print(sub_A.shape)
print()