import numpy as np
import matplotlib.pyplot as plt

import Animation
import AnimationShapes
from Spring import Spring
import Solution
import DEAnimation

######################### Create base plot #########################

print("Creating animation")

# define plot: figure environment and coordinate system
fig = plt.figure()
fig.canvas.draw()
ax = plt.axes()

xlim = (-20, 20)
ylim = (-20, 20)
ax.set(xlim=xlim, ylim=ylim)
ax.set_aspect('equal')

######################### Define objects to be drawn #########################
    
# choose a set of colors for masses
colors = iter([plt.cm.Set1(i) for i in range(10)])

# set radius of all circles in proportion to window width
circleRadius = (xlim[1]-xlim[0])/40

# define all masses for animation as circles
masses = [AnimationShapes.MovingShape(plt.Circle((0, 0), circleRadius, color=next(colors)), trajectory) for trajectory in DEAnimation.trajectories]
rod = AnimationShapes.ConnectingShape(plt.Line2D([0,0],[0,0], color='black'), masses[0], masses[1])

# collect all shapes in array to pass to animate()
shapes = [
    *masses,
    rod
]

# classes of used custom shapes (shapes that are not contained in matplotlib)
# customShapes = (rod,)

Animation.animate(fig, ax, shapes, Solution.STEP_SIZE, saveGif=False, fps=20, dpi=100)