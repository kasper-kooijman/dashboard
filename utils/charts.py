import altair as alt
import pandas as pd


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
            x="date",
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
            x="date",
            y="rolling_mean:Q",
            color=alt.Color("type", sort=legend_sort),
            tooltip=["total", "date"],
        )
    ).properties(title=title)


def layered_bar_chart(df, title):
    return (
        alt.Chart(df)
        .mark_bar(opacity=0.7)
        .encode(
            x="date",
            y=alt.Y("total:Q", stack=None),
            color="type",
            order=alt.Order("type", sort="descending"),
            tooltip=["total"],
        )
        .properties(title=title)
    )
