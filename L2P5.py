'''5.	Create an 1D array with arange containing first 15 even numbers as  elements
a.	Elements from index 2 to 8 with step 2(also demonstrate the same using slice function)
b.	Last 3 elements of the array using negative index
c.	Alternate elements of the array
d.	Display the last 3 alternate elements
'''
import numpy as np
print('Dona T John')
print('21/MCA/018')
import numpy as np
print('Dona T John')
print('21/MCA/018')

ar = np.arange(2,31,2,dtype=int)
print(ar)

print(" Elements from index 2 to 8 with step 2 : ",ar[1:9:2])
print("last 3 elements :",ar[-3:])
print("Alternate elements :",ar[:30:2])