# -*- coding: utf-8 -*-
"""
Created on Sun Mar 29 23:42:16 2020

@author: DWiley
"""

import yfinance as yf
import pandas as pd
from yahooquery import Ticker
import datetime
import numpy as np
from datetime import timedelta

# reading in files that contains the stock tickers for each the DOW and SP500
dow_tickers = pd.read_excel('F:\\Python\\ImpactofCoronaVirus_Stocks\\Stocks\\Dow30.xlsx')['Ticker']
sp_tickers = pd.read_excel('F:\\Python\\ImpactofCoronaVirus_Stocks\\Stocks\\SP500.xlsx')['Ticker']

# establishing todays date so we can get the up to date information for the stocks
today = datetime.date.today()

# reformatting the date
today = str(today.year) + '-' + str(today.month).zfill(2) + '-' + str(today.day).zfill(2)







#####################################################################################
# Getting current information for each stock ticker
#####################################################################################


##################################
# DOW
##################################

# these empty lists will contain their respective information for the DOW
d_symbol = []
d_name = []
d_sector = []
d_industry = []
d_summ = []
d_add = []
d_city = []
d_state = []
d_zip = []
d_country = []
d_phone = []
d_website = []
d_pclose = []
d_open = []
d_daylow = []
d_dayhigh = []
d_volume = []
d_52c = []
d_52l = []
d_52h = []
d_logo = []

# Looping through the DOW tickers
for t in dow_tickers:
    
    # Some tickers can't be pulled with the yahoofinance package but can be using the Ticker
    # First trying with the yahoofinance 
    try:
        tic = yf.Ticker(t)
        info = tic.info
        
        
        
        symbol = info['symbol']
        name = info['longName']
        sector = info['sector']
        industry = info['industry']
        summ = info['longBusinessSummary']
        add = info['address1']
        city = info['city']
        state = info['state']
        z = info['zip']
        country = info['country']
        phone = info['phone']
        website = info['website']
        pclose = info['previousClose']
        o = info['open']
        daylow = info['dayLow']
        dayhigh = info['dayHigh']
        volume = info['volume']
        c52 = info['52WeekChange']
        l52 = info['fiftyTwoWeekLow']
        h52 = info['fiftyTwoWeekHigh']
        logo = info['logo_url']
    
    # if there's an error using the yfinance package it will jump here and use the Ticker package
    except:
        
        # some queries in the Ticker package lack information
        # first trying to see if there's information, if not it'll move on
        try:
            price_info = Ticker(t).price[t]
            summ_pro = Ticker(t).summary_profile[t]
            
            
            symbol = price_info['symbol']
            name = price_info['longName']
            sector = summ_pro['sector']
            industry = summ_pro['industry']
            summ = summ_pro['longBusinessSummary']
            add = summ_pro['address1']
            city = summ_pro['city']
            state = summ_pro['state']
            z = summ_pro['zip']
            country = summ_pro['country']
            phone = summ_pro['phone']
            website = summ_pro['website']
            pclose = price_info['regularMarketPreviousClose']
            o = price_info['regularMarketOpen']
            daylow = price_info['regularMarketDayLow']
            dayhigh = price_info['regularMarketDayHigh']
            volume = price_info['regularMarketVolume']
            c52 = ''
            l52 = Ticker(t).summary_detail[t]['fiftyTwoWeekLow']
            h52 = Ticker(t).summary_detail[t]['fiftyTwoWeekHigh']
            logo = ''
            
        # if the Ticker throws an error, it'll just make everything blank
        # there is a better way to handle this, but this was to save time due timeframe
        except:
            symbol = price_info['symbol']
            name = price_info['longName']
            sector = ''
            industry = ''
            summ = ''
            add = ''
            city = ''
            state = ''
            z = ''
            country = ''
            phone = ''
            website = ''
            pclose = ''
            o = ''
            daylow = ''
            dayhigh = ''
            volume = ''
            c52 = ''
            l52 = ''
            h52 = ''
            logo = ''
            
    # appending all temporary variables to their respective lists
    d_symbol.append(symbol)
    d_name.append(name)
    d_sector.append(sector)
    d_industry.append(industry)
    d_summ.append(summ)
    d_add.append(add)
    d_city.append(city)
    d_state.append(state)
    d_zip.append(z)
    d_country.append(country)
    d_phone.append(phone)
    d_website.append(website)
    d_pclose.append(pclose)
    d_open.append(o)
    d_daylow.append(daylow)
    d_dayhigh.append(dayhigh)
    d_volume.append(volume)
    d_52c.append(c52)
    d_52l.append(l52)
    d_52h.append(h52)
    d_logo.append(logo)
        
