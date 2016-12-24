import pandas as pd
import matplotlib.pyplot as plt

from util import *

df = get_data(['GOOG', 'AAPL', 'GLD'], '2014-01-10', '2016-01-01')

dr = get_daily_returns(df)
rm = get_rolling_mean(df)
rstd = get_rolling_std(df)
lower_band, upper_band = get_bollinger_bands(rm, rstd)
ax = df.plot(title='Prices')
rm.plot(label='Rolling mean', ax=ax)
plt.show()
