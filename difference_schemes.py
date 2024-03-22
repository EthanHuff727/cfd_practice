import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 10, 500)
y = np.sin(x)
dydx = np.cos(x)

plt.plot(x, y, label='sin(x)')
plt.plot(x, dydx, label='Exact Derivative')
