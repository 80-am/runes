#!/usr/bin/env python3
from datetime import datetime
from datetime import timezone
from periods import Periods

import config
import requests
import urllib
import pandas as pd

DOWNLOADS_LOCATION = config.DOWNLOADS_LOCATION


class Runes():

    print(
        """ ____  _   _ _   _ _____ ____  
|  _ \| | | | \ | | ____/ ___| 
| |_) | | | |  \| |  _| \___ \ 
|  _ <| |_| | |\  | |___ ___) |
|_| \_\\\___/|_| \_|_____|____/ 
""")

    ticker = input('Ticker to download: ').upper()

    p = Periods()
    today = datetime.now(timezone.utc)
    print(
        "\nTime Period\n1) 1 month\n2) 3 months\n3) 6 months\n4) 1 year\n5) 5 years\n6) Max[default]")
    from_date = input('How many years of data do you want?: ').lower()
    from_date = p.deserialize_time_period(today, from_date)
    to_date = p.get_epoch_timestamp(today)

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
    pd.read_csv(response).to_csv(
        f'{DOWNLOADS_LOCATION}{ticker}-{from_date}-{to_date}.csv', sep='\t', encoding='utf-8')
