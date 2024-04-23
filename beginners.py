import dash
from dash import html #Used to create HTML Objects
from dash import dcc
import plotly.express as px # To create our graphs, a powerful functionality for processing data with minimal preparation
import pandas as pd
import csv

#Load and read the data
df = pd.read_csv("gcpEconomicSectors.csv")
df
#To create a plotly figure for use by dcc.graph()
fig = px.line(
    df, x='Year', 
    y=['GCP'], 
    title='GCP over the years', 
    color_discrete_map={'GCP':'gold'}
)


fig.update_layout(
    template ='plotly.dark',
    xaxis_title = 'Year',
    yaxis_title = 'GCP',
    font = dict(
        family ='Verdana, sans-serif',
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
#Drop Down List
html.Div(
    id='menu-area',
    children=[
        html.Div(
            children=[
                html.Div(
                    className='menu-title',
                    children='County'
                ),
                dcc.Dropdown(
                    id='county-filter',
                    className='dropdown',
                    options=[{'label':county,'value':county} for county in df.columns[1:]],
                    clearable=False
                )
            ]
            ),

    ]
)

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
