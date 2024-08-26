import numpy as np
from matplotlib import pyplot as plt

from expl.Model import Model

######################### Parameters #########################

# gravitational acceleration [m/s^2]
g = 9.81
# suspension mass [kg]
m1 = 1.0
# pendulum mass [kg]
m2 = 1.0
# pendulum length [m]
l = 8.0
# total mass
m = m1+m2

class FreePendulum(Model):
    
    def equationSystem(t, Y):
        q1 = Y[0]
        q2 = Y[1]
        q1d = Y[2]
        q2d = Y[3]

        dY = [None]*4
        dY[0] = q1d
        dY[1] = q2d
        dY[2] = (-m2*g*np.sin(q2)*np.cos(q2) + m2*l*q2d**2*np.sin(q2)) / (m -(m2*np.cos(q2)**2))
        dY[3] = ((m2*l*q2d**2*np.sin(q2)) + m*g*np.tan(q2)) / (m2*l*np.cos(q2) - m*l/np.cos(q2))
        return dY

    # intial conditions
    x0 = 8.0
    phi0 = 135*np.pi/180
    v0 = 2.0
    omega0 = 2.0
    Y0 = np.array([x0, phi0, v0, omega0])

    # time window [s]
    Model.T = 2*np.pi
    t = [0, Model.T]
    
    # generate solution
    solution = Model.solve(equationSystem, t, Y0)

    Model.staticShapes = [
        plt.Line2D([-20,20],[0,0], color='grey')
    ]

    Model.connectingShapes = [
        plt.Line2D([0,0],[0,0], color='black')
    ]

    def coordTrans(self, pos):
        x1 = pos[0]
        y1 = 0.0*pos[0]
        x2 = l*np.sin(pos[1]) + x1
        y2 = -l*np.cos(pos[1])
        return [x1, y1, x2, y2]