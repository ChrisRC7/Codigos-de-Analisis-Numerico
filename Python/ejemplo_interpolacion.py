import numpy as np
from scipy.linalg import solve
import matplotlib.pyplot as plt

x = np.array([0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8])
y = np.log(np.arcsin(x)) / np.log(x)
n = len(x) - 1

A = np.array([x**k for k in range(n, -1, -1)]).T
a = solve(A, y)

xv = np.arange(0.2, 0.81, 0.01)
fv = np.log(np.arcsin(xv)) / np.log(xv)
yv = np.polyval(a, xv)



print(y)
plt.plot(xv, yv, 'r')
plt.plot(xv, fv, 'b')
plt.show()
