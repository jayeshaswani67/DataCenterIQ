import plotly.express as px
import pandas as pd


def bar_chart(
    df: pd.DataFrame,
    x: str,
    y: str,
    title: str
):
    fig = px.bar(
        df,
        x=x,
        y=y,
        title=title,
        text_auto=True
    )

    fig.update_layout(
        xaxis_title=x.replace("_", " ").title(),
        yaxis_title=y.replace("_", " ").title(),
        height=450
    )

    return fig


def line_chart(
    df: pd.DataFrame,
    x: str,
    y: str,
    title: str
):
    fig = px.line(
        df,
        x=x,
        y=y,
        markers=True,
        title=title
    )

    fig.update_layout(
        height=450
    )

    return fig


def scatter_chart(
    df: pd.DataFrame,
    x: str,
    y: str,
    title: str,
    color: str = None,
    hover_name: str = None
):
    fig = px.scatter(
        df,
        x=x,
        y=y,
        color=color,
        hover_name=hover_name,
        title=title,
        size_max=25
    )

    fig.update_layout(
        height=500
    )

    return fig


def histogram(
    df: pd.DataFrame,
    column: str,
    title: str
):
    fig = px.histogram(
        df,
        x=column,
        title=title,
        marginal="box"
    )

    fig.update_layout(
        height=450
    )

    return fig