import dash
import cx_Oracle
import pandas as pd
import dash_bootstrap_components as dbc
import plotly.express as px

from dash import dcc
from dash import html
from dash import dash_table
from dash.dependencies import Input, Output

from pages.home_page import home_page
from pages.about_page import about_page
from pages.how_to_page import how_to_page
from pages.app_page import app_page

import ids
import graphs.scatter_plot as scatter_plot
import functions
import numpy as np

# Themes? Try FLATLY, LUX, QUARTZ
# https://towardsdatascience.com/3-easy-ways-to-make-your-dash-application-look-better-3e4cfefaf772
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.FLATLY])
app.config.suppress_callback_exceptions = True
app.title = 'world.ly'


app.layout = html.Div([
    dcc.Location(id=ids.CURRENT_URL, refresh=False),
    html.Div(id=ids.CURRENT_PAGE_CONTENT)
])

# FUNCTION TO ROUTE TO DIFFERENT PAGES
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


# UPDATE SCATTER PLOT BASED ON DROPDOWN SELECTION
@app.callback(
    Output(ids.STATIC_SCATTER_PLOT_CONTAINER, 'children'),
    [Input(ids.SCATTER_PLOT_DROPDOWN_1, 'value'),
        Input(ids.SCATTER_PLOT_DROPDOWN_2, 'value')])
def update_scatter_plot(metric_1, metric_2):
    if metric_1 is None or metric_2 is None:
        return html.Div([html.H3('Please select two metrics to create a scatter plot. Use the dropdowns above.')], style={'textAlign': 'center', 'margin-top': '50px', 'margin-bottom': '50px'})
    else:
        df = scatter_plot.query_for_static_scatter_plot(metric_1, metric_2)
        all_countries = df['ENTITY'].unique().tolist()
        all_years = df['YEAR'].unique().tolist()
        complete_data = pd.DataFrame([(country, year) for country in all_countries for year in all_years], columns=['ENTITY', 'YEAR'])
        df = pd.merge(complete_data, df, on=['ENTITY', 'YEAR'], how='left')
        df['PARAMETER1'].replace(np.nan, None, inplace=True)
        df['PARAMETER2'].replace(np.nan, None, inplace=True)

        print(df.head())
        fig = px.scatter(df, x='PARAMETER1', y='PARAMETER2', hover_name='ENTITY', color='ENTITY', animation_frame='YEAR', animation_group='ENTITY')
            # animated_plot = px.scatter(df_animation, x='PERCENTAGE_WITH_TERTIARY_EDUCATION', y='PER_CAPITA_INCOME',
    #                             animation_frame='YEAR',
    #                             animation_group='ENTITY',
    #                             hover_name='ENTITY', color='ENTITY')
        fig.update_xaxes(title_text=metric_1)
        fig.update_yaxes(title_text=metric_2)
        fig.update_layout(width=1300, height=1000)
        return dcc.Graph(id=ids.STATIC_SCATTER_PLOT, figure=fig)



if __name__ == '__main__':
    app.run()
    # app.run_server(debug=True)