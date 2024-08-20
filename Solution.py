import numpy as np
from scipy import integrate

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

######################### Definition of differential equation #########################

# system of differential equations
# function to be used in differential equation solver
# t: point in time
# Y: array of values of differentiated variables
# takes Y=[q1, q2, q1d, q2d,...], returns derivatives dY=[q1d, q2d, q1dd, q2dd,...]
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
T = 2*np.pi
t = [0, T] 

######################### Solving differential equation ######################### #!

print("Solving differential equation")

# might has to be lowered until there is a stable solution 
STEP_SIZE = 0.005

# differential equation solver scipy.integrate.solve_ivp needs:
#   a function that calculates the derivative at given point in time (here: equationSystem)
#   a time window (here: t)
#   an array of inital conditions (here: Y0)
# outputs soloution objects with information about solution
# solution.y returns matrix of solutions for all coordinates (array containing arrays of data points):
# solution.y = [q1(t), q1'(t), q2(t), q2'(t), ...]
# documentation: https://docs.scipy.org/doc/scipy/reference/generated/scipy.integrate.solve_ivp.html 
solution = integrate.solve_ivp(equationSystem, t, Y0, max_step = STEP_SIZE)

# transformation to cartesian coordinates
# in this example: pos = [q1,q2]
def coordTrans(pos):
    x1 = pos[0]
    y1 = 0.0*pos[0]
    x2 = l*np.sin(pos[1]) + x1
    y2 = -l*np.cos(pos[1])
    return [x1, y1, x2, y2]