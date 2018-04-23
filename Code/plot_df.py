import pandas as pd
import os
import matplotlib.pyplot as plt
import seaborn

plt.style.use('fivethirtyeight')
print("processing-----", __name__, " at ",__file__)
raw_data_folder = os.path.join(os.path.join(os.path.dirname(__file__),".."),"Data")
file = raw_data_folder +"\\df_with_technical.pkl"
df = pd.read_pickle(file)
plt.figure(1)
plt.subplot(211)
plt.plot(df["Close"],label = "Close")
plt.plot(df["MA5"],label = "Moving Average 5 Days")
plt.plot(df["MA19"],label = "Moving Average 19 Days")
plt.plot(df["EMA"],label = "Exp Moving Average")
#plt.fill_between(df.index,df['BBANDUP'],df['BBANDLO'],facecolor = 'lightgreen')
plt.legend(loc = 'best')
plt.subplot(212)
axes = plt.gca()
axes.set_ylim([0,100])
plt.plot(df["RSI"])
##plt.fill_between(df.index,70,30,facecolor = 'lightgreen')
plt.show()


