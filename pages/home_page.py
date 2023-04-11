import dash
import dash_bootstrap_components as dbc

from dash import html
from dash import dcc
from navbar import navbar
from footer import footer

from dash_iconify import DashIconify


nav = navbar()
ftr = footer()

body = dbc.Container(
    [
        # First Row, contains the title/blurb and the spinning earth gif
        dbc.Row(
            [
                dbc.Col(
                    [
                        html.H1("world.ly", className="home-page-title"),
                        html.Br(),
                        # home page blurb
                        html.P(
                            """\
                            Welcome!
                            This application gives you the power to discover complex insights into global demographic data.\n world.ly
                            allows you to study notable trends for the countries and metrics you choose. Explore and compare metrics from
                            various sectors like health, education, and economy.""",
                        ),
                        # Div for get started button
                        html.Div(
                            children=[
                                dcc.Link(
                                    html.Button(
                                        "Get Started",
                                        id="get-started-button",
                                        className="btn btn-lg btn-primary get-started-button",
                                        type="button"
                                    ),
                                    href="/app"
                                )
                            ],
                            className="centered",
                        )
                        
                    ],
                    md=6,
                ),
                dbc.Col(
                    [
                    # The spinning earth gif lmao
                        html.Img(
                            src="assets\images\earth.gif",
                            width="80%",
                            height="auto",
                            className="spinning-globe-gif"
                        )
                    ],
                    className="centered",
                    md=6,
                ),
            ]
        ),
        # New Row, contains sectors of interest title
        dbc.Row(
            [
                dbc.Col(
                    [
                        html.H3("Sectors of Interest"),
                        html.Hr(),
                    ]
                ),

            ],
            className="centered",
            style={"margin-top": "100px"},
        ),
        dbc.Row(
            [
                # Add a bunch of these dbc.Col to add icons for each sector
                dbc.Col(
                    [
                        html.H3("Health"),
                        # Search for icons here: https://icon-sets.iconify.design/
                        # Replace the name of the icon in the icon="" field
                        DashIconify(
                            icon="material-symbols:health-metrics",
                            width=50,
                            height=50,
                        )
                    ],
                ),
                dbc.Col(
                    [
                        html.H3("Economy"),
                        DashIconify(
                            icon="ph:piggy-bank-duotone",
                            width=50,
                            height=50,
                        )
                    ],
                ),
                dbc.Col(
                    [
                        html.H3("Energy"),
                        DashIconify(
                            icon="mdi:energy-circle",
                            width=50,
                            height=50,
                        )
                    ],
                ),
            ],
            className="centered",
        ),
        dbc.Row(
            [
                dbc.Col(
                    [
                        html.H2("Human Geography made simple."),
                        html.Br(),
                        html.P(
                            """\
                                Use world.ly to visualize hundreds of thousands of demographic data points.
                                """,
                        ),
                        
                    ],
                    className="centered",
                )
            ],
            style={"margin-top": "100px", "margin-bottom": "100px"},
        ),
    ],
    # mt-4 adds margin to the top
    className="mt-4 body-flex-wrapper",
)


def home_page(app: dash.Dash):
    layout = html.Div([nav, body, ftr], className="make-footer-stick")
    return layout