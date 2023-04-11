import dash
import cx_Oracle
import pandas as pd
import dash_bootstrap_components as dbc

from dash import html
from dash import dash_table
from navbar import navbar
from footer import footer

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
sql_query = 'SELECT * FROM adultmortality FETCH FIRST 20 ROWS ONLY'
cursor.execute(sql_query)
results = cursor.fetchall()

df = pd.DataFrame(results, columns=[desc[0] for desc in cursor.description])
cursor.close()
conn.close()


nav = navbar()
ftr = footer()

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
                        ])
                    ],
                    md=4,
                )
            ]
        )
    ],
    className="mt-4 body-flex-wrapper",
)


def app_page(app: dash.Dash):
    layout = html.Div([nav, body, ftr], className="make-footer-stick")
    return layout