import numpy as np
from print_lecture import print_custom as prt


# 아래 두개는 hstack 가능
a = np.array([[1,2,3],[4,5,6]],dtype=np.float64)
b = np.array([[-1,-2],[-3,-4]],dtype=np.float64)
new_mat = np.hstack( (a,b) )
prt(new_mat,fmt="%0.1f")
print(new_mat.shape)
print()

# a와 b를 편의상 덮어씌워서 재활용

# 아래는 vstack만 가능
a = np.array([[1,2,3],[4,5,6]],dtype=np.float64)
b = np.array([[-1,-2,-3],[-4,-5,-6],[-7,-8,-9]],dtype=np.float64)
new_mat = np.vstack( (a,b) )
prt(new_mat,fmt="%0.1f")
print(new_mat.shape)
print()

# 1D array의 hstack / vstack
a = np.array([1,2,3],dtype=np.float64)
b = np.array([4,5,6],dtype=np.float64)
# hstack은 벡터의 길이가 길어짐을 알 수 있음, 즉 사이즈가 달라도 됨
new_mat1 = np.hstack( (a,b) )
prt(new_mat1,fmt="%0.1f")
print(new_mat1.shape)
print()
# vstack은 벡터들을 row 벡터처럼 상상해서 vertical하게 쌓음. 즉, 사이즈가 같아야함
new_mat2 = np.vstack( (a,b) )
prt(new_mat2,fmt="%0.1f")
print(new_mat2.shape)
print()

# 혼합은 vstack만 행렬의 row 사이즈와 벡터의 사이즈가 같아야함을 주의
a = np.array([[1,2,3],[4,5,6]],dtype=np.float64)
b = np.array([7,8,9],dtype=np.float64)
new_mat = np.vstack( (a,b) )
prt(new_mat,fmt="%0.1f")
print(new_mat.shape)
