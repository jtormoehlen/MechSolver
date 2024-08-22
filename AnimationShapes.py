import sys
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
import matplotlib.patches as patches

from CustomShapes import Spring

class MovingShape:

    def __init__(self, shape, trajectory, showTrajectory=True):
        self.shape = shape
        self.trajectory = trajectory
        self.showTrajectory = showTrajectory
        self.transTraj = np.transpose(trajectory)
    
    def updateShape(self,frame):
        
        if type(self.shape) == type(plt.Circle(0,0)):
            self.shape.center = self.getPos(frame)
        elif type(self.shape) == type(plt.Line2D([], [])):
            self.shape.set_data([self.getPos(frame)[0],
                                 self.getPos(frame)[0],
                                 20+self.getPos(frame)[0],
                                 self.getPos(frame)[0]], 
                                 [0,5,0,0])
        else:
            print("""Shape not yet supported. Add to update- and getPos-method
                                                    in class MovingShape""")
            sys.exit(-1)

    def getPos(self,frame):
        return self.trajectory[frame]


class ConnectingShape:

    def __init__(self, shape, otherShape1, otherShape2):
        self.shape = shape
        self.otherShape1 = otherShape1
        self.otherShape2 = otherShape2
    
    def updateShape(self,frame):
        pos1 = self.otherShape1.getPos(frame)
        pos2 = self.otherShape2.getPos(frame)
        
        if type(self.shape) == type(plt.Line2D([0,0],[0,0])) or type(self.shape) == type(plt.plot(0,0)):
            xdata = [pos1[0],pos2[0]]
            ydata = [pos1[1],pos2[1]]
            self.shape.set_data(xdata,ydata)
        elif type(self.shape) == type(patches.ConnectionPatch((0,0),(0,0),'data')):
            self.shape = patches.ConnectionPatch(pos1,pos2,"data",
                                axesA = self.shape.axesA,
                                axesB = self.shape.axesB)
        elif isinstance(self.shape, Spring):
            self.shape.update(pos1,pos2)
        else:
            print("Shape not yet supported. Add to update-method in class ConnectingShape")
            sys.exit(-1)



class StaticShape:

    def __init__(self,shape):
        self.shape = shape
    
    def updateShape(self,frame):
        pass

    def getPos(self,frame):
        if type(self.shape) == type(plt.Circle(0,0)):
            return self.shape.center
        elif type(self.shape) == type(plt.Line2D([0,0],[0,0])):
            print("Cannot get single position from Line2D")
            sys.exit(-1)
        else:
            print("""Shape not yet supported. Add to getPos-method in class StaticShape""")
            sys.exit(-1)
