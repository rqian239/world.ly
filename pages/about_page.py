import dash
import dash_bootstrap_components as dbc

from dash import html
from dash import dcc

from components.navbar import navbar
from components.footer import footer

from dash_iconify import DashIconify

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
                    className="centered",
                )
            ]
        ),
        dbc.Row(
            [
                dbc.Col(
                    [   
                        html.Img(
                        src="assets\images\elements-silhouette-pixel-world-map-pixelated-vector.jpg",
                        width="100%",
                        height="auto",
                        className=""
                        )
                    ],
                    className="centered",
                ),
                dbc.Col(
                    [
                        html.H3("Metrics Used"),
                        html.Hr(),
                        html.P(
                            """\
                            Description of sectors chosen and corresponding metrics. Explain the relevance of metrics.
                            """,
                        ),
                        html.Br(),
                        html.P(
                            """\
                            ◉   Sector 1 (Economy): Metrics in Sector 1 (GDP, average income, inflation, etc.)
                            """,
                        ),
                        html.Br(),
                        html.P(
                            """\
                            ◉   Sector 2 (Health):  Metrics in Sector 2
                            """,
                        ),
                        html.Br(),
                        html.P(
                            """\
                            ◉   Sector 3 (Population): Metrics in Sector 3
                            """,
                        ),
                    ],
                ),
            ],
            style={"margin-top": "100px"},
        ),
        dbc.Row(
            [  
                dbc.Col(
                    [   html.Br(),
                        html.Br(),
                        html.Br(),
                        html.Br(),
                        html.Br(),
                        html.H3("Data Visualization and Trend Analysis"),
                        html.Hr(),
                        html.P(
                            """\
                            Visualize trends with world.ly. Generate graphs, charts, and maps of your selected data. Description of the visualization tools here. Describe the kinds of charts and graphs.
                            """,
                        ),
                        html.Br(), 
                        html.P(
                            """\
                            ◉   Line Graphs
                            """,
                        ),
                        html.Br(), 
                        html.P(
                            """\
                            ◉   Tables
                            """,
                        ),
                        html.Br(), 
                        html.P(
                            """\
                            ◉   Maps
                            """,
                        ),
                    ],
                    className="left",
                ),
                dbc.Col(
                    [   
                        html.Br(),
                        html.Br(),
                        html.Br(),
                        html.Br(),
                        html.Br(),
                        html.Br(),
                        html.Br(),
                        html.Br(),
                        html.Br(),
                        html.Br(),
                        # Search for icons here: https://icon-sets.iconify.design/
                        # Replace the name of the icon in the icon="" field
                        DashIconify(
                            icon="mdi:graph-line",
                            width=100,
                            height=100,
                        ),

                        DashIconify(
                            icon="ph:globe-hemisphere-west-fill",
                            width=100,
                            height=100,
                        ),
                        
                        DashIconify(
                            icon="material-symbols:table-chart-outline",
                            width=100,
                            height=100,
                        ),
                    ],
                    className="centered",
                ),
            ],
        ),
    ],
    className="mt-4 body-flex-wrapper",
)


def about_page(app: dash.Dash):
    layout = html.Div([nav, body, ftr], className="make-footer-stick")
    return layout