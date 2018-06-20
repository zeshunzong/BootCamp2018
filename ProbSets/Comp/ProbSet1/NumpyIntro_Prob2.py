import numpy as np

def get_result():
    A = np.array([[3, 1, 4], [1, 5, 9], [-5, 3, 1]])
    result = np.dot(np.dot(A, A), A)*(-1) + 9*np.dot(A, A) - 15*A
    return result
