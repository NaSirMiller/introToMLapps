'''
This helper module is to create dataframes for each market index, i.e. S&P 500, and their data
from January 1st, 2010 to Now (December 31st, 2023)

Implementation comes from: https://towardsdatascience.com/analyzing-world-stock-indices-performance-in-python-610df6a578f
'''

#Imports
import datetime as dt 
import pandas as pd
import yfinance as yf

#Helper function to create different dataframes for market indexes from 2009 to 2023
def createMarketData(market_index:str) -> pd.DataFrame:
  market_index_df = []
  ticker_data = yf.Ticker(market_index)
  ticker_df = ticker_data.history(period = "1d", start = "2010-1-1", end = "2023-12-31")
  market_index_df.append(ticker_df)
  market_index_df = pd.concat(market_index_df, axis = 0)
  
  #Giving the dataframe a title/name
  market_index_df = market_index_df.style.set_table_attributes("style='display:inline'").set_caption(market_index + " Data from January 2010 to December 2023")
  # market_index_df = market_index_df.reset_index()
  
  #Dropping stock splits, dividends, and adj close due to Market indices not having said feeatures
  market_index_df = market_index_df.drop(columns = ["Stock Splits", "Dividends", "Adj Close"])
  return market_index_df

def addPolutionIndex(market_index_df: pd.DataFrame, pollution_index: pd.DataFrame) -> pd.DataFrame:
  pass