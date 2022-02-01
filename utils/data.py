import pandas as pd

from pymongo import MongoClient


def filter_weekends(df: pd.DataFrame):
    df["datetime"] = pd.to_datetime(df["date"])
    return df[df["datetime"].dt.weekday < 5]


def strftime(data: pd.DataFrame):
    return [cd.strftime("%Y-%m-%d") for cd in data["datetime"]]


def load_clickdata(type_: str, search: MongoClient):
    clickdata = search.find(
        {
            "sent_from": {"$exists": True},
            "type_": type_,
        }
    )
    return pd.DataFrame(list(clickdata))
