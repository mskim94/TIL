import numpy as np
from print_lecture import print_custom as prt

A = np.array([[1,2],[3,4]], dtype=np.float64)

x = np.array([5,6],dtype=np.float64)

# reshape 방법
'''
x = np.reshape(x, (2,1) )
# 결과는 (1,1) 행렬로 반환됨
result = x.T @ A @ x
print(result)
'''

# vdot
result = np.vdot(x, A@x)
# 결과는 scalar 값으로 반환됨
print(result)
