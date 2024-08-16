import numpy as np
from scipy import integrate

######################### Parameters #########################

# gravitational acceleration [m/s^2]
g = 9.81

######################### Definition of differential equation #########################

# system of differential equations
# function to be used in differential equation solver
# t: point in time
# Y: array of values of differentiated variables
# takes Y=[q1, q2, q1d, q2d,...], returns derivatives dY=[q1d, q2d, q1dd, q2dd,...]
def equationSystem(t, Y):
    dY = [None]*2

    return dY

Y0 = [0.0, 0.0]

# time window [s]
T = 1.0 
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
    return pos
