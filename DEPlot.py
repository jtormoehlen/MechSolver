import numpy as np
import matplotlib.pyplot as plt

import Solution

############################### Create Plot ######################################

# select only (spatial) coordinates
spatialCoords = [Solution.solution.y[0],Solution.solution.y[1]]

# create multiple plots
ncols = min(3, len(spatialCoords))
nrows = 1 + int((len(spatialCoords)-1) / 3)
figure, axes = plt.subplots(ncols=ncols, nrows=nrows)

# select colors for plot lines
colors = iter([plt.cm.tab10(i) for i in range(10)])

# plot spatial coordinates
plotNo = 0
for q in spatialCoords:
    # create timestamp for every data point  
    time = np.linspace(0, Solution.T, len(q))
    
    # i,j: "coordinates" for position of plot in window
    i = plotNo % 3
    j = int(plotNo/3)
    if nrows == 1:
        axes[i].plot(time, q, color=next(colors))
        axes[i].set_ylabel("Y[" + str(plotNo) + "]")
        axes[i].set_xlabel("t")
    else:
        axes[i, j].plot(time, q, color=next(colors))
        axes[i, j].set_ylabel("Y[" + str(plotNo) + "]")
        axes[i, j].set_xlabel("t")
    plotNo += 1

figure.savefig('./img/plot.png')
plt.show()