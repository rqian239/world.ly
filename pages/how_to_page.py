import dash
import dash_bootstrap_components as dbc

from dash import html, dcc
from components.navbar import navbar
from components.footer import footer

from dash_iconify import DashIconify

import functions

nav = navbar()
ftr = footer()

body = dbc.Container(
    [
        dbc.Row(
            [
                dbc.Col(
                    [
                        html.H1("How to Use world.ly"),
                        html.Br(),
                        # home page blurb
                        html.P(
                            """\
                            Learn about using the world.ly application and its many features.
                            """
                        ),
                        html.Br(),
                        html.Div(
                            children=[
                                dcc.Link(
                                    html.Button(
                                        "Get Started",
                                        id="get-started-button-about-page",
                                        className="btn btn-lg btn-primary get-started-button-about-page",
                                        type="button"
                                    ),
                                    href="/app"
                                )
                            ],
                            className="centered",
                        )
                    ],
                    className="centered"
                )
            ]
        ),
        dbc.Row(
            [
                dbc.Col(
                    [
                        html.Br(),
                        html.Br(),
                        html.Br(),
                        html.Br(),
                        html.Br(),
                        html.H3("Select the metrics you want to compare"),
                        html.Hr(),
                        html.P(
                            """\
                            Description here.
                            """,
                        ),
                    ]
                ),
                dbc.Col(
                    [   
                        html.Br(),
                        html.Br(),
                        html.Br(),
                        html.Br(),
                        html.Br(),
                        html.Img(
                        src="assets\images\scatter-plot-example.jpg",
                        width="100%",
                        height="auto",
                        className=""
                        )
                    ],
                    className="centered",
                )
            ]
        ),
        dbc.Row(
            [
                dbc.Col(
                    [
                        html.Br(),
                        html.Br(),
                        html.Br(),
                        html.H3("See the trend with a timeline"),
                        html.Hr(),
                        html.P(
                            """\
                            Description here.
                            """,
                        ),
                    ]
                )
            ]
        ),
        dbc.Row(
            [
                dbc.Col(
                    [
                        html.Br(),
                        html.Br(),
                        html.Br(),
                        html.H3("Visually interpret complex queries using a globe"),
                        html.Hr(),
                        html.P(
                            """\
                            Description here.
                            """,
                        ),
                    ]
                )
            ]
        ),
    ],
    className="mt-4 body-flex-wrapper",
)


def how_to_page(app: dash.Dash):
    layout = html.Div([nav, body, ftr], className="make-footer-stick")
    return layout