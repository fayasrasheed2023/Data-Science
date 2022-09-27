'''4.	Create an one dimensional array using arange function containing 10 elements.
Display
a.	First 4 elements
b.	Last 6 elements
c.	Elements from index 2 to 7
'''
import numpy as np
print('Dona T John')
print('21/MCA/018')

arr=np.arange(start=1,stop=11,step=1)
print(arr)
print("First 4 elements are:\n",arr[:4])
print("last six elements are:\n",arr[-6:])
print("Elements from index 2 to 7 are:\n",arr[2:7])