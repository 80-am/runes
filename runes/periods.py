from dateutil.relativedelta import relativedelta

class Periods():

    def get_epoch_timestamp(self, date):
        return str(date.replace(hour = 0, minute = 0, second = 0, microsecond = 0).timestamp()).split('.', 1)[0]

    def get_years_ago(now, years):
        return self.get_epoch_timestamp(now - relativedelta(years=years))

    def get_months_ago(self, now, months):
        return self.get_epoch_timestamp(now - relativedelta(months=months))

    def deserialize_time_period(self, today, from_date):
        if from_date in ('1' or '1mo' or '1 month'):
            return self.get_months_ago(today, 1)
        elif from_date in ('2' or '3mo' or '3 months'):
            return self.get_months_ago(today, 3)
        elif from_date in ('3' or '6mo' or '6 months'):
            return self.get_months_ago(today, 6)
        elif from_date in ('4' or '1yr' or '1 year'):
            return self.get_years_ago(today, 1)
        elif from_date in ('5' or '5yr' or '5 years'):
            return self.get_years_ago(today, 5)
        else:
            return self.get_years_ago(today, 100)
