import dash
import cx_Oracle
import pandas as pd
import dash_bootstrap_components as dbc
import plotly.express as px

import plotly.graph_objs as go

from dash import html, dcc
from dash import dash_table
from components.navbar import navbar
from components.footer import footer

def query_db(sql_query):
    # These two lines of code are needed for the Oracle client to work on my Windows machine. If you are on windows,
        # replace the path with the path to your Oracle Instant Client (the path you added as an environment variable).
        # Otherwise, comment it out and disregard.
    path_of_oracle_instant_client = r"D:\Program Files\Oracle\instantclient_21_9"
    cx_Oracle.init_oracle_client(lib_dir=path_of_oracle_instant_client)

    # Connect to Oracle Database
    conn = cx_Oracle.connect(user='williamsobczak', password='REBY7TpizLTdOp5dZHa9qJS0',
                            dsn=cx_Oracle.makedsn('oracle.cise.ufl.edu', '1521',
                                                sid='orcl'))
    cursor = conn.cursor()
    cursor.execute(sql_query)
    results = cursor.fetchall()

    df = pd.DataFrame(results, columns=[desc[0] for desc in cursor.description])
    cursor.close()
    conn.close()

    return df

def reformat_data_label(label):
    words = label.split('_')
    formatted_words = [word.lower().capitalize() for word in words]
    return ' '.join(formatted_words)


nav = navbar()
ftr = footer()

#query_string = '(SELECT year, life_expectancy_change_compared_to_last_5_years FROM ( SELECT year, ROUND(life_expectancy - past_5_yrs_avg_life_expectancy,4) life_expectancy_change_compared_to_last_5_years FROM ( SELECT year, life_expectancy, AVG(life_expectancy) OVER(ORDER BY year DESC ROWS BETWEEN 1 FOLLOWING AND 5 FOLLOWING) past_5_yrs_avg_life_expectancy FROM ( SELECT year, AVG(life_expectancy_at_birth) life_expectancy FROM LifeExpectancy GROUP BY year ORDER BY YEAR DESC ) ) WHERE YEAR > 1950 AND YEAR < 2020 ) ORDER BY life_expectancy_change_compared_to_last_5_years FETCH FIRST 5 ROWS ONLY) UNION ALL (SELECT year, life_expectancy_change_compared_to_last_5_years FROM (SELECT year, ROUND(life_expectancy - past_5_yrs_avg_life_expectancy,4) life_expectancy_change_compared_to_last_5_years FROM (SELECT year, life_expectancy, AVG(life_expectancy) OVER(ORDER BY year DESC ROWS BETWEEN 1 FOLLOWING AND 5 FOLLOWING) past_5_yrs_avg_life_expectancy FROM (SELECT year, AVG(life_expectancy_at_birth) life_expectancy FROM LifeExpectancy GROUP BY year ORDER BY YEAR DESC)) WHERE YEAR > 1950 AND YEAR < 2020) ORDER BY life_expectancy_change_compared_to_last_5_years DESC FETCH FIRST 5 ROWS ONLY)'
query_string = '(SELECT education.entity, education.percentage percentage_with_tertiary_education, income.value per_capita_income FROM ShareOfThePopulationWithCompletedTertiaryEducation education, GrossNationalIncomePerCapita income WHERE education.code = income.code AND education.year = income.year AND education.year = 2010)'
df = query_db(query_string)

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

# data_visualization = dbc.Container(
#     [
#         dbc.Row(
#             [
#                 dbc.Col(
#                     [
#                         html.Div(
#                             [
#                                 dcc.Graph(
#                                     id='scatter-plot',
#                                     figure={
#                                         'data': [
#                                             go.Scatter(
#                                                 x=df['PERCENTAGE_WITH_TERTIARY_EDUCATION'],
#                                                 y=df['PER_CAPITA_INCOME'],
#                                                 mode='markers',
#                                                 text=df['ENTITY']
#                                             )
#                                         ],
#                                         'layout': go.Layout(
#                                             title='Sample Scatter Plot',
#                                             xaxis={'title': 'PERCENTAGE_WITH_TERTIARY_EDUCATION'},
#                                             yaxis={'title': 'PER_CAPITA_INCOME'}
#                                         )
#                                     }
#                                 )
#                             ]
#                         )
#                     ]
#                 )
#             ]
#         )
#     ]
# )

# fig = px.line(df, x="YEAR", y="BOTH_SEXES_MORTALITY_RATE", title='Adult Mortality Rate', color = 'COUNTRY')
# fig.update_xaxes(title_text=(reformat_data_label("YEAR")))
# fig.update_yaxes(title_text=(reformat_data_label("BOTH_SEXES_MORTALITY_RATE")))

fig = px.scatter(df, x='PERCENTAGE_WITH_TERTIARY_EDUCATION', y='PER_CAPITA_INCOME', hover_name='ENTITY', color='ENTITY')
fig.update_xaxes(title_text=(reformat_data_label("PERCENTAGE_WITH_TERTIARY_EDUCATION")))
fig.update_yaxes(title_text=(reformat_data_label("PER_CAPITA_INCOME")))

data_visualization = dbc.Container(
    [
        dbc.Row(
            [
                dbc.Col(
                    [
                        html.Div(
                            [
                                dcc.Graph(
                                    id='data-visualization',
                                    figure=fig
                                )
                            ]
                        )
                    ]
                )
            ]
        )
    ]
)


def app_page(app: dash.Dash):
    layout = html.Div([nav, body, data_visualization, ftr], className="make-footer-stick")
    return layout