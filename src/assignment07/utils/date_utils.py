from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta

def is_date_in_future_days(checked_date, days, compare_date = datetime.today()):
    if checked_date < compare_date or days < 0:
        return False
    future_date = compare_date + timedelta(days = days)
    if(checked_date <= future_date):
        return True
    return False

def get_date_converted_from_str(date_str, format):
    return datetime.strptime(date_str, format)