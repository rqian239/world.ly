import dash
import pandas as pd
import dash_bootstrap_components as dbc
import plotly.express as px
import numpy as np

import plotly.graph_objs as go

from dash import html, dcc
from dash import dash_table
from components.navbar import navbar
from components.footer import footer

import components.dropdown as dropdown
import ids
import functions
import data

# Set up blank line graph
blank_df = pd.DataFrame()
blank_fig = px.line(blank_df)

line_graph_section = dbc.Container([
        dbc.Row(
            dbc.Col(
                [
                    html.H4('Choose a metric.'),
                    dcc.Dropdown(
                        id=ids.LINE_GRAPH_DROPDOWN,
                        options=[{'label': i, 'value': i} for i in data.attribute_table_dict.keys()],
                        value=None,
                        multi=False,
                        className = 'dropdown-style',
                    ),
                    html.Br(),
                    html.Br(),
                    dcc.Dropdown(
                        id=ids.SORTING_DROPDOWN,
                        options=[{'label': i, 'value': i} for i in data.line_graph_options],
                        value=None,
                        multi=False,
                        className = 'dropdown-style',
                    ),
                ],
                style={'margin-top': '50px', 'margin-bottom': '50px'},
                className='centered'
            )
        ),
],
    className = 'scatter-plot-container'
)

def render():
    return line_graph_section

def query_for_line_graph(parameter):
    return