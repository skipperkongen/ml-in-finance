import numpy as np
import matplotlib.pyplot as plt

X = np.linspace(-16,16,21)
C = np.array([1.5, -10, -5, 60, 50])
Y = np.polyval(C, X)
plt.plot(X, Y, '-')
plt.show()
