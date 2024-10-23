import pandas as pd
import plotly.express as px
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))


def players_per_nationality():
    df = pd.read_csv("premier_league_players.csv")

    country_counts = df["nationality"].value_counts().reset_index()
    country_counts.columns = ["Country", "Number of players"]

    country_counts = country_counts[country_counts["Number of players"] >= 10]

    fig = px.bar(
        country_counts,
        x="Country",
        y="Number of players",
        title="Number of players per Country in PL",
        labels={"Number of players": "Number of players"},
        color="Number of players",
        color_continuous_scale="twilight",
    )

    fig.update_traces(texttemplate="%{y}", textposition="outside")

    fig.update_layout(height=200, margin=dict(l=10, r=10, t=25, b=20))
    
    fig.write_html("Players_per_Country.html")
