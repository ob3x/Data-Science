import dash
from dash import dcc
from dash import html
import plotly.graph_objects as go
import pandas_datareader as web


df = web.DataReader(name="AMZN", data_source="stooq")
df.reset_index(inplace=True)
df = df[df.Date > "2019-01-01"]



app = dash.Dash(__name__)

app.layout = html.Div([

    html.H2(children="Hello Dash!"),

    dcc.Graph(
        figure=go.Figure([
            go.Bar(
                x=["2017", "2018", "2019"],
                y=[150, 180, 220,],
                name="lokalnie",
            ),
            go.Bar(
                x=["2017", "2018", "2019"],
                y=[100, 20, 80],
                name="online"
            )
            
        ])
    )

])

if __name__ == "__main__":
    app.run_server(debug=True)