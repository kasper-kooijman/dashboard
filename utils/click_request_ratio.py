import pandas as pd

from pymongo import MongoClient

from .data import load_clickdata, strftime


def get_ratio_text_search(search: MongoClient):
    requests = load_clickdata("text", search)
    document_requests = load_clickdata("document", search)
    clicks = document_requests[document_requests["sent_from"] == "text_search_result"]

    clicks_requests = count_clicks_and_requests(clicks, requests)
    clicks_requests["type"] = "text_search"
    return clicks_requests


def get_ratio_doc_search(search: MongoClient):
    requests = load_clickdata("document", search)
    clicks = requests[
        requests["sent_from"].isin(
            ["document_search_recommendation", "document_search_result"]
        )
    ]

    clicks_requests = count_clicks_and_requests(clicks, requests)
    clicks_requests["type"] = "doc_search"
    return clicks_requests


def count_clicks_and_requests(clicks, requests):
    requests["date"] = strftime(requests)
    clicks["date"] = strftime(clicks)

    clicks = count(clicks, "clicks")
    requests = count(requests, "requests")
    clicks_requests = pd.merge(clicks, requests)
    clicks_requests["total"] = clicks_requests["clicks"] / clicks_requests["requests"]
    return clicks_requests


def count(clicks: pd.DataFrame, type_: str):
    return (
        pd.DataFrame(clicks["date"].value_counts())
        .reset_index()
        .rename(columns={"date": type_, "index": "date"})
    )


def prepare_bar_chart(clicks_requests: pd.DataFrame, type_: str):
    data = clicks_requests[clicks_requests["type"] == type_]

    clicks = data[["date", "clicks"]].rename(columns={"clicks": "total"})
    clicks["type"] = "clicks"
    requests = data[["date", "requests"]].rename(columns={"requests": "total"})
    requests["type"] = "requests"
    clicks_requests = clicks.append(requests).sort_values(by="date")
    print(clicks_requests)
    return clicks_requests