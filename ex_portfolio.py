import pandas as pd
import matplotlib.pyplot as plt
from util import *

start_date = '2015-09-01'
end_date = '2016-12-01'
#symbols = ['AAPL', 'GOOG', 'XOM', 'GLD']
symbols = ['GOOG', 'XOM', 'GLD']
#symbols = ['GLD']

df = get_data(symbols, start_date, end_date)
df = df[symbols]

allocation = [1/len(symbols)] * len(symbols)
start_val = 10000
df_normed = get_normalized(df)
df_alloced = df_normed * allocation
df_posval = df_alloced * start_val
df_portval = df_posval.sum(axis=1)
df_portval.plot()
plt.show()
#alloc =
