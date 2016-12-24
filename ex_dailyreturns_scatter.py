import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from util import *

df = get_data(['SPY', 'XOM', 'GLD'], '2009-01-10', '2012-12-31')
dr = get_daily_returns(df)

# Compute stats
beta_XOM, alpha_XOM = np.polyfit(dr['SPY'], dr['XOM'], 1)
beta_GLD, alpha_GLD = np.polyfit(dr['SPY'], dr['GLD'], 1)
correlation = dr.corr(method='pearson')

# Print stats
print('beta XOM =', beta_XOM)
print('alpha XOM =', alpha_XOM)
print('beta GLD =', beta_GLD)
print('alpha GLD =', alpha_GLD)
print('Correlation:')
print(correlation)

# Scatter plot data
dr.plot(kind='scatter', x='SPY', y='XOM')
plt.plot(dr['SPY'], beta_XOM*dr['SPY'] + alpha_XOM, '-', color='r')
plt.show()

dr.plot(kind='scatter', x='SPY', y='GLD')
plt.plot(dr['SPY'], beta_GLD*dr['SPY'] + alpha_GLD, '-', color='r')
plt.show()
