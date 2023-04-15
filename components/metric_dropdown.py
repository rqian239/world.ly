import dash
from dash import html, dcc
import ids
import data

def render(app: dash.Dash) -> html.Div:
    all_queries = ["Query 1", "Query 2", "Query 3"]
    return html.Div(
        children=[
            html.H6("Query"),
            dcc.Dropdown(
                id=ids.QUERY_DROPDOWN,
                options=[{"label": query, "value": query} for query in all_queries],
                value=all_queries
            )
        ])

def render_scatter_plot_dropdown(app: dash.Dash, input_id) -> html.Div:
    all_attributes = data.attribute_table_dict.keys()
    return html.Div(
        children=[
            dcc.Dropdown(
                id=input_id,
                options=[{"label": attribute, "value": attribute} for attribute in all_attributes],
                value=None,
            )
        ])
