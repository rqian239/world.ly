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
        dbc.Row(
            [
                dbc.Col(
                    [
                        html.Div(
                            children=[
                                dcc.Graph(
                                    id=ids.LINE_GRAPH,
                                    figure=blank_fig,
                                ),
                            ],
                            id=ids.LINE_GRAPH_CONTAINER,
                        )
                    ]
                )
            ]
        ),
    ],
    className = 'scatter-plot-container'
)

def query_for_line_graph(parameter):
    return


def render():
    return line_graph_section

def render_line_graph(parameter, sorting_option):

    table_with_the_parameter = data.attribute_table_dict[parameter]
    formatted_parameter = functions.format_attribute_name_for_sql(parameter).upper()

    if sorting_option == data.line_graph_options[0]:
        # TOP 10
        ordering = 'DESC'
    elif sorting_option == data.line_graph_options[1]:
        # BOTTOM 10
        ordering = 'ASC'
    else:
        # DEFAULT: TOP 10
        ordering = 'DESC'

    query_string = f'WITH desired_codes AS ( SELECT code FROM (     SELECT code, AVG({formatted_parameter}) avg_parameter_value     ' \
                    f'FROM {table_with_the_parameter}     WHERE code NOT LIKE \'%OWID%\'     ' \
                    f'GROUP BY code     HAVING AVG({formatted_parameter}) IS NOT NULL     ORDER BY avg_parameter_value {ordering}     FETCH FIRST 10 ROWS ONLY ) )  ' \
                    f'SELECT continents.entity, year, {formatted_parameter} FROM {table_with_the_parameter}, desired_codes, (SELECT entity, code, continent FROM Continents) continents ' \
                    f'WHERE {table_with_the_parameter}.code = desired_codes.code AND {formatted_parameter} IS NOT NULL AND continents.code = {table_with_the_parameter}.code'

    print(query_string)
    

    df = functions.query_db(query_string)

    print(df.head(10))


    fig = px.line(df, x="YEAR", y=formatted_parameter, color="ENTITY", line_group="ENTITY", hover_name="ENTITY")
    fig = fig.update_layout(width=1250, height=800)
    fig.update_xaxes(title_text='Year')
    fig.update_yaxes(title_text=parameter)

    line_graph_figure = html.Div(children=[
            html.H1("Line Graph"),
            dcc.Graph(id='data-visualization', figure=fig)
    ], className="centered")


    return line_graph_figure

