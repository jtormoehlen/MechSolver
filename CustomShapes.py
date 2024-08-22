import matplotlib.patches as plt
import matplotlib.pyplot as plt
import numpy as np
import warnings

warnings.filterwarnings("ignore")

class Spring:
    r = 0.05
    ns = 20
    nDataPoints = 200
    padRatio = 0.1
    padding = int(np.round(padRatio*nDataPoints))
    ax = None

    pos1 = None
    pos2 = None
    plot = None

    def __init__(self, pos1, pos2, ax, **kwargs):
        self.r = kwargs.get('r', self.r)
        self.ns = kwargs.get('ns', self.ns)
        self.ax = ax
        self.update(pos1, pos2)
    
    def update(self, pos1, pos2):
        pos1 = self.pos1 = np.array(pos1)
        pos2 = self.pos1 = np.array(pos2)
        L = np.linalg.norm(np.array(pos2) - np.array(pos1))
        try:
            k =  2*np.pi * self.ns / (L-2*self.padRatio*L)
        except ZeroDivisionError:
            k = 0

        xSpring = np.linspace(0, L, self.nDataPoints)
        ySpring = np.zeros(self.nDataPoints)
        ySpring[self.padding:-self.padding] = self.r * np.sin(k * xSpring[0:-2*self.padding])

        dx = pos2[0] - pos1[0]
        angle = np.arccos(dx/L)
        if pos1[1] > pos2[1]:
            angle = 2*np.pi - angle

        rotMatrix = np.array([[np.cos(angle), -np.sin(angle)],
                              [np.sin(angle), np.cos(angle)]])
        xSpring, ySpring = -np.matmul(rotMatrix, np.vstack([xSpring, ySpring]))
                
        self.plot = self.ax.plot(xSpring, ySpring, c='k', lw=1.25, zorder=0.1)

    def getArtists(self):
        return self.plot
    

class Cylinder(plt.Circle):

    def __init__(self, *args, **kwargs):
        plt.Circle.__init__(self, *args, **kwargs)
        

    def set_R(self, R):
        self.R = R

    def get_R(self):
        return self.R
    

class Plane(plt.Line2D):

    def __init__(self, *args, **kwargs):
        plt.Line2D.__init__(self, *args, **kwargs)

    def set_HL(self, H, L):
        self.H = H
        self.L = L

    def get_H(self):
        return self.H
    
    def get_L(self):
        return self.L