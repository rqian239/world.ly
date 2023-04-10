import dash
import dash_bootstrap_components as dbc
from dash import html


def footer():

    ftr = html.Div(
        dbc.Container(
            [
                dbc.Row(
                    [
                        dbc.Col(
                            html.Div([
                                html.H5("world.ly", className="text-uppercase footer-title"),
                            ]),
                            className="centered"
                        ),
                    ],
                    style={"margin-bottom": "30px"},
                ),
                dbc.Row(
                    [
                        dbc.Col(
                            html.Div([
                                html.H5("Quick Links", className="text-uppercase"),
                                dbc.NavLink("Home", href="/", className = "footer-link"),
                                dbc.NavLink("About", href="/about", className = "footer-link"),
                                dbc.NavLink("How to Use", href="/how_to", className = "footer-link"),
                                dbc.NavLink("Use world.ly", href="/app", className = "footer-link")                                
                            ]),
                            className="centered"
                        ),
                        dbc.Col(
                            html.Div([
                                html.P("Richard Qian"),
                                html.P("William Sobczak"),
                                html.P("Nikhil Pandya"),
                                html.P("Nicholas Borowski"),
                            ]),
                            className="centered"
                        ),
                    ],
                    className="justify-content-center"
                ),
                dbc.Row(
                    [
                        dbc.Col(
                            html.P("❤️")
                        )
                    ],
                    className="centered",
                ),
            ],
            fluid=True,
        ),
        className="p-5 mt-5 bg-light",
        style={"margin-top": "30px"},
    )
    return ftr