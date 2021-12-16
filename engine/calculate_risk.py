# -*- coding: utf-8 -*-
"""calculate_risk.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1_oKEjl4iTKPGTbDa_nF4kQprTb-ioF_r
"""

pip install anvil-uplink

import numpy as np
import pandas as pd
import anvil.server

crypto_df = pd.read_csv("crypto-markets.csv")
crypto_df.head()

crypto_df['daily_returns'] = (crypto_df['close'] - crypto_df['open']) / (crypto_df['open']) * 100
crypto_df['name'].unique().shape[0]

bt_df = crypto_df[crypto_df['name'] == "Bitcoin"]
bt_df.tail()

four_two_df = crypto_df[crypto_df['name'] == "Project-X"]
four_two_df.tail()

crypto_df['name'].unique().shape[0]

lst = list()
lst1 = list()
def calculate_volatility(crypto_name):
  bt_df = crypto_df[crypto_df['name'].str.lower() == "bitcoin"]
  b1_df = crypto_df[crypto_df['name'] == crypto_name]
  if (b1_df.shape[0] < bt_df.shape[0]):
    arr = b1_df['date']
    bt_df = bt_df[bt_df['date'].isin(arr)]
  if (b1_df.shape[0] > bt_df.shape[0]):
    arr = bt_df['date']
    b1_df = b1_df[b1_df['date'].isin(arr)]
  benchmark_std = np.std(bt_df['daily_returns'])
  b1_std = np.std(b1_df['daily_returns'])
  temp = np.corrcoef(b1_df['daily_returns'], bt_df['daily_returns'])[0][1]
  return temp * (b1_std / benchmark_std), temp

for name in crypto_df['name'].unique():
  temp = calculate_volatility(name)
  if temp is not None:
    beta, corr = temp
    lst.append(beta)
    lst1.append(corr)
  else:
    lst.append(None)
    lst1.append(None)

names = [x for x in crypto_df['name'].unique()]
df_betas = pd.DataFrame({"Name": names, "Beta": lst, "Correlation": lst1})
df_cleaned = df_betas[df_betas['Beta'].notna()]
df_cleaned.sort_values("Beta", ascending = False)
df_cleaned.tail()

df_cleaned.to_csv("crypto_betas")

df_betas = pd.read_csv("/content/crypto_betas")
df_betas.shape[0]

#anvil.server.connect("2FHPU6NFGHWS3MPOZHU2XZID-G3THAFGNA7MMKPUF")

@anvil.server.callable

def calculate_risk(names, percentages):
  betas = list()
  if (sum([int(percentage) for percentage in percentages]) != 100):
      return "The Percentages Do Not Add Up To 100!"
  for i in range(len(names)):
    betas.append(df_betas[df_betas['Name'] == names[i].lower()]['Beta'].iloc[0] * (int(percentages[i]) / 100))
  risk_score = np.sum(betas)
  return risk_score 

#anvil.server.wait_forever()

def calculate_risk1(names, percentages):
  score = 0;
  name_len = len(names)
  i = 0
  while i < name_len:
      if (names[i].lower() not in set(crypto_df['symbol'].str.lower().unique())):
        names.remove(names[i])
        name_len -= 1
        continue;
      else:
        x = crypto_df[crypto_df['symbol'].str.lower() == names[i].lower()]['daily_returns']
        score += percentages[i] * np.var(x)
      i += 1 
  for i in range(len(names)):
    for j in range(len(names)):
      first = crypto_df[crypto_df['symbol'].str.lower() == names[i]]
      second = crypto_df[crypto_df['symbol'].str.lower() == names[j]]
      if (i != j):
        if (first.shape[0] < second.shape[0]):
          arr = first['date']
          second = second[second['date'].isin(arr)]
        if (first.shape[0] > second.shape[0]):
          arr = second['date']
          first = first[first['date'].isin(arr)]
        score += percentages[i] * percentages[j] * np.cov(first['daily_returns'], second['daily_returns'])[0][1]
  return np.sqrt(score)

lst = ["lies", "btc", "eth", "bnb", "usdt","ada", "xrp", "doge"]
lst1 = [.1] * 10

calculate_risk1(lst, lst1), np.std(crypto_df[crypto_df['name'].str.lower() == "bitcoin"]['daily_returns'])

"btc" in set(crypto_df['symbol'].str.lower().unique())

import itertools
risks = list()
portfolios = list()
for portfolio in itertools.combinations(lst, 4):
  percentages = [.25] * 4
  portfolios.append(portfolio)
  risks.append(calculate_risk1(portfolio, percentages))

df_portfolio_risks = pd.DataFrame({"Porfolio": portfolios, "Risk": risks}).sort_values("Risk", ascending = True)
df_portfolio_risks.tail()

crypto_df[crypto_df['name'].str.lower() == "bitcoin"].tail()

import matplotlib.pyplot as plt
data = df_portfolio_risks['Risk']
bins = np.linspace(0, 10, 10)
plt.hist(data, bins = bins)
plt.xlabel("Risk Score")
plt.ylabel("Density")