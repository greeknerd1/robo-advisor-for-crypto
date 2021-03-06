# -*- coding: utf-8 -*-
"""risk_visualization.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/190WV7Gvl2ZybzwPabKP8ZSOHmpuSSvjX
"""

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

crypto_df = pd.read_csv("/content/crypto-markets.csv")
crypto_df.head()

crypto_df = crypto_df[crypto_df['date'].str.startswith("2018")]
crypto_df = crypto_df[crypto_df['date'] != "2018-11-30"]
crypto_df['daily_returns'] = (crypto_df['close'] - crypto_df['open']) / (crypto_df['open']) * 100
crypto_df.head()

def visualize_risk(crypto_name):
  cr_df = crypto_df[crypto_df['name'].str.lower() == crypto_name.lower()]
  ax = sns.scatterplot(x = 'open', y = 'close', data = cr_df)
  ax.set(xlabel = "Opening Price per Day for " + crypto_name, ylabel = "Closing Price per Day for " + crypto_name, 
        title = "Opening Price vs Closing Price daily")
  plt.show()
  plt.plot(cr_df['date'], np.log(cr_df['close']), label = crypto_name)
  plt.plot(crypto_df[crypto_df['name'] == "Bitcoin"]['date'], np.log(crypto_df[crypto_df['name'] == "Bitcoin"]['close']), label = "Bitcoin")
  plt.legend()
  plt.xlabel('Date')
  plt.ylabel('Daily Closing Price for ' + crypto_name +  ' Stock')
  plt.title('Daily Closing Price for ' + crypto_name + " Vs. Bitcoin")
  plt.show()
visualize_risk("xrp")