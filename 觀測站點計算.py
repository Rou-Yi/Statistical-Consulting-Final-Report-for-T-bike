# -*- coding: utf-8 -*-
"""
Created on Fri Dec 17 00:48:43 2021

@author: Rou_yi
"""
import pandas as pd
import numpy as np

df = pd.read_csv("C:/Users/Rou_yi/OneDrive/上課/統計諮詢/統諮期末報告/data/租賃站資訊-.csv")
df_2 = pd.read_excel("C:/Users/Rou_yi/OneDrive/上課/統計諮詢/統諮期末報告/data/觀測站點.xlsx")

ans = []
for i in range(77):
    if i == 26:
        ls = []
        for j in range(36):
            a = (df.loc[i, 'Latitude'] - df_2.loc[j, '緯度'])**2 
            b = (df.loc[i, 'Longitude'] - df_2.loc[j, '經度'])**2
            dist = (a + b) ** 0.5
            ls.append(dist)
    
        print(np.where(ls == min(ls))[0], min(ls))
        ans.extend(df_2.loc[np.where(ls == min(ls))[0], '站名'].tolist())

df_3 = pd.DataFrame({"站點":ans})
df_3.to_excel("C:/Users/Rou_yi/OneDrive/上課/統計諮詢/統諮期末報告/data/a.xlsx")


