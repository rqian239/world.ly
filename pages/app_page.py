import dash
import pandas as pd
import dash_bootstrap_components as dbc
import plotly.express as px

import plotly.graph_objs as go

from dash import html, dcc
from dash import dash_table
from components.navbar import navbar
from components.footer import footer

import functions


nav = navbar()
ftr = footer()

#query_string = '(SELECT year, life_expectancy_change_compared_to_last_5_years FROM ( SELECT year, ROUND(life_expectancy - past_5_yrs_avg_life_expectancy,4) life_expectancy_change_compared_to_last_5_years FROM ( SELECT year, life_expectancy, AVG(life_expectancy) OVER(ORDER BY year DESC ROWS BETWEEN 1 FOLLOWING AND 5 FOLLOWING) past_5_yrs_avg_life_expectancy FROM ( SELECT year, AVG(life_expectancy_at_birth) life_expectancy FROM LifeExpectancy GROUP BY year ORDER BY YEAR DESC ) ) WHERE YEAR > 1950 AND YEAR < 2020 ) ORDER BY life_expectancy_change_compared_to_last_5_years FETCH FIRST 5 ROWS ONLY) UNION ALL (SELECT year, life_expectancy_change_compared_to_last_5_years FROM (SELECT year, ROUND(life_expectancy - past_5_yrs_avg_life_expectancy,4) life_expectancy_change_compared_to_last_5_years FROM (SELECT year, life_expectancy, AVG(life_expectancy) OVER(ORDER BY year DESC ROWS BETWEEN 1 FOLLOWING AND 5 FOLLOWING) past_5_yrs_avg_life_expectancy FROM (SELECT year, AVG(life_expectancy_at_birth) life_expectancy FROM LifeExpectancy GROUP BY year ORDER BY YEAR DESC)) WHERE YEAR > 1950 AND YEAR < 2020) ORDER BY life_expectancy_change_compared_to_last_5_years DESC FETCH FIRST 5 ROWS ONLY)'
query_string = 'SELECT education.code, education.entity, education.percentage percentage_with_tertiary_education, income.value per_capita_income FROM ShareOfThePopulationWithCompletedTertiaryEducation education, GrossNationalIncomePerCapita income WHERE education.code = income.code AND education.year = income.year AND education.year = \'2010\' '
df = functions.query_db(query_string)

body = dbc.Container(
    [
        dbc.Row(
            [
                dbc.Col(
                    [
                        html.H1("Main Application"),
                        html.P(
                            """\
                            This is where we put the data visualizations."""
                        ),
                        html.Div([
                            dash_table.DataTable(
                                id='table',
                                columns=[{"name": i, "id": i} for i in df.columns],
                                data=df.to_dict('records'),
                                style_table={'width': '50%'},
                                style_cell={'textAlign': 'left', 'fontSize': 14}
                            )
                        ]),
                    ],
                    md=4,
                )
            ]
        )
    ],
    className="mt-4 body-flex-wrapper",
)

# fig = px.line(df, x="YEAR", y="BOTH_SEXES_MORTALITY_RATE", title='Adult Mortality Rate', color = 'COUNTRY')
# fig.update_xaxes(title_text=(reformat_data_label("YEAR")))
# fig.update_yaxes(title_text=(reformat_data_label("BOTH_SEXES_MORTALITY_RATE")))

scatter_fig = px.scatter(df, x='PERCENTAGE_WITH_TERTIARY_EDUCATION', y='PER_CAPITA_INCOME', hover_name='ENTITY', color='ENTITY')
scatter_fig.update_xaxes(title_text=(functions.reformat_data_label("PERCENTAGE_WITH_TERTIARY_EDUCATION")))
scatter_fig.update_yaxes(title_text=(functions.reformat_data_label("PER_CAPITA_INCOME")))
scatter_fig.update_layout(width=1500, height=1000)

scatter_plot_visualization = dbc.Container(
    [
    # Add dropdown and buttons here
        dbc.Row(
            [
            ]
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

world_map_fig = px.scatter_geo(df, locations = 'CODE',
                     color='ENTITY',
                     hover_name='ENTITY',
                     size='PERCENTAGE_WITH_TERTIARY_EDUCATION',
                     projection='orthographic')
world_map_fig.update_layout(width=1500, height=1000)

world_map_visualization = dbc.Container(
    [
    # Add dropdown and buttons here
        dbc.Row(
            [
            ]
        ),
        dbc.Row(
            [
                dbc.Col(
                    [
                        html.Div(
                            [
                                dcc.Graph(
                                    id='data-visualization',
                                    figure=world_map_fig
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



def app_page(app: dash.Dash):
    layout = html.Div([nav, body, scatter_plot_visualization, world_map_visualization, ftr], className="make-footer-stick")
    return layout