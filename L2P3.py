'''3.	Familiarize with the functions to create
a)	an uninitialized array
b)	array with all elements as 1,
c)	 all elements  as 0
'''
print('Dona T John')
print('21/MCA/018')

import numpy as np

print("a)	an uninitialized array\n")
mat1 = np.empty(4, dtype=int)
print("Matrix mat1 : \n", mat1)

mat2 = np.empty([3, 3], dtype=int)
print("Matrix mat2 : \n", mat2)

mat3 = np.empty([2, 2])
print("Matrix mat3 : \n", mat3)

print(" b)	array with all elements as 1\n")
a = np.ones(3, dtype=int)
print("Matrix a : \n", a)

b = np.ones([3, 3], dtype=int)
print("Matrix b : \n", b)

print("c)	 all elements  as 0\n")
a = np.zeros(3, dtype=int)
print("Matrix a : \n", a)

b = np.zeros([3, 3], dtype=int)
print("Matrix b : \n", b)