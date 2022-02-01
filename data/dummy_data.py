import pandas as pd

users_per_day = pd.DataFrame(
    data={
        "date": [
            "2021-12-01",
            "2021-12-01",
            "2021-12-01",
            "2021-12-02",
            "2021-12-02",
            "2021-12-02",
            "2021-12-03",
            "2021-12-03",
            "2021-12-03",
        ],
        "type": [
            "total",
            "doc search",
            "text search",
            "total",
            "doc search",
            "text search",
            "total",
            "doc search",
            "text search",
        ],
        "total": [10, 5, 7, 12, 6, 8, 15, 8, 10],
    }
)

clicks_and_requests = pd.DataFrame(
    data={
        "date": [
            "2021-12-01",
            "2021-12-01",
            "2021-12-02",
            "2021-12-02",
            "2021-12-03",
            "2021-12-03",
        ],
        "type": [
            "doc search",
            "text search",
            "doc search",
            "text search",
            "doc search",
            "text search",
        ],
        "total": [0.2, 0.5, 0.3, 0.6, 0.4, 0.7],
    }
)


recurring_users_total = pd.DataFrame(
    data={
        "date": [
            "2021-12-01",
            "2021-12-01",
            "2021-12-01",
            "2021-12-02",
            "2021-12-02",
            "2021-12-02",
            "2021-12-03",
            "2021-12-03",
            "2021-12-03",
        ],
        "type": [
            "30 days",
            "14 days",
            "7 days",
            "30 days",
            "14 days",
            "7 days",
            "30 days",
            "14 days",
            "7 days",
        ],
        "total": [10, 7, 5, 12, 8, 6, 15, 10, 8],
    }
)

recurring_users_text_search = pd.DataFrame(
    data={
        "date": [
            "2021-12-01",
            "2021-12-01",
            "2021-12-01",
            "2021-12-02",
            "2021-12-02",
            "2021-12-02",
            "2021-12-03",
            "2021-12-03",
            "2021-12-03",
        ],
        "type": [
            "30 days",
            "14 days",
            "7 days",
            "30 days",
            "14 days",
            "7 days",
            "30 days",
            "14 days",
            "7 days",
        ],
        "total": [8, 5, 3, 10, 6, 5, 12, 8, 5],
    }
)

recurring_users_doc_search = pd.DataFrame(
    data={
        "date": [
            "2021-12-01",
            "2021-12-01",
            "2021-12-01",
            "2021-12-02",
            "2021-12-02",
            "2021-12-02",
            "2021-12-03",
            "2021-12-03",
            "2021-12-03",
        ],
        "type": [
            "30 days",
            "14 days",
            "7 days",
            "30 days",
            "14 days",
            "7 days",
            "30 days",
            "14 days",
            "7 days",
        ],
        "total": [8, 5, 3, 10, 6, 5, 12, 8, 5],
    }
)
