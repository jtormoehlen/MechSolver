import matplotlib.pyplot as plt

import Animation
import AnimationShapes
from CustomShapes import Spring
import Solution

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
masses = [AnimationShapes.MovingShape(plt.Circle((0, 0), circleRadius, color=next(colors)), trajectory) for trajectory in Solution.trajectories]

# rod = AnimationShapes.ConnectingShape(plt.Line2D([0,0],[0,0], color='black'), masses[0], masses[1])
# suspension = AnimationShapes.StaticShape(plt.Line2D([-20,20],[0,0], color='grey'))

suspension = AnimationShapes.StaticShape(plt.Circle((0,0), 0.3*circleRadius, color='k'))
spring = AnimationShapes.ConnectingShape(Spring((0,0), (0,0), ax, r=0.5*circleRadius, ns=10), masses[1], suspension)

# collect all shapes in array to pass to animate()
shapes = [
    *masses,
    spring,
    suspension
]

# classes of used custom shapes (shapes that are not contained in matplotlib)
customShapes = (Spring,)

Animation.animate(fig, ax, shapes, Solution.model.STEP_SIZE, customShapes, 
                  saveGif=True, fileName=Solution.model.name, fps=20, dpi=100)