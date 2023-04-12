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
                            icon="material-symbols:health-metrics",
                            width=50,
                            height=50,
                        ),

                        DashIconify(
                            icon="ph:piggy-bank-duotone",
                            width=50,
                            height=50,
                        ),
                        
                        DashIconify(
                            icon="mdi:energy-circle",
                            width=50,
                            height=50,
                        ),

                        html.Br(),

                        DashIconify(
                            icon="material-symbols:emoji-people-rounded",
                            width=50,
                            height=50,
                        ),

                        DashIconify(
                            icon="mdi:education-outline",
                            width=50,
                            height=50,
                        ),

                        DashIconify(
                            icon="ion:skull-outline",
                            width=50,
                            height=50,
                        )
                    ],
                    className="centered",
                ),
                dbc.Col(
                    [   html.Br(),
                        html.Br(),
                        html.H3("Metrics Used"),
                        html.Hr(),
                    ],
                ),
            ],
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
                            width=50,
                            height=50,
                        ),

                        DashIconify(
                            icon="ph:globe-hemisphere-west-fill",
                            width=50,
                            height=50,
                        ),
                        
                        DashIconify(
                            icon="material-symbols:table-chart-outline",
                            width=50,
                            height=50,
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