# taking all of the populated lists and creating a dataframe from them
dow_df = pd.DataFrame({'Symbol': d_symbol,
                       'Name': d_name,
                       'Sector': d_sector,
                       'Industry': d_industry,
                       'Summary': d_summ,
                       'Address': d_add,
                       'City': d_city,
                       'State': d_state,
                       'Zip': d_zip,
                       'Country': d_country,
                       'Phone': d_phone,
                       'Website': d_website,
                       'Previous Close': d_pclose,
                       'Open': d_open,
                       'Day Low': d_daylow,
                       'Day High': d_dayhigh,
                       'Volume': d_volume,
                       '52 Week Change': d_52c,
                       '52 Week Low': d_52l,
                       '52 Week High': d_52h,
                       'Logo Url': d_logo})
    
################################################################


##################################
# SP500
##################################

# these empty lists will contain their respective information for the SP500
sp_symbol = []
sp_name = []
sp_sector = []
sp_industry = []
sp_summ = []
sp_add = []
sp_city = []
sp_state = []
sp_zip = []
sp_country = []
sp_phone = []
sp_website = []
sp_pclose = []
sp_open = []
sp_daylow = []
sp_dayhigh = []
sp_volume = []
sp_52c = []
sp_52l = []
sp_52h = []
sp_logo = []


# Looping through the SP500 tickers
for t in sp_tickers:
    
    
    # Some tickers can't be pulled with the yahoofinance package but can be using the Ticker
    # First trying with the yahoofinance 
    try:
        tic = yf.Ticker(t)
        info = tic.info
        
        
        
        symbol = info['symbol']
        name = info['longName']
        sector = info['sector']
        industry = info['industry']
        summ = info['longBusinessSummary']
        add = info['address1']
        city = info['city']
        state = info['state']
        z = info['zip']
        country = info['country']
        phone = info['phone']
        website = info['website']
        pclose = info['previousClose']
        o = info['open']
        daylow = info['dayLow']
        dayhigh = info['dayHigh']
        volume = info['volume']
        c52 = info['52WeekChange']
        l52 = info['fiftyTwoWeekLow']
        h52 = info['fiftyTwoWeekHigh']
        logo = info['logo_url']
    
    # if there's an error using the yfinance package it will jump here and use the Ticker package
    except:
        
        # some queries in the Ticker package lack information
        # first trying to see if there's information, if not it'll move on
        try:
            price_info = Ticker(t).price[t]
            summ_pro = Ticker(t).summary_profile[t]
            
            symbol = price_info['symbol']
            name = price_info['longName']
            sector = summ_pro['sector']
            industry = summ_pro['industry']
            summ = summ_pro['longBusinessSummary']
            add = summ_pro['address1']
            city = summ_pro['city']
            state = summ_pro['state']
            z = summ_pro['zip']
            country = summ_pro['country']
            phone = summ_pro['phone']
            website = summ_pro['website']
            pclose = price_info['regularMarketPreviousClose']
            o = price_info['regularMarketOpen']
            daylow = price_info['regularMarketDayLow']
            dayhigh = price_info['regularMarketDayHigh']
            volume = price_info['regularMarketVolume']
            c52 = ''
            l52 = Ticker(t).summary_detail[t]['fiftyTwoWeekLow']
            h52 = Ticker(t).summary_detail[t]['fiftyTwoWeekHigh']
            logo = ''
        
        # if the Ticker throws an error, it'll just make everything blank
        # there is a better way to handle this, but this was to save time due timeframe
        except:
            symbol = price_info['symbol']
            name = price_info['longName']
            sector = ''
            industry = ''
            summ = ''
            add = ''
            city = ''
            state = ''
            z = ''
            country = ''
            phone = ''
            website = ''
            pclose = ''
            o = ''
            daylow = ''
            dayhigh = ''
            volume = ''
            c52 = ''
            l52 = ''
            h52 = ''
            logo = ''
    
    # appending all temporary variables to their respective lists
    sp_symbol.append(symbol)
    sp_name.append(name)
    sp_sector.append(sector)
    sp_industry.append(industry)
    sp_summ.append(summ)
    sp_add.append(add)
    sp_city.append(city)
    sp_state.append(state)
    sp_zip.append(z)
    sp_country.append(country)
    sp_phone.append(phone)
    sp_website.append(website)
    sp_pclose.append(pclose)
    sp_open.append(o)
    sp_daylow.append(daylow)
    sp_dayhigh.append(dayhigh)
    sp_volume.append(volume)
    sp_52c.append(c52)
    sp_52l.append(l52)
    sp_52h.append(h52)
    sp_logo.append(logo)
        
