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
                        html.Br(),
                        html.H1("Learn More About world.ly"),
                        html.Br(),
                        # home page blurb
                        html.P(
                            """\
                            world.ly is an easy-to-use web application that displays demographic data and allows you to study their trends.
                            """
                        )
                    ],
                    className="centered",
                )
            ]
        )
    ],
    className="mt-4 body-flex-wrapper",
)


def about_page(app: dash.Dash):
    layout = html.Div([nav, body, ftr], className="make-footer-stick")
    return layout