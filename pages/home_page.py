import dash
import dash_bootstrap_components as dbc

from dash import html
from navbar import navbar


nav = navbar()


body = dbc.Container(
    [
        dbc.Row(
            [
                dbc.Col(
                    [
                        html.H1("world.ly"),
                        # home page blurb
                        html.P(
                            """\
                            Welcome to world.ly!
                            This application gives you the power to discover complex insights into global demographic data.\n world.ly
                            allows you to study notable trends for the countries and metrics you choose. Explore and compare metrics from
                            various sectors like health, education, and economy."""
                        )
                    ],
                    md=4,
                )
            ]
        )
    ],
    className="mt-4",
)


def home_page():
    layout = html.Div([nav, body])
    return layout