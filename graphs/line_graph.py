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

line_graph_section = None

def render():
    return line_graph_section

def query_for_line_graph(parameter):
    return