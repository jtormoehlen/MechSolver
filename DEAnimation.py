import numpy as np

import Solution

# select only spatial coordinates
spatialCoordsList = [sol for sol in Solution.solution.y]

# transform to cartesian coordinates 
# transpose for easier manipulation of data:
# [[q1(t)], [q2(t)]] --> [[q1(0), q2(0)], [q1[1], q2(1)],...]
spatialCoords = Solution.coordTrans([spatialCoordsList[0], spatialCoordsList[1]])  

# group coordinates to trajectories of masses
trajectories = []
for j in range(int(len(spatialCoords)/2)):
    trajectories.append(np.transpose([-spatialCoords[2*j], spatialCoords[2*j+1]]))