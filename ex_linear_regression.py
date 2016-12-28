import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import sys
from sklearn import datasets,linear_model

def test_run():
    # Load the diabetes dataset
    #diabetes = datasets.load_diabetes()
    #diabetes_X = diabetes.data[:, np.newaxis, 2]
    #print(diabetes_X[:10])
    #sys.exit(1)

    m,b = 4,2
    X_orig = np.linspace(0, 10, 21)
    Y_orig = m * X_orig + b

    # Generate noisy data points
    noise_sigma = 3.0
    noise = np.random.normal(0, noise_sigma, Y_orig.shape)

    # Set features and labels
    features = np.asarray([[x] for x in X_orig])
    labels = Y_orig + noise

    print(features)
    print(labels)

    # Fit line to data
    reg = linear_model.LinearRegression()
    reg.fit(features, labels)
    predictions = reg.coef_[0]*X_orig + reg.intercept_

    # Plot
    plt.plot(X_orig, Y_orig, 'b--', linewidth=2.0, label='Original line')
    plt.plot(X_orig, labels, 'go', label='Data points')
    plt.plot(X_orig, predictions, 'r--', linewidth=2.0, label='Predictions')
    plt.legend()
    plt.show()



if __name__=='__main__':
    test_run()
