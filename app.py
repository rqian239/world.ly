import dash
import cx_Oracle
import pandas as pd
import dash_bootstrap_components as dbc

from dash import dcc
from dash import html
from dash import dash_table
from dash.dependencies import Input, Output

from pages.home_page import home_page
from pages.about_page import about_page
from pages.how_to_page import how_to_page
from pages.app_page import app_page

# Themes? Try FLATLY, LUX, QUARTZ
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.FLATLY])
app.config.suppress_callback_exceptions = True
app.title = 'world.ly'

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

# app.layout = html.Div([
#     html.H1('world.ly'),
#     dash_table.DataTable(
#         id='table',
#         columns=[{"name": i, "id": i} for i in df.columns],
#         data=df.to_dict('records'),
#         style_table={'width': '50%'},
#         style_cell={'textAlign': 'left', 'fontSize': 14}
#     )
# ])

app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content')
])

@app.callback(
    Output('page-content', 'children'),
    [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/':
        return home_page()
    elif pathname == '/about':
        return about_page()
    elif pathname == '/how_to':
        return how_to_page()
    elif pathname == '/app':
        return app_page()
    else:
        return home_page()

if __name__ == '__main__':
    app.run()
    # app.run_server(debug=True)