# MechSolver
This Solver is designed to find numerical solutions to Mechanics based problems. For that, a system of first order differential equations related to a specific problem is given. The solution is then computed numerically by the SciPy-based Runge-Kutta procedure. The result can the be plotted as a trajectory of mass points or simple geometric objects.

## Example: Free moving pendulum
$$
\begin{align}
v &= \dot{x},\\
\omega &= \dot{\varphi},\\
\dot{v} &= -\frac{-m_2g\sin\varphi\cos\varphi+m_2l\dot{\varphi}^2\sin\varphi}{m-m_2\cos^2\varphi},\\
\dot{\omega} &= \frac{m_2l\dot{\varphi}^2\sin\varphi+mg\tan\varphi}{m_2l\cos\varphi-\frac{ml}{\cos\varphi}}
\end{align}
$$
```
    dY = [None]*4
    dY[0] = q1d
    dY[1] = q2d
    dY[2] = (-m2*g*np.sin(q2)*np.cos(q2) + 
            m2*l*q2d**2*np.sin(q2)) / (m - (m2*np.cos(q2)**2))
    dY[3] = ((m2*l*q2d**2*np.sin(q2)) + 
            m*g*np.tan(q2)) / (m2*l*np.cos(q2) - m*l/np.cos(q2))
    return dY
```