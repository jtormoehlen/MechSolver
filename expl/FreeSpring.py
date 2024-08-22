import numpy as np

from expl.Model import Model

######################### Parameters #########################

# length [m]
l = 1.0
# gravitational acceleration [m/s^2]
g = 9.81
# mass [kg]
m = 3.0
# spring constant [N/m]
k = g/2

class FreeSpring(Model):

    def equationSystem(t, Y):

        dY = [None]*4
        dY[0] = Y[2]
        dY[1] = Y[3]
        dY[2] = Y[0] * Y[3]**2 + g * np.cos(Y[1]) - k/m * (Y[0] - l)
        dY[3] = -2 * Y[3] * Y[2] / Y[0] - g * np.sin(Y[1]) / Y[0]

        return dY

    # intial conditions
    x0 = -1.0
    phi0 = 90*np.pi/180
    v0 = 3.0
    omega0 = 0.1
    Y0 = np.array([x0, phi0, v0, omega0])

    # time window [s]
    Model.T = 4*np.pi
    t = [0, Model.T]
    
    # generate solution
    solution = Model.solve(equationSystem, t, Y0)

    def coordTrans(self, pos):
        x1 = pos[0]*0
        y1 = pos[0]*0
        x2 = pos[0]*np.cos(pos[1]-np.pi/2)
        y2 = pos[0]*np.sin(pos[1]-np.pi/2)
        return [x1, y1, x2, y2]