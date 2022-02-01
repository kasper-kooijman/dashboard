import pandas as pd

from pymongo import MongoClient

from .data import load_clickdata, strftime


def get_users_per_day(search: MongoClient):
    users_text = get_users_per_day_textsearch(search)
    users_doc = get_users_per_day_docsearch(search)
    users_total = get_users_per_day_total(search)

    users_per_day = users_text.append(users_doc).append(users_total)
    return users_per_day.sort_values("date")


def get_users_per_day_textsearch(search: MongoClient):
    data = load_clickdata("text", search)
    data["date"] = strftime(data)
    return _get_users_per_day(data, "text_search")


def get_users_per_day_docsearch(search: MongoClient):
    data = load_clickdata("document", search)
    data = data[
        data["sent_from"].isin(
            ["document_search_recommendation", "document_search_result"]
        )
    ]
    data["date"] = strftime(data)
    return _get_users_per_day(data, "doc_search")


def get_users_per_day_total(search: MongoClient):
    data = pd.DataFrame(list(search.find({"sent_from": {"$exists": True}})))
    data = data[
        (
            data["sent_from"].isin(
                ["document_search_recommendation", "document_search_result"]
            )
        )
        | (data["type_"] == "text")
    ]

    data["date"] = strftime(data)
    return _get_users_per_day(data, "total")


def _get_users_per_day(data: pd.DataFrame, type_: str):
    data = (
        data[["date", "user_id"]]
        .groupby("date")
        .nunique()["user_id"]
        .reset_index()
        .rename(columns={"user_id": "total"})
    )
    data["type"] = type_
    return data
