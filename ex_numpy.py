import numpy as np

#
## https://docs.scipy.org/doc/numpy/reference/routines.random.html

# Generate random arrays
## 1D array - normal distribution
a = np.random.normal(100, 10, 3) # mean, variance, shape
## 2D array - uniform distrution
a = np.random.uniform(0, 10, (5, 7)) # min, max, shape
## 1D array - uniform distrubtion - other method
b = np.random.rand(10)

# Slicing
a[0, 1:3]
a[1:3, 1:3]
a[[0,2,4], 2]
a[0:5:2, :]
a[:, 6] = range(-10, -5)

# Predicate indexing
mean_b = b.mean()
bool_idx = b<mean_b
b[bool_idx]
# same as
b[b<b.mean()]


# Assignment
a[0, 0] = 1
a[1:3, 1:3] = 2
a[-1, :] = 3

# Mean + 33 other
a.mean()
a.median()
a.std()

# Rolling statistics
