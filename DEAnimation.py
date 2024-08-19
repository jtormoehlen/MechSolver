import numpy as np

import Solution

# q1, q2, q3, q4 = Solution.solution.y[0], Solution.solution.y[1], Solution.solution.y[2], Solution.solution.y[3]
# print(q1)
# print(q2)
# print(q3)
# print(q4)

# select only spatial coordinates
spatialCoordsList = [sol for sol in Solution.solution.y]

# transform to cartesian coordinates 
# transpose for easier manipulation of data:
# [[q1(t)], [q2(t)]] --> [[q1(0), q2(0)], [q1[1], q2(1)],...]

# for j, spatialCoords in enumerate(spatialCoordsList):
#     spatialCoords = np.transpose(spatialCoords)
#     for i in range(len(spatialCoords)):
#         spatialCoords[i] = Solution.coordTrans(spatialCoords[i])
#     spatialCoords = np.transpose(spatialCoords)
#     spatialCoordsList[j] = spatialCoords

# group coordinates to trajectories of masses
# trajectories = []
# for spatialCoords in spatialCoordsList:
#     for i in range(int(len(spatialCoords)/2)):
#         trajectories.append(np.transpose(spatialCoords[2*i:2*i+2]))
        
x1, y1, x2, y2 = Solution.coordTrans([spatialCoordsList[0], spatialCoordsList[1]])

trajectories = [np.transpose([-x1, y1]), np.transpose([-x2, y2])]
print(trajectories)