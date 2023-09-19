import numpy as np
import multiprocessing as mp

from cocomas.path_planning import A_StarDist, Node, Grid

def test_a_star(N):
    dists = np.ones((N,N)) * np.inf
    grid = Grid(np.zeros((N,N)))

    tgt = Node()
    tgt.set_pose((0,0))

    for i in range(N):
        for j in range(N):
            src = Node()
            src.set_pose((i,j))
            dists[i,j] = A_StarDist(grid, src, tgt, dists)
    return dists

if __name__ == "__main__":
    
    with mp.Pool() as pool:
        for result in pool.map(test_a_star, range(1,101)):
            print(result)
            print()