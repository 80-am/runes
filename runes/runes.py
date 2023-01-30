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


class Runes():
    print(
""" ____  _   _ _   _ _____ ____  
|  _ \| | | | \ | | ____/ ___| 
| |_) | | | |  \| |  _| \___ \ 
|  _ <| |_| | |\  | |___ ___) |
|_| \_\\\___/|_| \_|_____|____/ 
""")

    ticker = input("Ticker to download: ").upper()

    today = datetime.now(timezone.utc)
    from_date = get_years_ago(today, 10)
    to_date = get_epoch_timestamp(today)

    print('\n1) Daily\n2) Weekly \n3) Monthly')
    frequency = input('Frequency of data: ')
    if frequency.lower() in ('1' or 'daily' or '1d'):
        frequency = '1d'
    elif frequency.lower() in ('2' or 'weekly' or '1wk'):
        frequency = '1wk'
    else:
        frequency = '1mo'

    CSV_URL = f'https://query1.finance.yahoo.com/v7/finance/download/{ticker}?period1={from_date}&period2={to_date}&interval={frequency}&events=history&includeAdjustedClose=true'
    response = urllib.request.urlopen(CSV_URL)
    pd.read_csv(response).to_csv(f'{DOWNLOADS_LOCATION}{ticker}-{from_date}-{to_date}.csv', sep='\t', encoding='utf-8')
