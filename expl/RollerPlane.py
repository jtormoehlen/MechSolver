import numpy as np
from matplotlib import pyplot as plt

from expl.Model import Model
from CustomShape import Cylinder
from CustomShape import Plane

######################### Parameters #########################

# cylinder radius [m]
R = 2.0
# gravitational acceleration [m/s^2]
g = 9.81
# plane mass [kg]
m = 1.0
# cylinder mass [kg]
M = 10.0
# constants c1, c2 [1]
c1 = M/(m+M)
c2 = 2/3
# plane height [m]
H = 7.0
# plane angle [radian]
phi = np.pi/180*8
# plane length [m]
L = H/np.tan(phi)

class RollerPlane(Model):

    def equationSystem(t, Y):

        dY = [None]*4
        dY[0] = Y[2]
        dY[1] = Y[3]
        dY[2] = -c1*c2*g*np.sin(phi)*np.cos(phi) / (1 - c1*c2*np.cos(phi)**2)
        dY[3] = c2*g*np.sin(phi) / (R * (1 - c1*c2*np.cos(phi)**2))

        return dY

    # intial conditions
    u0 = -18.0
    theta0 = 0.0
    v0 = 3.0
    omega0 = 0.0
    Y0 = np.array([u0, theta0, v0, omega0])

    # time window [s]
    Model.T = 10.0
    t = [0, Model.T]
    
    # generate solution
    solution = Model.solve(equationSystem, t, Y0)

    Model.staticShapes = [
        plt.Line2D([-20,20],[-0.2,-0.2], color='grey')
    ]

    Model.movingShapes = [
        Plane([0,0,L,0], [0,H,0,0], color='k'),
        Cylinder((0, 0), R, color='black')
    ]
    Model.movingShapes[0].set_HL(H, L)
    Model.movingShapes[1].set_R(R)
    Model.movingShapes[1].set_facecolor('none')

    def coordTrans(self, pos):
        x = pos[0] + R*pos[1]*np.cos(phi)
        y = H - R*pos[1]*np.sin(phi)
        
        for i in range(y.size):
            if y[i] <= 0.0:
                y[i] = 0.0
        return [pos[0],0.0*pos[0],x,y]