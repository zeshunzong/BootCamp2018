import numpy as np

def max_adjacent_product():
    grid = np.load("grid.npy")

    row_product = grid[:, 0:-3] * grid[:, 1:-2] * grid[:, 2:-1] * grid[:, 3:]
    row_max = np.max(row_product)

    column_product = grid[0:-3,:] * grid[1:-2,:] * grid[2:-1,:] * grid[3:,:]
    column_max = np.max(column_product)

    diag_product = grid[0:-3, 0:-3] * grid[1:-2, 1:-2] * grid[2:-1, 2:-1] * grid[3:, 3:]
    diag_max = np.max(diag_product)

    return np.max([row_max, column_max, diag_max])