# Creating a dataframe from the populated lists
sp_df = pd.DataFrame({'Symbol': sp_symbol,
                       'Name': sp_name,
                       'Sector': sp_sector,
                       'Industry': sp_industry,
                       'Summary': sp_summ,
                       'Address': sp_add,
                       'City': sp_city,
                       'State': sp_state,
                       'Zip': sp_zip,
                       'Country': sp_country,
                       'Phone': sp_phone,
                       'Website': sp_website,
                       'Previous Close': sp_pclose,
                       'Open': sp_open,
                       'Day Low': sp_daylow,
                       'Day High': sp_dayhigh,
                       'Volume': sp_volume,
                       '52 Week Change': sp_52c,
                       '52 Week Low': sp_52l,
                       '52 Week High': sp_52h,
                       'Logo Url': sp_logo})
    
# creating two lists to be appended to both dataframes just created to indicate which stock index they are from
dow_index = ['DOW' for i in range(len(dow_df))]
sp_index = ['S&P' for i in range(len(sp_df))]

# appending the stock index lists
dow_df['Index'] = dow_index
sp_df['Index'] = sp_index

# writing the dataframes to excel files just for reference
dow_df.to_excel('F:\\Python\\ImpactofCoronaVirus_Stocks\\Stocks\\DowInfo.xlsx', index=False)
sp_df.to_excel('F:\\Python\\ImpactofCoronaVirus_Stocks\\Stocks\\SPInfo.xlsx', index=False)
    
# =============================================================================
# # getting current information for both DOW and SP500 indices just for reference (this was never used later)
# dow_index_df = pd.DataFrame.from_dict(yf.Ticker('^DJI').info, orient='index').T
# snp_index_df = pd.DataFrame.from_dict(yf.Ticker('^GSPC').info, orient='index').T
# 
# dow_index_df.to_excel('F:\\Python\\ImpactofCoronaVirus_Stocks\\Stocks\\dow_index_info.xlsx', index=False)
# snp_index_df.to_excel('F:\\Python\\ImpactofCoronaVirus_Stocks\\Stocks\\sp_index_info.xlsx', index=False)  
# =============================================================================







#######################################################################
# HISTORY
#######################################################################

# =============================================================================
# names = []
# dates = []
# opens = []
# closes = []
# highs = []
# lows = []
# volumes = []
# 

#     
# 

# 
# 
# for s in range(len(symbol)):
#     yf.Tickers()
#     
# 
#     
# stock_df = pd.DataFrame({'Name': names, 'Date': dates, 'Open': opens, 'Close': closes, 'High': highs, 'Low': lows, 'Volume': volumes})
#     
# 
#     
#     
# =============================================================================

# creating a single list that contains all of the stock tickers on both DOW and SP500
# this information is coming from the two dataframes we created
dow_sp_list = list(dow_df['Symbol']) + list(sp_df['Symbol'])

all_symbols = []

