import pandas as pd

from collections import Counter
from datetime import datetime, time, timedelta


def combine_recurring_users(data: pd.DataFrame):
    weekly = get_recurring_users(data, 7)
    weekly["type"] = "7 days"
    biweekly = get_recurring_users(data, 14)
    biweekly["type"] = "14 days"
    monthly = get_recurring_users(data, 30)
    monthly["type"] = "30 days"

    recurring_users = weekly.append(biweekly).append(monthly)
    recurring_users = recurring_users.sort_values("date")
    return recurring_users


def get_recurring_users(data: pd.DataFrame, n_days: int):

    start_date = min(data["datetime"]) - timedelta(days=n_days)
    start_date = datetime.combine(start_date, time())
    dates = pd.date_range(
        start_date, datetime.today() - timedelta(days=n_days), freq="d"
    )
    recurring_users = []
    for date in dates:
        end_date = date + timedelta(days=n_days)
        end_date = end_date.strftime("%Y-%m-%d")
        counts = {
            "date": end_date,
            "total": get_number_of_recurring_users(date, data, n_days),
        }
        recurring_users.append(counts)
    return pd.DataFrame(recurring_users)


def get_number_of_recurring_users(
    start_date: datetime, data: pd.DataFrame, n_days: int
):
    end_date = start_date + timedelta(days=n_days)
    weekly_interval = data[
        (data["datetime"] > start_date) & (data["datetime"] < end_date)
    ]
    weekly_interval.loc[:, "datestr"] = [
        cd.strftime("%Y-%m-%d") for cd in weekly_interval["datetime"]
    ]
    counts = weekly_interval.groupby(["user_id", "datestr"]).size()
    counts = Counter(counts.reset_index()["user_id"])
    return len({k: v for k, v in counts.items() if v > 1})
