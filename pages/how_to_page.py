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
    className="mt-4",
)


def how_to_page():
    layout = html.Div([nav, body])
    return layout