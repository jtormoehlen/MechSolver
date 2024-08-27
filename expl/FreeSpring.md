# Example: Free moving spring
## Find langrangian function
$$
\mathcal{L} = \frac{1}{2}m \left( \dot{r}^2 + r^2 \dot{\varphi}^2 \right) + mgr \cos{\varphi} - \frac{D}{2} \left( r - L_0 \right)^2
$$
## Defining differential equation system
$$
\begin{align}
\dot{r} &= v,\\
\dot{\varphi} &= \omega,\\
\dot{v} &= r \omega^2 + \cos{\varphi} - \frac{k}{m} \left( r - L_0 \right),\\
\dot{\omega} &= - \frac{2v\omega}{r} + \frac{g}{r} \sin{\varphi}
\end{align}
$$
```
def equationSystem(t, Y):
    dY = [None]*4
    dY[0] = Y[2]
    dY[1] = Y[3]
    dY[2] = Y[0] * Y[3]**2 + g * np.cos(Y[1]) - k/m * (Y[0] - l)
    dY[3] = -2 * Y[3] * Y[2] / Y[0] - g * np.sin(Y[1]) / Y[0]
    return dY
```
## Defining transformation to cartesian coordinates
$$
\begin{equation}
x = L_0\sin{\varphi}, \quad y = -L_0\cos{\varphi}
\end{equation}
$$
```
def coordTrans(self, pos):
    x1 = pos[0]*0
    y1 = pos[0]*0
    x2 = pos[0]*np.cos(pos[1]-np.pi/2)
    y2 = pos[0]*np.sin(pos[1]-np.pi/2)
    return [x1, y1, x2, y2]
```
## Simple plot result
![](../img/FreiSchwingendefederPlot.png)
## Advanced animation result
![](../img/FreiSchwingendefederAnim.gif)