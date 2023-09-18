# CoCoMAS
Competency Conditioned Multi Agent Search

# Requires:
- VMAS
- torch

# Strategy:
- generate N waypoints that fully cover the map
    - randomly select N points in the map
    - generate the Voronoi diagram of the N points
    - find the smallest radius circle that circumscribes each voronoi region
    - update the N points as the radii of the circles
    - iterate until convergence
    - see: 
        - https://www.cs.ccu.edu.tw/~korenson/courses/cs5755/07021413061913497.pdf
        - https://theory.stanford.edu/~megiddo/pdf/lp3.pdf
        - https://docs.scipy.org/doc/scipy/reference/generated/scipy.spatial.Voronoi.html
- policy assigns one waypoint per robot
- robot follows A* path to waypoint