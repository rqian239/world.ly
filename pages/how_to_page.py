import dash
import dash_bootstrap_components as dbc

from dash import html
from components.navbar import navbar
from components.footer import footer


nav = navbar()
ftr = footer()

body = dbc.Container(
    [
        dbc.Row(
            [
                dbc.Col(
                    [
                        html.H1("How to Use"),
                        # home page blurb
                        html.P(
                            """\
                            This is the How to Use Page."""
                        )
                    ],
                    md=4,
                )
            ]
        )
    ],
    className="mt-4 body-flex-wrapper",
)


def how_to_page(app: dash.Dash):
    layout = html.Div([nav, body, ftr], className="make-footer-stick")
    return layout