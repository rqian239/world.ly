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

import ids

# Themes? Try FLATLY, LUX, QUARTZ
# https://towardsdatascience.com/3-easy-ways-to-make-your-dash-application-look-better-3e4cfefaf772
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.FLATLY])
app.config.suppress_callback_exceptions = True
app.title = 'world.ly'


app.layout = html.Div([
    dcc.Location(id=ids.CURRENT_URL, refresh=False),
    html.Div(id=ids.CURRENT_PAGE_CONTENT)
])

@app.callback(
    Output(ids.CURRENT_PAGE_CONTENT, 'children'),
    [Input(ids.CURRENT_URL, 'pathname')])
def display_page(pathname):
    if pathname == '/':
        return home_page(app)
    elif pathname == '/about':
        return about_page(app)
    elif pathname == '/how_to':
        return how_to_page(app)
    elif pathname == '/app':
        return app_page(app)
    else:
        return home_page(app)

if __name__ == '__main__':
    app.run()
    # app.run_server(debug=True)