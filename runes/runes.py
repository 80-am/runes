#!/usr/bin/env python3
from datetime import datetime
from datetime import timezone
from dateutil.relativedelta import relativedelta

import config
import requests
import urllib
import pandas as pd

DOWNLOADS_LOCATION = config.DOWNLOADS_LOCATION

def get_epoch_timestamp(date):
    return str(date.replace(hour = 0, minute = 0, second = 0, microsecond = 0).timestamp()).split('.', 1)[0]

def get_years_ago(now, years):
    return get_epoch_timestamp(now - relativedelta(years=years))

def get_months_ago(now, months):
    return get_epoch_timestamp(now - relativedelta(months=months))

def deserialize_time_period(today, from_date):
    if from_date in ('1' or '1mo' or '1 month'):
        return get_months_ago(today, 1)
    elif from_date in ('2' or '3mo' or '3 months'):
        return get_months_ago(today, 3)
    elif from_date in ('3' or '6mo' or '6 months'):
        return get_months_ago(today, 6)
    elif from_date in ('4' or '1yr' or '1 year'):
        return get_years_ago(today, 1)
    elif from_date in ('5' or '5yr' or '5 years'):
        return get_years_ago(today, 5)
    else:
        return get_years_ago(today, 100)

class Runes():
    print(
""" ____  _   _ _   _ _____ ____  
|  _ \| | | | \ | | ____/ ___| 
| |_) | | | |  \| |  _| \___ \ 
|  _ <| |_| | |\  | |___ ___) |
|_| \_\\\___/|_| \_|_____|____/ 
""")

    ticker = input('Ticker to download: ').upper()

    today = datetime.now(timezone.utc)
    print("\nTime Period\n1) 1 month\n2) 3 months\n3) 6 months\n4) 1 year\n5) 5 years\n6) Max[default]")
    from_date = input('How many years of data do you want?: ').lower()
    from_date = deserialize_time_period(today, from_date)
    to_date = get_epoch_timestamp(today)

    print('\n1) Daily[default]\n2) Weekly \n3) Monthly')
    frequency = input('Frequency of data: ').lower()
    if frequency in ('3' or 'monthly' or '1mo'):
        frequency = '1mo'
    elif frequency in ('2' or 'weekly' or '1wk'):
        frequency = '1wk'
    else:
        frequency = '1d'

    CSV_URL = f'https://query1.finance.yahoo.com/v7/finance/download/{ticker}?period1={from_date}&period2={to_date}&interval={frequency}&events=history&includeAdjustedClose=true'
    print(CSV_URL)
    response = urllib.request.urlopen(CSV_URL)
    pd.read_csv(response).to_csv(f'{DOWNLOADS_LOCATION}{ticker}-{from_date}-{to_date}.csv', sep='\t', encoding='utf-8')
