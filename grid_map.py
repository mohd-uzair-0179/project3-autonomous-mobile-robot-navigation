import numpy as np

def create_grid():

    grid=np.zeros((20,20),dtype=int)

    grid[5:15,10]=1

    grid[10,3:10]=1

    return grid
