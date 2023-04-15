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

query_string = 'SELECT education.code, education.entity, education.year, education.percentage_with_tertiary_education percentage_with_tertiary_education, income.gross_national_income_per_capita per_capita_income FROM ShareOfThePopulationWithCompletedTertiaryEducation education, GrossNationalIncomePerCapita income WHERE education.code = income.code AND education.year = income.year AND education.year = \'2010\' '
df = functions.query_db(query_string)

# x='PERCENTAGE_WITH_TERTIARY_EDUCATION'
# y='PER_CAPITA_INCOME'
# coefficients = np.polyfit(x, y, 1)
# line = coefficients[0] * x + coefficients[1]

scatter_fig = px.scatter(df, x='PERCENTAGE_WITH_TERTIARY_EDUCATION', y='PER_CAPITA_INCOME', hover_name='ENTITY', color='ENTITY')
scatter_fig.update_xaxes(title_text=(functions.reformat_data_label("PERCENTAGE_WITH_TERTIARY_EDUCATION")))
scatter_fig.update_yaxes(title_text=(functions.reformat_data_label("PER_CAPITA_INCOME")))

# scatter_fig.add_trace(px.line(x=x, y=line).data[0])

scatter_fig.update_layout(width=1300, height=1000)

scatter_plot_section = dbc.Container(
    [
    # Add dropdown and buttons here
        dbc.Row(
            dbc.Col(
                [
                html.H6('Choose a metric'),
                dcc.Dropdown(
                    id=ids.SCATTER_PLOT_DROPDOWN_1,
                    options=[{'label': i, 'value': i} for i in data.attribute_table_dict.keys()],
                    value=None,
                    multi=False
                ),
                dcc.Dropdown(
                    id=ids.SCATTER_PLOT_DROPDOWN_2,
                    options=[{'label': i, 'value': i} for i in data.attribute_table_dict.keys()],
                    value=None,
                    multi=False
                ),
                ]
            )
        ),
        dbc.Row(
            [
                dbc.Col(
                    [
                        html.Div(
                            [
                                dcc.Graph(
                                    id='data-visualization',
                                    figure=scatter_fig
                                ),
                            ],
                            # className="center-content"
                        )
                    ]
                )
            ]
        ),
    ]
)

def render():
    return scatter_plot_section