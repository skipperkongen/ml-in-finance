import pandas as pd
import matplotlib.pyplot as plt
import math
from util import *
import sys

start_date = '2015-09-01'
end_date = '2016-12-01'

# Define portfolio
symbols = ['GOOG', 'XOM', 'GLD']
allocation = [0.4, 0.4, 0.2]
start_val = 10000

# Load data
df = get_data(symbols, start_date, end_date)

# Reference portfolio, S&P 500
df_reference = get_normalized(df['SPY']).to_frame('SPY') * start_val

# Filter for portfolio
df = df[symbols] # filter out SPY

# Compute cumulative return
df_normed = get_normalized(df)
df_alloced = df_normed * allocation
df_posval = df_alloced * start_val
df_portval = df_posval.sum(axis=1).to_frame('Portfolio')

# Compute Sharpe ratio
dr_portfolio = get_daily_returns(df_portval)
dr_reference = get_daily_returns(df_reference.sum(axis=1).to_frame())
print('Sharpe ratio portfolio:', get_sharpe_ratio(dr_portfolio))
print('Sharpe ratio reference:', get_sharpe_ratio(dr_reference))

# Plot
ax = df_portval.plot(title='Comparison', label='Portfolio')
df_reference.plot(label='SPY', ax=ax)
plt.legend(loc='upper left')
plt.show()
