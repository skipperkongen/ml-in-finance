import pandas as pd
import matplotlib.pyplot as plt
import math

def get_data(symbols, start_date, end_date, fill=True):
    dates = pd.date_range(start_date, end_date)
    df = pd.DataFrame(index=dates)
    df = df.sort_index()

    # Always join on SPY
    dfSPY = pd.read_csv(
        'data/SPY.csv', parse_dates=True, index_col='Date',
        usecols=['Date', 'Adj Close'], na_values=['nan']
    )
    dfSPY = dfSPY.rename(columns={'Adj Close': 'SPY'})
    dfSPY = dfSPY.sort_index()
    df = df.join(dfSPY, how='inner')
    for symbol in symbols:
        if symbol == 'SPY': continue
        df_temp = pd.read_csv(
            'data/{}.csv'.format(symbol), index_col='Date',
            parse_dates=True, usecols=['Date', 'Adj Close'], na_values=['nan'])
        df_temp = df_temp.rename(columns={'Adj Close': symbol})
        df = df.join(df_temp)

    # Fill (optional)
    if fill:
        df.fillna(method='ffill', inplace=True)
        df.fillna(method='bfill', inplace=True)

    return df

def get_sharpe_ratio(df, risk_free=0.0):
    df_summed = df.sum(axis=1)
    return math.sqrt(252) * (df_summed.mean() - risk_free) / df_summed.std()

def get_daily_returns(df):
    daily_returns = df / df.shift(1) - 1
    daily_returns.ix[0, :] = 0
    return daily_returns

def get_normalized(df):
    return df / df.ix[0,:]

def get_bollinger_bands(rm, rstd, lf=2, uf=2):
    return rm - rstd * lf, rm + rstd * uf

def get_rolling_mean(df, window=20):
    return df.rolling(center=False,window=window).mean()

def get_rolling_std(df, window=20):
    return df.rolling(center=False,window=window).std()
