import pandas as pd
import matplotlib.pyplot as plt

from util import *

df = get_data([], '2009-01-10', '2012-12-31')
dr = get_daily_returns(df)

print(dr.head())

#df.plot(title='SPY')
#dr.plot(title='Daily returns', label='SPY')
dr.hist()
plt.show()
