import pandas as pd
import os
import matplotlib.pyplot as plt
import seaborn

def BollingerBand(df, column="Close", period=20):
    sma = df[column].rolling(window=period, min_periods=period - 1).mean()
    std = df[column].rolling(window=period, min_periods=period - 1).std()
    up = (sma + (std * 2)).to_frame('BBANDUP')
    lower = (sma - (std * 2)).to_frame('BBANDLO')
    return df.join(up).join(lower)

def EMA(df, column="Close", period=20):
    ema = df[column].ewm(span=period, min_periods=period - 1).mean()
    return df.join(ema.to_frame('EMA'))


def RSI(df, column="Close", period=14):
    # wilder's RSI
    delta = df[column].diff()
    up, down = delta.copy(), delta.copy()
    up[up < 0] = 0
    down[down > 0] = 0
    rUp = up.ewm(com=period - 1,  adjust=False).mean()
    rDown = down.ewm(com=period - 1, adjust=False).mean().abs()
    rsi = 100 - 100 / (1 + rUp / rDown)    
    return df.join(rsi.to_frame('RSI'))

print("processing-----", __name__, " at ",__file__)
raw_data_folder = os.path.join(os.path.join(os.path.dirname(__file__),".."),"Data")
file = raw_data_folder +"\\bitcoin.pkl"
df = pd.read_pickle(file)
df = df.sort_index()
df["RETURNS"] = df["Close"]/df["Close"].shift(1)
df["MA5"] = df["Close"].rolling(window = 5).mean()
df["MA19"] = df["Close"].rolling(window = 19).mean()
df = BollingerBand(df)
df = EMA(df)
df = RSI(df)
df.to_pickle(raw_data_folder+"\\df_with_technical.pkl")
