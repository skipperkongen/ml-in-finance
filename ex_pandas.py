import pandas as pd
import matplotlib.pyplot as plt

def debug(df, message='DataFrame'):
    print('------')
    print('{}:'.format(message))
    print(df.head())
    print('...')
    print(df.tail())
    print()

# Create empty dataframe
start_date = '2006-01-01'
end_date = '2017-01-01'
dates = pd.date_range(start_date, end_date)
df1 = pd.DataFrame(index=dates)
df1 = df1.sort_index()

# Join SPY
dfSPY = pd.read_csv(
    'data/SPY.csv', parse_dates=True, index_col='Date',
    usecols=['Date', 'Adj Close'], na_values=['nan'])
dfSPY = dfSPY.rename(columns={'Adj Close': 'SPY'})
dfSPY = dfSPY.sort_index()
df1 = df1.join(dfSPY, how='inner')

# Join AAPL, GOOG, GLD
symbols = ['AAPL', 'GOOG', 'GLD']
for symbol in symbols:
    df_temp = pd.read_csv(
        'data/{}.csv'.format(symbol), index_col='Date',
        parse_dates=True, usecols=['Date', 'Adj Close'], na_values=['nan'])
    df_temp = df_temp.rename(columns={'Adj Close': symbol})

    df1 = df1.join(df_temp)

# Slice
df_slice = df1.ix['2015-05-01':'2017-05-31', ['AAPL', 'GOOG']]

# Normalize (by first row)
df_normalized = df1 / df1.ix[0,:]

# Global statistics, i.e mean + 33 other
print('-------')
print('Global statistics')
print(df1.mean())
print(df1.median())
print(df1.std())
print()

# Bollinger bands
df_slice = df1.ix['2015-01-01':'2015-12-31', 'SPY']
rm_SPY = df_slice.rolling(center=False,window=20).mean()
rstd_SPY = df_slice.rolling(center=False,window=20).std()
lower_band, upper_band = rm_SPY + rstd_SPY * 2, rm_SPY - rstd_SPY * 2

# Plot
ax = df_slice.plot(title='SPY rolling mean', label='SPY')
rm_SPY.plot(label='Rolling mean', ax=ax)
lower_band.plot(label='Lower band', ax=ax)
upper_band.plot(label='Upper band', ax=ax)
ax.set_xlabel('Date')
ax.set_ylabel('Price')
ax.legend('upper left')
plt.show()
