import numpy as np

from expl.FreeSpring import FreeSpring
from expl.FreePendulum import FreePendulum
from expl.RollerPlane import RollerPlane, R, L, H

model = RollerPlane("RolleBeweglicheSchiefeEbene")
# model = FreePendulum("FreiBeweglichesPendel")
# model = FreeSpring("FreiSchwingendeFeder")
T = model.T
solution = model.solution
R, L, H = R, L, H

# select only spatial coordinates
spatialCoordsList = [sol for sol in solution.y]

# transform to cartesian coordinates 
# transpose for easier manipulation of data:
# [[q1(t)], [q2(t)]] --> [[q1(0), q2(0)], [q1[1], q2(1)],...]
spatialCoords = model.coordTrans([spatialCoordsList[0], spatialCoordsList[1]])  

# group coordinates to trajectories of masses
trajectories = []
for j in range(int(len(spatialCoords)/2)):
    trajectories.append(np.transpose([spatialCoords[2*j], spatialCoords[2*j+1]]))