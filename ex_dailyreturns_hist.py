import pandas as pd
import matplotlib.pyplot as plt

from util import *

df = get_data([], '2009-01-10', '2012-12-31')
dr = get_daily_returns(df)

# Get mean, standard deviation and kurtosis
mean = dr['SPY'].mean()
std = dr['SPY'].std()
kurtosis = dr['SPY'].kurtosis()
print('Kurtosis =', kurtosis)

# Plot histogram
dr.hist(bins=20)
plt.axvline(mean, color='w', linewidth=2, linestyle='dashed')
plt.axvline(mean+std, color='r', linewidth=2, linestyle='dashed')
plt.axvline(mean-std, color='r', linewidth=2, linestyle='dashed')

plt.show()
