import pandas as pd
import streamlit as st

from pymongo import MongoClient


def filter_weekends(df: pd.DataFrame):
    df.loc[:, "datetime"] = pd.to_datetime(df["date"])
    return df[df["datetime"].dt.weekday < 5]


def filter_users(data: pd.DataFrame):
    return data[~data["user_id"].isin(st.secrets["users"].values())]


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


def get_user_data(search, type_: str):
    if type_ == "recurring_users":
        new_data = pd.DataFrame(list(search.find({"sent_from": {"$exists": True}})))
        new_data = new_data[
            (
                new_data["sent_from"].isin(
                    ["document_search_recommendation", "document_search_result"]
                )
            )
            | (new_data["type_"] == "text")
        ]

    elif type_ == "users_per_day_text":
        new_data = load_clickdata("text", search)

    new_data.loc[:, "datestr"] = strftime(new_data)
    return new_data[["_id", "datetime", "user_id"]]
