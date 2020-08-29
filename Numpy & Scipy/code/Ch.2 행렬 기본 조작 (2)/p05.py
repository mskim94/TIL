import numpy as np
from print_lecture import print_custom as prt

A = np.array([[1-2j,3+1j,1],[1+2j,2-1j,7]],dtype=np.complex128)

# real과 imag는 같은 메모리 공간의 값을 참조
A_real = A.real
A_imag = A.imag

# conjugate는 새 메모리 공간 반환
A_conj = A.conjugate()

# A의 일부를 변경전
prt(A_real, fmt="%0.1f")
print()
prt(A_imag, fmt="%0.1f")
print()
prt(A_conj, fmt="%0.1f")
print()

A[0,2] = 100+100j

# A의 일부를 변경후
prt(A_real, fmt="%0.1f")
print()
prt(A_imag, fmt="%0.1f")
print()
# conjugate는 A와 다른 메모리 공간에 있음을 확인 가능
prt(A_conj, fmt="%0.1f")