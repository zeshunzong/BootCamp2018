import numpy as np

def change_negative_to_zero(arr):
    myarr = np.copy(arr)
    negative_positions = myarr < 0
    myarr[negative_positions] = 0
    return myarr


arr = np.array([[-1,1,-1],[-1,1,-1]])
print(change_negative_to_zero(arr))


A = np.arange(12)
B = A.reshape((12, 1))

print(B)
