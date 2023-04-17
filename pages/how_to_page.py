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
                            Learn more about using the world.ly application and its many features.\n
                            """
                            #Explore the different sections of the application and make your own complex queries!
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
                        html.H3("Explore relationships between relevant parameters"),
                        html.Hr(),
                        html.P(
                            """\
                            Visualize the trend between metrics over time on a dynamic scatter plot
                            """,
                        ),
                        html.Br(),
                        html.P(
                            """\
                            ◉   Select two metrics you want to compare
                            """,
                        ),
                        html.Br(),
                        html.P(
                            """\
                            ◉   After selecing the metrics, a scatter plot will appear with each dot representing a country
                            """,
                        ),
                        html.Br(),
                        html.P(
                            """\
                            ◉   Use the play/pause buttons to see the trend of the metrics over the years available
                            """,
                        ),
                        html.Br(),
                        html.P(
                            """\
                            ◉   Hovering over each dot will display the country and its resepctive data on both parameters
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
                ),
                dbc.Col(
                    [   
                        html.Br(),
                        html.Br(),
                        html.Br(),
                        html.Br(),
                        html.Br(),
                        html.Img(
                        src="assets\images\line-graph-example.jpg",
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
                        html.H3("Visually interpret complex queries using a dynamic globe"),
                        html.Hr(),
                        html.P(
                            """\
                            Use our built-in globe to visualize the queries!
                            """,
                        ),
                        html.Br(),
                        html.P(
                            """\
                            ◉   Select one of our complex queries
                            """,
                        ),
                        html.Br(),
                        html.P(
                            """\
                            ◉   Click and hold the globe to pan/navigate around 
                            """,
                        ),
                        html.Br(),
                        html.P(
                            """\
                            ◉   Hover over each dot to see the country and its specific metrics
                            """,
                        ),
                        html.Br(),
                        html.P(
                            """\
                            ◉   Each dot's size will vary based on the magnitude of the corresponding metric tracked
                            """,
                        ),
                        html.Br(),
                        html.P(
                            """\
                            ◉   Use the timeline below the globe to see the data by year
                            """,
                        ),
                        html.Br(),
                        html.P(
                            """\
                            ◉   Select the play/pause button (represented by symbols) to visualize the trend change over time
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
                        src="assets\images\world-map-example.jpg",
                        width="100%",
                        height="auto",
                        className=""
                        )
                    ],
                    className="centered",
                )
            ]
        ),
    ],
    className="mt-4 body-flex-wrapper",
)


def how_to_page(app: dash.Dash):
    layout = html.Div([nav, body, ftr], className="make-footer-stick")
    return layout