import dash
import cx_Oracle
import pandas as pd
import dash_bootstrap_components as dbc
import plotly.express as px

from dash import html, dcc
from dash import dash_table
from components.navbar import navbar
from components.footer import footer

def query_db(sql_query):
    # These two lines of code are needed for the Oracle client to work on my Windows machine. If you are on windows,
        # replace the path with the path to your Oracle Instant Client (the path you added as an environment variable).
        # Otherwise, comment it out and disregard.
    path_of_oracle_instant_client = r"C:\Program Files\Oracle\instantclient_21_9"
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

df = query_db('SELECT * FROM adultmortality FETCH FIRST 20 ROWS ONLY')

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

fig = px.line(df, x="YEAR", y="BOTH_SEXES_MORTALITY_RATE", title='Adult Mortality Rate', color = 'COUNTRY')
fig.update_xaxes(title_text=(reformat_data_label("YEAR")))
fig.update_yaxes(title_text=(reformat_data_label("BOTH_SEXES_MORTALITY_RATE")))

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