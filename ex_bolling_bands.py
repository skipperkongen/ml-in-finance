import pandas as pd
import matplotlib.pyplot as plt

from util import *

df = get_data(['GOOG'], '2015-01-10', '2016-01-01')

rm = get_rolling_mean(df)
rstd = get_rolling_std(df)
lower_band, upper_band = get_bollinger_bands(rm, rstd)
ax = df.plot(title='Bollinger Bands', label='SPY')
rm.plot(label='Rolling mean', ax=ax)
lower_band.plot(label='Lower band', ax=ax)
upper_band.plot(label='Upper band', ax=ax)
plt.show()
