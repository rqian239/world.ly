import dash
import dash_bootstrap_components as dbc

from dash import html
from navbar import navbar
from footer import footer

nav = navbar()
ftr = footer()

body = dbc.Container(
    [
        dbc.Row(
            [
                dbc.Col(
                    [
                        html.H1("Main Application HERE"),
                        # home page blurb
                        html.P(
                            """\
                            This is where we put all the data and graphs and stuff."""
                        )
                    ],
                    md=4,
                )
            ]
        )
    ],
    className="mt-4 body-flex-wrapper",
)


def app_page():
    layout = html.Div([nav, body, ftr], className="make-footer-stick")
    return layout