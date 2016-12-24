import pandas as pd
import matplotlib.pyplot as plt

from util import *

df = get_data(['SPY', 'GLD', 'AAPL'], '2009-01-10', '2012-12-31')
dr = get_daily_returns(df)

# Plot histogram
dr.plot(kind='scatter', x='SPY', y='AAPL')
plt.show()
