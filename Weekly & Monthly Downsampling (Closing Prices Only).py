# -*- coding: utf-8 -*-
"""
Created on Wed Jan 14 04:26:25 2026

@author: jgive

Mini‑Assignment 3 — Weekly & Monthly Downsampling (Closing Prices Only)
This assignment focuses on transforming intraday price data into daily, weekly, and monthly 
closing‑price series. The goal is to practice time‑series resampling and understand how 
changing the frequency of financial data affects smoothness and trend visibility.

Steps completed in this assignment:

Extracted the daily close by selecting the 15:30 timestamp from intraday data.

Resampled the daily close series to compute the weekly close (last value of each week).

Resampled the daily close series to compute the monthly close (last value of each month).

Plotted daily, weekly, and monthly closing prices to compare how each frequency smooths short‑term noise and highlights different market horizons.

Concept focus:  
Resampling changes the time resolution of a dataset. Daily closes capture short‑term 
fluctuations, weekly closes smooth out noise, and monthly closes reveal long‑term 
structure. Understanding these differences is essential for multi‑horizon modeling and 
feature engineering in quantitative research.
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

apple_data = 'C:/Users/jgive/Documents/Python Projects/Mini Projects/Data/aapl_intraday-30min_historical-data-03-17-2025.csv'
df = pd.read_csv(apple_data, index_col=0, parse_dates = True)

#Setting the index resolution to daily 
daily_close = df.between_time("15:30", "15:30").copy()
daily_close.index = daily_close.index.to_period('D')


#Setting the index resolution to Monthly
"""
.mean() only computes on numeric columns, but there exists
one non-numeric column in the dataframe,

""" 
Monthly_close = df.between_time("15:30", "15:30").copy()
Monthly_close = Monthly_close.resample('ME').last()

#Setting the index resolution to Monthly

Weekly_close = df.between_time("15:30", "15:30").copy()
Weekly_close = Weekly_close.resample('W').last()

daily_close['Last'].plot(figsize =(12,6))
Monthly_close['Last'].plot(figsize =(12,6))
Weekly_close['Last'].plot(figsize =(12,6))