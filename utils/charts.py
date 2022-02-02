import altair as alt
import pandas as pd


def get_date_range(source, step_size):
    return [source.iloc[i]["date"] for i in range(0, len(source), step_size)]


def simple_line_chart(source: pd.DataFrame, title: str):
    return (
        alt.Chart(source)
        .mark_line()
        .encode(x="date", y=alt.Y("total", scale=alt.Scale(domain=[0, 1])))
    ).properties(title=title, width=150)


def multi_line_chart(source: pd.DataFrame, title: str, legend_sort: list):
    return (
        alt.Chart(source)
        .mark_line()
        .encode(
            x=alt.X("date", axis=alt.Axis(values=get_date_range(source, 2))),
            y="total",
            color=alt.Color("type", sort=legend_sort),
            tooltip=["total"],
        )
    ).properties(title=title)


def multi_line_chart_rolling_mean(
    source: pd.DataFrame, title: str, legend_sort: list, days: int
):
    return (
        alt.Chart(source)
        .mark_line()
        .transform_window(rolling_mean="mean(total)", frame=[-days, 0])
        .encode(
            x=alt.X("date", axis=alt.Axis(values=get_date_range(source, 2))),
            y="rolling_mean:Q",
            color=alt.Color("type", sort=legend_sort),
            tooltip=["total", "date"],
        )
    ).properties(title=title)


def layered_bar_chart(source, title):
    return (
        alt.Chart(source)
        .mark_bar(opacity=0.7)
        .encode(
            x=alt.X("date", axis=alt.Axis(values=get_date_range(source, 2))),
            y=alt.Y("total:Q", stack=None),
            color="type",
            order=alt.Order("type", sort="descending"),
            tooltip=["total"],
        )
        .properties(title=title)
    )
