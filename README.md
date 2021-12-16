# crypto-portfolio-advisor
## Sample Dashboard
Crypto Portfolio Advisor is a cryptocurrency portfo risk and recommendation tool powered by machine learning algorithm and front-end web services that aims for helping different levels of investors to achieve a more reliable cryptocurrency investment solution. This project was designed by the Crypto Robo Advisor team from UC Berkeley Data-X course. This project is mentored and advised by CEO of Anchain.ai, Victor Fang.

![ezgif com-gif-maker](https://user-images.githubusercontent.com/39391660/144360945-fc017110-767c-4b2b-bb34-068eedb318ce.gif)

## Installations
Install pip, then connect the UI to the existing notebook:

import ``` anvil.server```

Then run

```
pip install anvil-uplink
```


## Files

The main folder to be used is **engine**, which has combined data visualization, bayesian algorithm for potential prediction parts,
and risk functions.

Here is a breakdown of the ```engine``` folder,
<br>


|engine                |Function                                                                             |
|----------------------|-------------------------------------------------------------------------------------|
|**bayesian_pred.py**  |Initial algorithm for 'Bayesian regression for latent source model' method for predicting price variation of crypto.|
|**risk_scoring.py**   |Initial risk scoring methods                                                         |
|**risk_visualization.py**|Implemented risk visualization plot                                               |
|**calculate_risk.py** |Applies portfolio standard deviation formula to build correlation structures and calculated risk score based on variance      |
|**external.ipynb**    |Core notebook that contains data cleaning, anvil framework, portfolio risk functions, SARIMA models, dynamic asset numbers, and data visualization with ```plotly```  |
|**portfolio_profit_pred.ipynb** |Foundation of **external.ipynb**, including data preprocessing, model selections/simulations, and risk scoring 1.0  |

## Scraping

Mains scripts in the sourcing folder is: **coinmarketcap.py**, **defipulse.py**

Each scraping function takes in three arguments: data, soup and tag, and returns the open source data within the stated date range for the particular entity.

Our scraping scripts is for the data sourcing purpose and thus not connected to the application.

## Data Sources

We use **crypto-markets.csv**

- **About this file**:
    - **Observations: 942,000 Variables: 13 Crypto Tokens: 2,071**
    - **All historic open, high, low, close values for all cryptocurrencies.**
        - **Fixed duplicate coins sharing symbol by introducing coin slug**
        - **Added two new variables, close_ratio and spread**
        - **Close ratio is the daily close rate, min-maxed with the high and low values for the day.Close Ratio = (Close-Low)/(High-Low)**
        - **Spread is the $USD difference between the high and low values for the day.**
## System Architecture

<img width="1151" alt="Screen Shot 2021-12-03 at 2 10 50 PM" src="https://user-images.githubusercontent.com/39391660/144679653-47c3a07d-5526-45b1-9c74-e6a78704b4a0.png">

## Key Features
- Preprocessing
  - We uses ```Bayesian Regression``` for our initial cryptocurrency model building; uses `scrapping` and `simulation` to process initial sample data from DeFiPulse
- Model
  - Crypto Portfolio Advisor is powered by an ARIMA model, which is known for its performance in measure events that happen over a period of time. The model is used to understand past data or predict future data in a series. It’s used when a metric is recorded in regular intervals, from fractions of a second to daily, weekly or monthly periods. During the model selection process, we also tried using prophet model, Gradient Boost, and Bayesian but found out ARIMA model offers better AIC score.
- Scoring
  - Crypto Portfolio Advisor uses volarity and correlation based on the Portfolio Standard Deviation Formula. It is calculated based on the standard deviation of returns of each asset in the portfolio, the proportion of each asset in the overall portfolio i.e., their respective weights in the total portfolio, and also the correlation between each pair of assets in the portfolio. The main scoring file is ```calculate_risk.py```
  - A high portfolio standard deviation highlights that the portfolio risk is high, and return is more volatile in nature and, as such unstable as well.
  - A Portfolio with low Standard Deviation implies less volatility and more stability in the returns of a portfolio and is a very useful financial metric when comparing different portfolios.
- User Interface
  - Our application can either output a portfolio of the most profitable portfolio of five different cryptocurrencies based on an user’s selected risk tolerance, or calculates the risk of a user-given portfolio of cryptocurrencies additionally. Each of the feature comes with the current prediction time, a risk level, a pie chart of the recommended/input portfolio, and a historical daily returns for all 5 crypto in one portfolio on the purpose of better understanding. It also comes with a download plot as .png feature, which is easy for users to use.
  - This information gives new investors a list of cryptocurrencies to potentially invest in and accompanying graphs to show the reason the portfolio’s risk is evaluated the way it is

## Built with
- anvil
- Beautiful Soup
- plotly
- SARIMAX
- Bayesian Regression

## Team
Our team is formed by UC Berkeley students from various majors and backgrounds:

- Saahil Shangle      --*Business Administration BS, Data Science BA*
- Ian Chen            --*Development Engineering MDE*
- Gabriel Khouri-Haddad       --*Computer Science BA*
- Sora Kang         --*Master of Design MDES*
- Suvam Nayak       --*Data Science BA*
