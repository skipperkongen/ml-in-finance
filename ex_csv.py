import pandas as pd
import matplotlib.pyplot as plt

def debug(df, message='DataFrame'):
    print('------')
    print('{}:'.format(message))
    print(df.head())
    print('...')
    print(df.tail())
    print()

# Creates empty dataframe
start_date = '2015-01-01'
end_date = '2017-01-01'
dates = pd.date_range(start_date, end_date)
df1 = pd.DataFrame(index=dates)
df1 = df1.sort_index()

debug(df1, 'empty')

# Read SPY data
dfSPY = pd.read_csv(
    'data/SPY.csv', parse_dates=True, index_col='Date',
    usecols=['Date', 'Adj Close'], na_values=['nan'])
dfSPY = dfSPY.rename(columns={'Adj Close': 'SPY'})
dfSPY = dfSPY.sort_index()

debug(dfSPY, 'w. SPY')

# Join SPY
df1 = df1.join(dfSPY, how='inner')

# Add more symbols
symbols = ['AAPL', 'GOOG', 'GLD']
for symbol in symbols:
    df_temp = pd.read_csv(
        'data/{}.csv'.format(symbol), index_col='Date',
        parse_dates=True, usecols=['Date', 'Adj Close'], na_values=['nan'])
    df_temp = df_temp.rename(columns={'Adj Close': symbol})

    df1 = df1.join(df_temp)

debug(df1, 'w. all symbols')

# Normalize by first row
df1_norm = df1 / df1.ix[0,:]

debug(df1_norm, 'normalized')

# Slicing
df1_slice = df1.ix['2010-01-01':'2012-01-01', ['AAPL', 'GOOG']]

debug(df1_slice, 'sliced')


# Plot
#df1.plot()
#plt.title('Closing prices (adjusted)')
#plt.show()
