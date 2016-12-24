import pandas as pd
import matplotlib.pyplot as plt

from util import *

df = get_data(['GLD'], '2009-01-10', '2012-12-31')
dr = get_daily_returns(df)

# Plot histogram
dr['SPY'].hist(bins=20, label='SPY')
dr['GLD'].hist(bins=20, label='GLD')
plt.legend()
plt.show()
