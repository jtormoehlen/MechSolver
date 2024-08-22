import numpy as np

from expl.Model import Model

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
H = 5.0
# plane angle [radian]
phi = np.pi/180*22.5
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
    u0 = 0.0
    theta0 = 0.0
    v0 = 5.0
    omega0 = 0.0
    Y0 = np.array([u0, theta0, v0, omega0])

    # time window [s]
    Model.T = 5.0
    t = [0, Model.T]
    
    # generate solution
    solution = Model.solve(equationSystem, t, Y0)

    def coordTrans(self, pos):
        x1 = pos[0]*0
        y1 = pos[0]*0
        x2 = pos[0] + R*pos[1]*np.cos(phi)
        y2 = H - R*pos[1]*np.sin(phi)
        # if y2 <= 0.0:
        #     y2 = 0.0
        return [x1, y1, x2, y2]