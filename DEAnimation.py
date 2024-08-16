import numpy as np

import Solution

# select only spatial coordinates
spatialCoordsList = [[(Solution.solution.y)[0],(Solution.solution.y)[1]]]

# transform to caretsian coordinates 
# transpose for easier manipulation of data:
# [[q1(t)], [q2(t)]] --> [[q1(0), q2(0)], [q1[1], q2(1)],...]

for j, spatialCoords in enumerate(spatialCoordsList):
    spatialCoords = np.transpose(spatialCoords)
    for i in range(len(spatialCoords)):
        spatialCoords[i] = Solution.coordTrans(spatialCoords[i])
    spatialCoords = np.transpose(spatialCoords)
    spatialCoordsList[j] = spatialCoords

# group coordinates to trajectories of masses
trajectories = []
for spatialCoords in spatialCoordsList:
    for i in range(int(len(spatialCoords)/2)):
        trajectories.append(np.transpose(spatialCoords[2*i:2*i+2]))