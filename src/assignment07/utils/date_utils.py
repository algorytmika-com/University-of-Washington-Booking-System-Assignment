from datetime import datetime, timedelta


def is_date_in_future_days(checked_date, days, compare_date=datetime.today()):
    if checked_date < compare_date or days < 0:
        return False
    future_date = compare_date + timedelta(days=days)
    if (checked_date <= future_date):
        return True
    return False


def get_date_converted_from_str(date_str, format):
    return datetime.strptime(date_str, format)


def add_date(current_date: datetime = datetime.today(),
             days_added: int = 0) -> datetime:
    d = current_date + timedelta(days=days_added)
    return d


def convert_datetime_to_str(d: datetime, format: str) -> str:
    return datetime.strftime(d, format)
