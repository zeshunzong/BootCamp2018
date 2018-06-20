import numpy as np

def convert_to_stochatic_matrix(matrix):
    row_sum =(matrix.sum(axis = 1)).reshape((-1,1))
    result = matrix / row_sum
    return result

A = np.array([[1,2,2],[3,4,5]])
print(convert_to_stochatic_matrix(A))
