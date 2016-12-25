import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import scipy.optimize as spo

def error(line, data):
    err = np.sum((data[:, 1] - (line[0]*data[:,0] + line[1])) ** 2)
    return err

def fit_line(data, error_func):
    """
    Fit a line to given data, using a supplied error function

    Returns the line that minimizes the error function
    """
    # Initial guess
    l = np.float32([0, np.mean(data[:, 1])])

    # Call optimizer to minimize error function
    result = spo.minimize(error_func, l, args=(data,), method='SLSQP', options={'disp': True})
    print('Fitline debug:', type(result))
    print('Fitline debug:', result)
    return result.x

def test_run():
    l_orig = np.float32([4,2])
    print('Original line: C0 = {}, C1 = {}'.format(l_orig[0], l_orig[1]))
    X_orig = np.linspace(0, 10, 21)
    Y_orig = l_orig[0] * X_orig + l_orig[1]
    plt.plot(X_orig, Y_orig, 'b--', linewidth=2.0, label='Original line')

    # Generate noisy data points
    noise_sigma = 3.0
    noise = np.random.normal(0, noise_sigma, Y_orig.shape)
    data = np.asarray([X_orig, Y_orig + noise]).T
    plt.plot(data[:,0], data[:,1], 'go', label='Data points')

    # Fit line to data
    l_fit = fit_line(data, error)
    print('Fitted line: C0 = {}, C1 = {}'.format(l_fit[0], l_fit[1]))
    plt.plot(data[:,0], l_fit[0]*data[:,0] + l_fit[1], 'r--', linewidth=2.0, label='Fitted line')

    plt.legend()
    plt.show()

if __name__=='__main__':
    test_run()