for s in dow_sp_list:
    if s not in all_symbols:
        all_symbols.append(s)

# appending the actual DOW and SP500 tickers themselves
all_symbols.append('^DJI')
all_symbols.append('^GSPC')


# getting the history for all of our stock tickers up to yesterday
all_hist = Ticker(all_symbols).history(start='2020-01-01', end=today)

#####################################
# stock history dataframe
#####################################
# =============================================================================
# 
# # the stock history information is stored in a dictionary format with tickers as keys
# # reformatting the dictionary into a dataframe but keeping the ticker for each ticker history row
# 
# # initializing empty lists to hold the information
# names = []
# dates = []
# opens = []
# closes = []
# highs = []
# lows = []
# volumes = []
# 
# 
# for a in all_hist:
#     
#     # using try/except if it can't find the data
# #    try:
#         for i in range(len(all_hist[a].index)):
#             #date = str(all_hist[a].index[i].date())
#             
#     #        for c in range(len(all_hist[a].columns)):
#                 
#            # try:
#                     
#                 name = a
#                 date = str(all_hist[a].index[i])
#                 high = all_hist[a].iloc[i]['high']
#                 close = all_hist[a].iloc[i]['close']
#                 o = all_hist[a].iloc[i]['open']
#                 low = all_hist[a].iloc[i]['low']
#                 volume = all_hist[a].iloc[i]['volume']
#                 
#                 names.append(name)
#                 dates.append(date)
#                 highs.append(high)
#                 closes.append(close)
#                 opens.append(o)
#                 lows.append(low)
#                 volumes.append(volume)
# =============================================================================

# =============================================================================
#             # If it can't find the history for a ticker, then keep the name but make everything NaN
#             except:
#         #        pass
#                     
#                 name = a
#                 date = np.NaN
#                 high = np.NaN
#                 close = np.NaN
#                 o = np.NaN
#                 low = np.NaN
#                 volume = np.NaN
# 
#                 names.append(name)
#                 dates.append(date)
#                 highs.append(high)
#                 closes.append(close)
#                 opens.append(o)
#                 lows.append(low)
#                 volumes.append(volume)
# =============================================================================
# =============================================================================
#     # appending each temporary variable to their respective list
#     names.append(name)
#     dates.append(date)
#     highs.append(high)
#     closes.append(close)
#     opens.append(o)
#     lows.append(low)
#     volumes.append(volume)
# =============================================================================
            
# reformatting the datetime into date
all_hist.index = all_hist.index.set_levels([all_hist.index.levels[0], [pd.to_datetime(i).date() for i in all_hist.index.levels[1]]])
    
# writing the final dataframe to excel
all_hist.to_excel('F:\\Python\\ImpactofCoronaVirus_Stocks\\Stocks\\all_history.xlsx', merge_cells=False)

# =============================================================================
# # creating a dataframe from the lists
# stock_df = pd.DataFrame({'Name': names, 'Date': dates, 'Open': opens, 'Close': closes, 'High': highs, 'Low': lows, 'Volume': volumes})
# 
# # writing the history dataframe into excel
# stock_df.to_excel('F:\\Python\\ImpactofCoronaVirus_Stocks\\Stocks\\all_history.xlsx', index=False)
# =============================================================================

#all_hist.to_excel('F:\\Python\\ImpactofCoronaVirus_Stocks\\Stocks\\stock_history.xlsx')

# =============================================================================
# 
# # Was trying to create the dataframe in a short optimize code I couldn't get it to work for some reason
# 
# all_hist_df = pd.DataFrame.from_dict({i: all_hist[i] 
#                            for i in all_hist.keys()},
#                        orient='index')
# 
# all_hist_df.to_excel('F:\\Python\\ImpactofCoronaVirus_Stocks\\Stocks\\all_history.xlsx')
# 
# all_symbols = []
# data = []
# 
# for sym, d in all_hist.items():
#     all_symbols.append(sym)
#     data.append(pd.DataFrame.from_dict(d, orient='index'))
# 
# pd.concat(data, keys=all_symbols)
# 
# 
#     
#     
# =============================================================================
    

    
    