import numpy as np

# Generate random arrays
## https://docs.scipy.org/doc/numpy/reference/routines.random.html

# Normal distribution
## 1D array
a = np.random.normal(100, 10, 3)
## 2D array
a = np.random.normal(100, 10, (5, 7))

# Slicing
a[0, 1:3]
a[1:3, 1:3]
a[[0,2,4], 2]

# Mean
a.mean()
