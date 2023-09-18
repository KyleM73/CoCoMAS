# CoCoMAS
Competency Conditioned Multi Agent Search

# Requires:
- VMAS
- torch

# Strategy:
- robot has two modes: explore and inspect
- initialize K robots in explore mode
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
- get waypoints adjacent to robot's current region
- policy assigns one waypoint from filtered list per robot
    - input:
        - coverage competency feature vector
        - whole map occupamcy grid
        - pose
        - labeled adjacent waypoints
    - output:
        - waypoint index
- robot follows A* path to waypoint until next point is assigned
- if point-of-interest is detected (ENML or LIVES), mode switch and inspect with camera
    - if target, dome
    - else, mode switch to explore and resume search

# Problem Types:
The search problem may take on the following forms: 
- Single Agent, Static Target -> This is the traveling salesman problem
- Multi Agent, Static Target -> see CONCERTS for optimal formulation
- Multi Agent, Dynamic Target (random)
- Multi Agent, Dynamic Target (adversarial)
This work will explore the dynamic target setting for heterogenious multi agent teams.
In the random case, the target performs a random walk over the graph of map-cover centroids. In the adversarial case, the target selects the node that has the largest minimum distance to one of the robots.

# Theory:
## Static Case:
The probability of finding the target in a cell is: 
- 1/(# of unseen cells) if unseen
- 0 if seen

## Dynamic Case: 
The probability of finding the target in cell(i) given the lilihood p(i) of the most recent scan is:
- P(p=p(i) | cell(i)=target) * P(cell(i) = target) / P(p=p(i)) -> see CONCERTS