import numpy as np

def combine_matrix():
    A = np.arange(6)
    A = A.reshape((3,2))
    A = A.T

    B = np.full((3,3), 3)
    B = np.tril(B)

    C = np.diag([-2, -2, -2])


    left_column = np.vstack((np.zeros((3,3)), A, B))
    mid_column = np.vstack((A.T, np.zeros((left_column.shape[0]-3, 2))))
    right_column = np.vstack((np.eye(3), np.zeros((2,3)), C))

    result = np.hstack((left_column, mid_column, right_column))

    return result
print(combine_matrix())
