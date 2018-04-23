import os
import pandas as pd
import numpy as np
import time

raw_data_folder = os.path.join(os.path.join(os.path.dirname(__file__),".."),"Data")

file = raw_data_folder+"\\df_with_technical.pkl"
df = pd.read_pickle(file)

#back_testing
value = 0
value_list = []
pos = np.zeros(len(df.index))
bt_close = np.array(df.Close)
bt_rsi = np.array(df.RSI)
opens = False
for close,rsi in zip(bt_close,bt_rsi):
    if opens == False:
        if rsi > 80:
            current  ="Short"
            opens = True
            value += close
            value_list.append(close)
            print("Position {}\t Value of Fund {:.2f}\t  Open {}\tRSI {:.1f}\t Price {}".format(current,value,opens,rsi,close))
        elif rsi < 40:
            opens = True
            current = "Long"
            value += close*-1
            value_list.append(close *-1)
            print("Position {}\t Value of Fund {:.2f}\t Open {}\t RSI {:.1f}\t Price {}".format(current,value,opens,rsi,close))
    elif opens == True:
        if current == "Short":
            if rsi > 80:
                current = None
                opens = False
                value += close*-1
                value_list.append(close*-1)
                print("Position {}\t Value of Fund {:.2f}\t Open {}\tRSI {:.1f}\t Price {}".format(current,value,opens,rsi,close))
        elif current == "Long":
            if rsi < 40:
                current = None
                opens = False
                value += close
                value_list.append(close)
                print("Position {}\t Value of Fund {:.2f}\t Open {}\tRSI {:.1f}\t Price {}".format(current,value,opens,rsi,close))
##input("Go ahead : ")
