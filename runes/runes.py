#!/usr/bin/env python3
from datetime import datetime
from datetime import timezone
from dateutil.relativedelta import relativedelta

import requests
import urllib
import pandas as pd


def get_epoch_timestamp(date):
    return str(date.replace(hour = 0, minute = 0, second = 0, microsecond = 0).timestamp()).split('.', 1)[0]

def get_years_ago(now, years):
    return get_epoch_timestamp(now - relativedelta(years=years))


class Runes():
    ticker = "TSLA"

    today = datetime.now(timezone.utc)
    from_date = get_years_ago(today, 10)
    to_date = get_epoch_timestamp(today)
    print(from_date)
    print(to_date)

    frequency = "1d" # 1d, 1wk, 1mo

    CSV_URL = f'https://query1.finance.yahoo.com/v7/finance/download/{ticker}?period1={from_date}&period2={to_date}&interval={frequency}&events=history&includeAdjustedClose=true'
    response = urllib.request.urlopen(CSV_URL)
    pd.read_csv(response).to_csv(f'{ticker}.csv', sep='\t', encoding='utf-8')
