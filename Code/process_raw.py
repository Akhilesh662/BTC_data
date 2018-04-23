import pandas as pd
import os
import glob
print("processing-----", __name__, " at ",__file__)
raw_data_folder = os.path.join(os.path.join(os.path.dirname(__file__),".."),"Data")
file = glob.glob(raw_data_folder+ "\\BTC_data.csv")[0]
df = pd.read_csv(file)
df.index = df["Date"]
df.index = pd.to_datetime(df.index)
##del df["Date"]


df["Open"] = df.Open.astype(float)
df["Close"] = df.Close.astype(float)
df["High"] = df.High.astype(float)
df["Low"] = df.Low.astype(float)
df.sort_index(ascending = True)
df.to_pickle(raw_data_folder+"\\bitcoin.pkl")


