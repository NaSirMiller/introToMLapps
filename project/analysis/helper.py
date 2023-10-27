'''
This helper module is to create dataframes for each market index, i.e. S&P 500, and their data
from January 1st, 2010 to Now (December 31st, 2023)

Implementation comes from: https://towardsdatascience.com/analyzing-world-stock-indices-performance-in-python-610df6a578f
'''

#Imports
import datetime as dt 
import pandas as pd
import yfinance as yf


def create_market_data(market_index:str) -> pd.DataFrame: #Helper function to create different dataframes for market indexes from 2009 to 2023
  market_index_df = []
  ticker_data = yf.Ticker(market_index)
  ticker_df = ticker_data.history(period = "1d", start = "2010-1-1", end = "2023-12-31")
  market_index_df.append(ticker_df)
  market_index_df = pd.concat(market_index_df, axis = 0)
  
  market_index_df = market_index_df.drop(columns = ["Stock Splits", "Dividends", "Adj Close"]) #Dropping stock splits, dividends, and adj close due to Market indices not having said features
  market_index_df["Region"] = market_index_df.ticker.apply(lambda ticker: add_region(ticker))
  market_index_df = market_index_df.style.set_table_attributes("style='display:inline'").set_caption(market_index + " Data from January 2010 to December 2023")   #Giving the dataframe a title/name
  # market_index_df = market_index_df.reset_index()
  
  return market_index_df

def add_region(market_index: str) -> pd.DataFrame:
  region_idx= \
    { 'US & Canada' : ['^GSPC', '^DJI', '^IXIC', '^RUT','^GSPTSE'],
      'Latin America' : ['^BVSP', '^MXX', '^IPSA'],
      'East Asia' : ['^N225', '^HSI', '000001.SS', '399001.SZ', '^TWII', '^KS11'],
      'ASEAN & Oceania' : ['^STI', '^JKSE', '^KLSE','^AXJO',  '^NZ50'],
      'South & West Asia' : ['^BSESN', '^TA125.TA'],
      'Europe' : ['^FTSE', '^GDAXI', '^FCHI', '^STOXX50E','^N100', '^BFX']
    }

  for region in region_idx:
    if (market_index in region_idx[region]):
      return region

def add_date(market_index_df: pd.DataFrame) -> pd.DataFrame: #Add month and day of week features to dataframe
  # https://stackoverflow.com/questions/26105804/extract-month-from-date-in-python
  for date in market_index_df["Date"]:
    dtobj = dt.datetime.strptime(date, "%Y-%m-%d")
    market_index_df["Month"] = dtobj.month
    market_index_df["Days_of_Week"] = dtobj.dayofweek
  return market_index_df
    
def adjust_close(market_index_df: pd.DataFrame) -> pd.DataFrame: #Update price to have a universal "currency"
  price_change = []
  for open_price in market_index_df["Open"]: #Go through all open and closing prices
    for close_price in market_index_df["Close"]:
      price_change.append(((close_price - open_price) / open_price) * 100)
  market_index_df["Price_Change"] = price_change
  market_index_df = pd.concat(price_change, axis = 0)
  return market_index_df
  
def add_pollution_index(market_index_df: pd.DataFrame, pollution_index: pd.DataFrame) -> pd.DataFrame:
  pass

def get_impactful_events() -> dict: #Function to find the most impactful events on Stock Market from 2020 to 2023
  high_impact_times = {}
  covid = ["2020-1-1", "2023-05-11"]
  russia_ukraine = ["2022-02-24","2022-04-07"]
  third_infitada = ["2023-10-07", "2023-12-31"]
  high_impact_times["COVID"] = covid
  high_impact_times["Russian_Ukranian_War"] = russia_ukraine
  high_impact_times["Israeli_Hamas_War"] = third_infitada
  return high_impact_times