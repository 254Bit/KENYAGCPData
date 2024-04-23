import dash
from dash import html #Used to create HTML Objects
from dash import dcc
import plotly.express as px # To create our graphs, a powerful functionality for processing data with minimal preparation
import pandas as pd

#Load and read the data
data = pd.read_csv("gcp_economic_sectors.csv")
#To create a plotly figure for use by dcc.graph()
fig = px.line(
    data, x='Year', 
    y=['GCP'], 
    title='GCP over the years', 
    color_discrete_map={'GCP':'gold'}
)


fig.update_layout(
    template ='plotly.dark',
    xaxis_title = 'Year',
    yaxis_title = 'GCP',
    font = dict(
        family ='Verdana, sans-serif'
        size = 18,
        color ='white',
    )
)


app = dash.Dash(__name__) #Constructor: Is creating the dash application
app.title = 'GCP over the years'

app.layout = html.Div(
    id='app-container',
    children=[
        html.Div(
            id='header-area',
            style={'backgroundColor':'black'},
        ),
        html.H1(
            id='header-title',
            style={'color': 'white', 'fontFamily':'Verdana, sans-serif'},
            children='Kenya Gross County Product(2018-2020)Data Challenge',
            ),
        html.P(
            id='header-description',
            children=('Year vs GCP'),
            ),
    ],
),
html.Div(
    id='graph-container',
    children= dcc.Graph(
        id='price-chart',
        figure=fig,
        config={'displayModeBar': False}
        ),
),

if __name__ == '__main__':
    app.run_server(debug=True)
