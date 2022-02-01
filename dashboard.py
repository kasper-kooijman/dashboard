import pandas as pd
import streamlit as st

from pymongo import MongoClient

from utils.charts import (
    layered_bar_chart,
    multi_line_chart,
    multi_line_chart_rolling_mean,
)

from utils.click_request_ratio import (
    get_ratio_text_search,
    get_ratio_doc_search,
    prepare_bar_chart,
)
from utils.data import filter_weekends
from utils.recurring_users import (
    combine_deduced_with_new_data,
    combine_recurring_users,
)
from utils.users_per_day import get_users_per_day

client = MongoClient(**st.secrets["mongo"])
SEARCH = client.db.PRODUCTION.search

# Data up until January 28, where we had to deduce clickdata ourselves.
data_deduced = pd.read_csv("data/clickdata_deduced.csv", parse_dates=["date"])
users_per_day = pd.read_csv("data/users_per_day_docsearch_deduced.csv")
clicks_requests = pd.read_csv("data/clicks_requests_deduced.csv")


users_per_day = users_per_day.append(get_users_per_day(SEARCH))
clicks_requests = clicks_requests.append(get_ratio_doc_search(SEARCH))
clicks_requests = clicks_requests.append(get_ratio_text_search(SEARCH))

recurring_users = combine_deduced_with_new_data(SEARCH, data_deduced)
recurring_users = combine_recurring_users(recurring_users)

# In the sidebar we write:
#     - Total number of requests
#     - Total number of opened results
#     - Total number of users
st.sidebar.write(f"Total number of requests: {sum(clicks_requests['requests'])}")
st.sidebar.write(f"Total number opened results: {sum(clicks_requests['clicks'])}")


# Number of different users per day per feature
users_per_day = filter_weekends(users_per_day)
chart = multi_line_chart_rolling_mean(
    source=users_per_day,
    title="Different users per weekday per feature",
    legend_sort=["total", "doc_search", "text_search"],
    days=5,
)
st.altair_chart(chart, use_container_width=True)

# Number of recurring users
chart = multi_line_chart(
    recurring_users,
    title="Number of recurring users",
    legend_sort=["30 days", "14 days", "7 days"],
)
st.altair_chart(chart, use_container_width=True)

# Ratio of number of clicks to the number of requests
clicks_requests = filter_weekends(clicks_requests)
chart = multi_line_chart_rolling_mean(
    clicks_requests,
    title="Ratio of number of clicks compared to requests per weekday per feature",
    legend_sort=["text_search", "doc_search"],
    days=5,
)
st.altair_chart(chart, use_container_width=True)


# Number of clicks and requests doc search
clicks_requests_docsearch = prepare_bar_chart(clicks_requests, "doc_search")
chart = layered_bar_chart(
    clicks_requests_docsearch,
    title="Number of clicks and requests per day for doc search",
)
st.altair_chart(chart, use_container_width=True)


clicks_requests_docsearch = prepare_bar_chart(clicks_requests, "text_search")
chart = layered_bar_chart(
    clicks_requests_docsearch,
    title="Number of clicks and requests per day for doc search",
)
st.altair_chart(chart, use_container_width=True)
