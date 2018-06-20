import numpy as np

def matrix_def_and_product():
     A = np.triu(np.ones((7,7)))
     #print(A)

     B_lower = np.tril(np.full_like(A, -1))
     B_uppper = np.triu(np.full_like(A, 5)) - np.diag([5,5,5,5,5,5,5])
     B = B_lower + B_uppper
     #print(B)

     return np.dot(np.dot(A,B),A)

print(matrix_def_and_product())
